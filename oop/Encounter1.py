
from rich_pixels import Pixels
from rich.console import Console
from rich.segment import Segment
from rich.style import Style
from klasserTest import Brawler, Enemy, start_combat


def move_down(grid, start_row, end_row, amount):
    rows = [list(row) for row in grid.splitlines()]

    width = max(len(row) for row in rows)
    rows = [row + ["."] * (width - len(row)) for row in rows]

    pixels_to_move = []

    for y in range(start_row, end_row):
        for x in range(width):
            if rows[y][x] not in [".", " "]:
                pixels_to_move.append((x, y, rows[y][x]))
                rows[y][x] = "."

    for x, y, pixel in pixels_to_move:
        rows[y + amount][x] = pixel

    return "\n".join("".join(row) for row in rows)


def start_battle(player):
    print("start_battle kjører")
    console = Console()

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

    grid = move_down(grid, 2, 11, 16)

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

    pixels = Pixels.from_ascii(grid, mapping)

    console.clear()
    console.print(pixels)

    input("\nTrykk Enter for å starte kampen...")

  
    enemies = [
        Enemy(60, 8),
        Enemy(40, 6),
        Enemy(100, 12)
    ]

    for enemy in enemies:
        start_combat(player, enemy)

        if player.hp <= 0:
            break

    input("\nTrykk Enter for å fortsette...")
    console.clear()


