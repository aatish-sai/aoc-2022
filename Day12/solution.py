import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--input", help="Input File name")

args = parser.parse_args()

fileName = args.input

files = open(fileName, 'r')

lines = files.readlines()

inputgrid = []

# generate grid input for problem
for index, value in enumerate(lines):
    row = list(value.strip())
    inputgrid.append(row)

print(inputgrid)


class Position:

    def __init__(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = dist

    def __repr__(self):
        return f"Position {self.row} {self.col} {self.dist}"


def isValidMove(x, y, currentValue, grid, visited):

    # out of bound
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        print(f"Out of bound")
        return False
    # already visited
    if visited[x][y]:
        print(f"Already visited position {x},{y}")
        return False

    if currentValue == 'S':
        currentValue = 'a'
    
    destinationValue = grid[x][y]
    if destinationValue == 'E':
        destinationValue = 'z'
    if destinationValue == 'S':
        destinationValue = 'a'
    if ord(currentValue) + 1 >= ord(destinationValue):
        print(f"{currentValue} > {grid[x][y]}")
        return True

    if grid[x][y] == "E" and currentValue == 'y':
        print(f"Final move")
        return True

    print(f"Move not possible from {currentValue} to {x}, {y}")
    return False

def solve_all(grid):
    result = []
    # find the statring positions
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] in ('S','a'):
                result.append(solve(grid, row, col))

    print(sorted(result))

    return min(result)

def solve(grid, row, col):
    source = Position(row, col, 0)

    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    queue = []
    queue.append(source)
    visited[source.row][source.col] = True

    while len(queue) != 0:
        source = queue.pop(0)
        print(f"From {repr(source)}")
        # Destination Found
        if grid[source.row][source.col] == 'E':
            return source.dist

        # up
        if isValidMove(source.row - 1, source.col,
                       grid[source.row][source.col], grid, visited):
            queue.append(Position(source.row - 1, source.col, source.dist + 1))
            visited[source.row - 1][source.col] = True

        # down
        if isValidMove(source.row + 1, source.col,
                       grid[source.row][source.col], grid, visited):
            queue.append(Position(source.row + 1, source.col, source.dist + 1))
            visited[source.row + 1][source.col] = True
        # left
        if isValidMove(source.row, source.col - 1,
                       grid[source.row][source.col], grid, visited):
            queue.append(Position(source.row, source.col - 1, source.dist + 1))
            visited[source.row][source.col - 1] = True
        # right
        if isValidMove(source.row, source.col + 1,
                       grid[source.row][source.col], grid, visited):
            queue.append(Position(source.row, source.col + 1, source.dist + 1))
            visited[source.row][source.col + 1] = True
        print("============================================")
    return -1


print(solve_all(inputgrid))
