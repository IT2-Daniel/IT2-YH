
from rich_pixels import Pixels
from rich.console import Console
from rich.segment import Segment
from rich.style import Style
import msvcrt
from Encounter1 import start_battle
from klasserTest import Brawler,Wizard

print("Brettet starter")


console = Console()

grid = """ 

 ..............vvvvvvvvvvvv.............................
 ..............vggqqqvrrqqv.............................
 ..............vvvqqqvqqqqv.............................
 ..............vrrqqqqqrrqv.............................
 ..............vvvvvvvvvvvv.............................
 
"""
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

for y in range(len(rows)):
    for x in range(width):
        if rows[y][x] == "g":
            under_player[(x, y)] = "."

def choose_class():
    print("VELG KLASSE")
    print("1: Brawler")
    print("2: Wizard")

    while True:
        valg = input("> ")

        if valg == "1":
            print("Du valgte Brawler!")
            return Brawler(100, 10, 5, 10, 20)

        elif valg == "2":
            print("Du valgte Wizard!")
            return Wizard(80, 20, 7, 2, 25)

        else:
            print("Ugyldig valg!")

player_character = choose_class()

def draw():
    current_grid = "\n".join("".join(row) for row in rows)
    pixels = Pixels.from_ascii(current_grid, mapping)

    console.clear()
    console.print(pixels)
    print("\nWASD = Beveg | Q = Avslutt")




def move_player(dx, dy):
    print("MOVE PLAYER KJØRER")
    global under_player

    # Finn spilleren
    player = []

    for y in range(len(rows)):
        for x in range(width):
            if rows[y][x] == "g":
                player.append((x, y))

    # Fjern spilleren og gjenopprett bakgrunnen
    for x, y in player:
        rows[y][x] = under_player[(x, y)]

    # Sjekk om bevegelsen er mulig
    print("Spillerposisjoner:", player)
    battle_encounter = False
    can_move = True

    for x, y in player:
        new_x = x + dx
        new_y = y + dy

        if not (0 <= new_x < width and 0 <= new_y < len(rows)):
            can_move = False
            break

        if rows[new_y][new_x] == "r":
            print("Encounter!")
            battle_encounter = True
            break

        if rows[new_y][new_x] not in [".", " ", "q"]:
            can_move = False
            break

    # Start kamp hvis spilleren treffer r
    if battle_encounter:
        for x, y in player:
            rows[y][x] = "g"

        start_battle(player_character)
        return

    # Flytt spilleren
    if can_move:
        new_under_player = {}

        for x, y in player:
            new_x = x + dx
            new_y = y + dy

            new_under_player[(new_x, new_y)] = rows[new_y][new_x]
            rows[new_y][new_x] = "g"

        under_player = new_under_player

    else:
        # Sett spilleren tilbake
        for x, y in player:
            rows[y][x] = "g"



# Spilløkke
draw()

while True:
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

    draw()
