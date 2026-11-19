
from rich_pixels import Pixels
from rich.console import Console
from rich.segment import Segment
from rich.style import Style
import msvcrt

#importerer funksjon som starter kampen
from Encounter1 import start_battle
from Klasser import Brawler,Wizard

print("Brettet starter")


console = Console()

#griden for hovedbrettet
grid = """ 

 ..............vvvvvvvvvvvv.............................
 ..............vggqqqvrrqqv.............................
 ..............vvvqqqvqqqqv.............................
 ..............vrrqqqqqrrqv.............................
 ..............vvvvvvvvvvvv.............................
 
"""
#lagrer originalversjon av brettet
start_grid = grid

mapping = {
    "x": Segment(" ", Style.parse("white on #CC9966")),
    "b": Segment(" ", Style.parse("white on #000000")),
    "w": Segment(" ", Style.parse("white on #e6e6e6")),
    "a": Segment(" ", Style.parse("white on #999999")),
    "g": Segment(" ", Style.parse("white on #FFCC00")),
    "h": Segment(" ", Style.parse("white on #663300")),
    "q": Segment(" ", Style.parse("white on #666666")),
    ".": Segment(" ", Style.parse("")),
    " ": Segment(" ", Style.parse("")),
    "r": Segment(" ", Style.parse("white on #990000")),
    "p": Segment(" ", Style.parse("white on #E6C299")),
    "c": Segment(" ", Style.parse("white on #000066")),
    "l": Segment(" ", Style.parse("white on #CC00FF")),
    "v": Segment(" ", Style.parse("white on #333333"))
}

# Gjør griden om til en liste
rows = [list(row) for row in start_grid.strip("\n").splitlines()]


# Sørg for at alle radene har samme bredde
width = max(len(row) for row in rows)
rows = [row + ["."] * (width - len(row)) for row in rows]

# Husk bakgrunnen under spilleren
under_player = {}

#går gjennom brettet og finner spillerens startposisjon
for y in range(len(rows)):
    for x in range(width):
        if rows[y][x] == "g":
            under_player[(x, y)] = "."

def choose_class():
    #lar spilleren velge klasse
    print("VELG KLASSE")
    print("1: Brawler")
    print("2: Wizard")

    #fortsetter helt til man velger en gyldig klasse
    while True:
        valg = input("> ")

        if valg == "1":
            print("Du valgte Brawler!")
            #oppretter et brawlerobjekt med verdier for hp, mp, speed, baseDamage og baseAbilityDamage
            return Brawler(100, 10, 5, 10, 20)

        elif valg == "2":
            print("Du valgte Wizard!")
            #Oppretter Wizardobjekt med verdier for akkurat det samme
            return Wizard(80, 20, 7, 2, 25)

        else:
            print("Ugyldig valg!")

#oppretter spilleren en gang så inventory og stats beholdes mellom kampene
player_character = choose_class()

def draw():
    #Gjør listene i griden til str igjen
    current_grid = "\n".join("".join(row) for row in rows)
    #konverterer grid til grafikk
    pixels = Pixels.from_ascii(current_grid, mapping)

    #tømmer terminal og tegner brettet
    console.clear()
    console.print(pixels)
    #viser kontrollene
    print("\nWASD = Beveg | Q = Avslutt")




def move_player(dx, dy):
    #beveger spiller i retningen til inputet
    #dx er horisontal bevegelse 
    #dy er vertikal
    print("MOVE PLAYER KJØRER")
    #oppdaterer bakgrunnen under spilleren globalt
    global under_player

    # Finn spilleren koordinater
    player = []

    #finner cellene som tilhører spillerens sprite
    for y in range(len(rows)):
        for x in range(width):
            if rows[y][x] == "g":
                player.append((x, y))

    # Fjern spilleren midlertidig og gjenopprett bakgrunnen
    for x, y in player:
        rows[y][x] = under_player[(x, y)]

    # Sjekk om bevegelsen er mulig
    print("Spillerposisjoner:", player)
    battle_encounter = False #blir True hvis man treffer en fiende
    can_move = True #bestemmer om bevegelsen er tillatt


    #skjekker celler innenfor spilleresn sprite
    for x, y in player:
        new_x = x + dx
        new_y = y + dy

        #skjekker om ny posisjon e innenfor brettet

        if not (0 <= new_x < width and 0 <= new_y < len(rows)):
            can_move = False
            break

            #starter encounter hvis man treffer en r altså fiende
        if rows[new_y][new_x] == "r":
            print("Encounter!")
            battle_encounter = True
            break

        #kan kun flytte seg til . eller q
        if rows[new_y][new_x] not in [".", " ", "q"]:
            can_move = False
            break

    # Start kamp hvis spilleren treffer r
    if battle_encounter:
        #setter spiller tilbake på brettet
        for x, y in player:
            rows[y][x] = "g"

        #sender eksisterende spillerobjekt til kamp
        start_battle(player_character)
        return

    # Flytt spilleren
    if can_move:
        new_under_player = {}

        for x, y in player:
            new_x = x + dx
            new_y = y + dy

            #lagrer hva som er under spillers nye posisjon
            new_under_player[(new_x, new_y)] = rows[new_y][new_x]
            #plasserer spiller på ny posisjon
            rows[new_y][new_x] = "g"

        #oppdaterer bakgrunnsdata
        under_player = new_under_player

    else:
        # Sett spilleren tilbake om bevegelsen ikke går
        for x, y in player:
            rows[y][x] = "g"



# Spilløkke
#tegner brettet før start
draw()

while True:
    #Leser ett og ett input
    key = msvcrt.getch().lower()

    if key == b'\x00' or key == b'\xe0':
        msvcrt.getch()
        continue    

    if key == b'w':
        move_player(0, -1)

    elif key == b's':
        move_player(0, 1)

    elif key == b'a':
        move_player(-1, 0)

    elif key == b'd':
        move_player(1, 0)

    elif key == b'q':
        console.clear()
        print("Takk for spillet!")
        break

    #tegner brett på nytt etter hver tast
    draw()
