import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--input", help="Input File name")

args = parser.parse_args()

fileName = args.input

files = open(fileName, 'r')

lines = files.readlines()

grid = []

# Creting a input grid
for index, value in enumerate(lines):
    grid.append([int(i) for i in str(value.strip())])

row_count = len(grid)
column_count = len(grid[0])

# print(*grid, sep="\n")
count_edge = 0
count_interior = 0

for row in range(row_count):
    for col in range(column_count):

        # count the outer as visible
        if row == 0 or col == 0 or row == row_count - 1 or col == column_count - 1:
            count_edge += 1
            continue

        top = [x[col] for x in grid[:row]]
        bottom = [x[col] for x in grid[row + 1:]]
        left = grid[row][:col]
        right = grid[row][col + 1:]

        # check if the height is larger than the surrounding
        j = grid[row][col]
        if j > max(top) or j > max(bottom) or j > max(left) or j > max(right):
            count_interior += 1
            continue

print(count_edge)
print(count_interior)

print(count_edge + count_interior)
