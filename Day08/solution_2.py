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


def check_visibility(data, row):
    if not row:
        return 1
    if len(row) <= 1:
        return 1

    for idx, value in enumerate(row):
        if value >= data:
            return idx + 1
    return len(row)


# print(*grid, sep="\n")
scenic_score = 0
for row in range(row_count):
    for col in range(column_count):

        # skip if it is a edge tree, it not hidden DUH
        if row == 0 or col == 0 or row == row_count - 1 or col == column_count - 1:
            continue

        top = [x[col] for x in grid[:row]][::-1]
        bottom = [x[col] for x in grid[row + 1:]]
        left = grid[row][:col][::-1]
        right = grid[row][col + 1:]

        top_visibility = check_visibility(grid[row][col], top)
        bottom_visibility = check_visibility(grid[row][col], bottom)
        left_visibility = check_visibility(grid[row][col], left)
        right_visibility = check_visibility(grid[row][col], right)

        score = top_visibility * bottom_visibility * left_visibility * right_visibility

        if score > scenic_score:
            scenic_score = score

print(scenic_score)
