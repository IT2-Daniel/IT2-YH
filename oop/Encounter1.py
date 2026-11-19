
from rich_pixels import Pixels
from rich.console import Console
from rich.segment import Segment
from rich.style import Style
from Klasser import Brawler, Enemy, start_combat


#fått av AI 
#flytter valgte deler av griden nedover for å få den krabben ned på bakkenivå uten å trenge å gjøre alt på nytt
def move_down(grid, start_row, end_row, amount):
    #gjør alle radene til en liste med tegn som alle ender opp i en liste 
    rows = [list(row) for row in grid.splitlines()]

    #setter bredden av alle radene lik den lengste 
    width = max(len(row) for row in rows)
    rows = [row + ["."] * (width - len(row)) for row in rows]

    pixels_to_move = []

    #går gjennom rader/kolonner som skal flyttes
    for y in range(start_row, end_row):
        for x in range(width):
            #flytter alt som ikke er tomrom eller punktum av det som skal flyttes
            if rows[y][x] not in [".", " "]:
                pixels_to_move.append((x, y, rows[y][x]))
                #fjerne piksel fra opprinnelig posisjon eller egt bytter d ut med . men d blir da tomrom
                rows[y][x] = "."
    #plasserer pikslene i nye posisjoner
    for x, y, pixel in pixels_to_move:
        rows[y + amount][x] = pixel

    #gjør listen om til en str igjen
    return "\n".join("".join(row) for row in rows)


def start_battle(player):
    #starter encounter og sender spilleren inn som parameter
    print("start_battle kjører")
    console = Console()


    #gridden viser kampbakgrunnen
    grid = """
..........................................................................................
..............................................r...............r.........................
............................................r.rr.............rr.r.......................
...........................................rr..rr..b.....b..rr..rr......................
............................................rrrr...r.....r...rrrr.......................
................................................r.rrrrrrrrr.r...........................
...............................................rrrrbwbwbwbrrrr..........................
..............................................rpppppppppppppppr.........................
.............................................r.r..r.r..r.r.r.r.r........................
............................................r..r..r.r..r.r.r.r..r..........................
..........................................................................................
..........................................................................................
..........................................................................................
..............cccccc...................................................................
.............c...cccc.....................................................................
...............cccccccc....................................................................
..............ccxbxxbxcc.....hhhh.........................................................
................xxxxxx......h.ll.h..........................................................
................xwwwwx.....h..hhh..........................................................
..................xx.......h..............................................................
..........xxccccccccccccccxx...............................................................
..................cc.......h..............................................................
..................cc.......h..............................................................
................cccccc.....h..............................................................
................c....c....................................................................
................x....x...................................................................................
vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
"""

    #justerer plassering
    grid = move_down(grid, 2, 11, 16)

    #bestemmer farge til hvert tegn i gridden
    mapping = {
        "x": Segment(" ", Style.parse("white on #CC9966")),
        "b": Segment(" ", Style.parse("white on #000000")),
        "w": Segment(" ", Style.parse("white on #e6e6e6")),
        "a": Segment(" ", Style.parse("white on #999999")),
        "g": Segment(" ", Style.parse("white on #FFCC00")),
        "h": Segment(" ", Style.parse("white on #663300")),
        "q": Segment(" ", Style.parse("white on #666666")),
        ".": Segment(" ", Style.parse("")),
        "r": Segment(" ", Style.parse("white on #990000")),
        "p": Segment(" ", Style.parse("white on #E6C299")),
        "c": Segment(" ", Style.parse("white on #000066")),
        "l": Segment(" ", Style.parse("white on #CC00FF")),
        "v": Segment(" ", Style.parse("white on #333333"))
    }

    #konverterer til et bilde som kan vises i terminal
    pixels = Pixels.from_ascii(grid, mapping)

    #tømmer terminal, viser kampgraffikk
    console.clear()
    console.print(pixels)

    #trykk enter for å starte kamp
    input("\nTrykk Enter for å starte kampen...")


  #lager en liste med tre forskjellige enemyobjekter med verdier for hp og baseDamage
    enemies = [
        Enemy(60, 8),
        Enemy(40, 6),
        Enemy(100, 12)
    ]

    #starter kamp mot neste enemy i listen når du har drept den forrige
    for enemy in enemies:
        start_combat(player, enemy)

        #avslutter hvis du dør
        if player.hp <= 0:
            break

    #trykk enter for å gå tilbake til hovedbrettet
    input("\nTrykk Enter for å fortsette...")
    console.clear()


