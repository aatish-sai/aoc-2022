import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--input", help="Input File name")

args = parser.parse_args()

fileName = args.input

files = open(fileName, 'r')

lines = files.readlines()

head_x = 0
head_y = 0

tail_x = 0
tail_y = 0

tail = [[0,0] for _ in range(9)]

visited = set()
visited.add('0,0')


def is_touching():
    # Overlapping condition
    if head_x == tail_x and head_y == tail_y:
        return True
    # Same row condition
    if head_x == tail_x and abs(head_y - tail_y) <= 1:
        return True
    # Same column condition
    if head_y == tail_y and abs(head_x - tail_x) <= 1:
        return True
    # Diagonal condition
    if abs(head_x - tail_x) == 1 and abs(head_y - tail_y) == 1:
        return True
    return False


def move_tail():
    global head_x, head_y, tail_x, tail_y
    # same row condition
    if head_y == tail_y:
        if head_x > tail_x:
            tail_x += 1
        else:
            tail_x -= 1
    # same column condition
    elif head_x == tail_x:
        if head_y > tail_y:
            tail_y += 1
        else:
            tail_y -= 1
    # Diagonal condition
    else:
        if head_x > tail_x:
            tail_x += 1
        else:
            tail_x -= 1
        if head_y > tail_y:
            tail_y += 1
        else:
            tail_y -= 1

    visited.add(f"{tail_x},{tail_y}")
    # print(f"Moved Tail to {tail_x},{tail_y}")

def move_head(movement):
    global head_x, head_y
    [direction, amount] = movement.split(" ")

    for _ in range(int(amount)):
        if direction == "R":
            head_x += 1
        if direction == "U":
            head_y += 1
        if direction == "D":
            head_y -= 1
        if direction == "L":
            head_x -= 1

        # print(f"New Head Position {head_x}, {head_y}")
        if not is_touching():
            move_tail()


for index, value in enumerate(lines):
    movement = value.strip()
    move_head(movement)

print(len(visited))
