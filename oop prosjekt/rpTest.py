from rich_pixels import Pixels
from rich.console import Console
from rich.segment import Segment
from rich.style import Style

console = Console()

grid = """ 
 ..........................................................................................
 ..........................................................................................
 ..........................................................................................
 ..........................................................................................
 ..........................................................................................
 ..........................................................................................
 ............a...................................r...............r.........................
 ....hhhhh..aqa................................r.rr.............rr.r.......................
 ...hxxxxxh.aqa...............................rr..rr..b.....b..rr..rr......................
 ....xbxbx..aqa................................rrrr...r.....r...rrrr.......................
 ....xwwwx.ggggg...................................r.rrrrrrrrr.r...........................
 ......x.....g....................................rrrrbwbwbwbrrrr..........................
 .xhhhhhhhhhhx...................................rpppppppppppppppr.........................
 ......h........................................r.r..r.r..r.r.r.r.r........................
 .....hhh......................................r..r..r.r..r.r.r.r..r.......................
 .....x.x..................................................................................
 vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
 vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv


    
"""

#Fått fra AI
def move_right_down(grid, split_x, amount):
    rows = [list(row) for row in grid.splitlines()]

    width = max(len(row) for row in rows)
    rows = [row + ["."] * (width - len(row)) for row in rows]

    # Finn alle piksler på høyre side
    pixels = []

    for y in range(len(rows)):
        for x in range(split_x, width):
            if rows[y][x] not in [".", " ", "v"]:
                pixels.append((x, y, rows[y][x]))
                rows[y][x] = "."

    # Plasser dem på nytt
    for x, y, pixel in pixels:
        rows[y + amount][x] = pixel

    return "\n".join("".join(row) for row in rows)


grid = move_right_down(grid, 40, 1)

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

console.print(pixels)