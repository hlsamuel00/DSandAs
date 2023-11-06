class Point:
    def __init__(self, row: int, column: int) -> None:
        self.row = row
        self.column = column

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Point):
            return self.row == other.row and self.column == other.column
        return False
    

direction = [
    [-1, 0],
    [1, 0],
    [0, 1],
    [0, -1]
]

def maze_solver(maze: list[str], wall: str, start: Point, end: Point) -> list[Point]:

    def walk(m: list[str], w: str, cur: Point, e: Point, seen: list[list[bool]], path: list[Point]) -> bool:
        
        # Are we off the map
        if cur.column < 0 or cur.column >= len(m[0]) or cur.row < 0 or cur.row >= len(m):
            return False
        
        # Are we on a wall
        if m[cur.row][cur.column] == w:
            return False
        
        # Have we been here before
        if seen[cur.row][cur.column]:
            return False
        
        # Are we at the end
        if cur == e:
            path.append((cur.column, cur.row))
            return True
        
        # pre
        seen[cur.row][cur.column] = True
        path.append((cur.column, cur.row))
        
        # recurse
        for step in direction:
            column, row = step
            if walk(m, w, Point(cur.row + row, cur.column + column), e, seen, path):
                return True
        
        # post
        path.pop()
        return False
        
    seen = [[False] * len(row) for row in maze]
    path = []

    walk(maze, wall, start, end, seen, path)

    return path

maze_solver_maze = [
        "xxxxxxxxxx x",
        "x        x x",
        "x        x x",
        "x xxxxxxxx x",
        "x          x",
        "x xxxxxxxxxx",
    ]



#============================================================================================================
# CLEANED UP:


def maze_solver(maze: list[str], wall: str, start: Point, end: Point) -> list[Point]:
    
    def walk(m: list[str], w: str, cur: Point, e: Point, seen: list[list[bool]], path: list[Point]) -> bool:
        if cur.column < 0 or cur.row < 0 or cur.column > len(m[0]) or cur.row > len(m):
            return False
        
        if m[cur.row][cur.column] == w or seen[cur.row][cur.column]:
            return False
        
        if cur == e:
            path.append((cur.row, cur.column))
            return True
        
        seen[cur.row][cur.column] = 1
        path.append((cur.row, cur.column))

        for step in direction:
            row, column = step
            if walk(m, w, Point(cur.row + row, cur.column + column), e, seen, path):
                return True

        path.pop()
        return False
    
    seen = [[0] * len(row) for row in maze]
    path = []

    walk(maze, wall, start, end, seen, path)
    return path

print(maze_solver(maze_solver_maze, 'x', Point(0, 10), Point(5, 1)))
