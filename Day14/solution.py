import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--input", help="Input File name")

args = parser.parse_args()

fileName = args.input

files = open(fileName, 'r')

lines = files.readlines()

cave = set()
ground = 0


class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self) -> int:
        return int(f"{self.x}0000{self.y}")

    def __repr__(self):
        return f"X:{self.x}, Y:{self.y}"


def getNextPosition(pos: Coordinate, part2:bool = False) -> Coordinate:
    
    if part2:
        if pos.y == ground + 1:
            return pos
    if Coordinate(pos.x, pos.y + 1) not in cave:
        return Coordinate(pos.x, pos.y + 1)
    elif Coordinate(pos.x - 1, pos.y + 1) not in cave:
        return Coordinate(pos.x - 1, pos.y + 1)
    elif Coordinate(pos.x + 1, pos.y + 1) not in cave:
        return Coordinate(pos.x + 1, pos.y + 1)
    else:
        return pos


for index, value in enumerate(lines):
    line = value.strip()

    scans = line.split(" -> ")

    for i in range(len(scans)):
        [x, y] = [int(x) for x in scans[i].split(",")]

        if y > ground:
            ground = y

        if i == 0:
            cave.add(Coordinate(x, y))
            continue
        else:
            [prev_x, prev_y] = [int(x) for x in scans[i - 1].split(",")]

            if prev_x == x:
                for n in range(min(prev_y, y), max(prev_y, y) + 1):
                    cave.add(Coordinate(x, n))
            if prev_y == y:
                for n in range(min(prev_x, x), max(prev_x, x) + 1):
                    cave.add(Coordinate(n, y))

def solvePart1():
    inAbyss = False
    count = 0
    while not inAbyss:
        print(f"Sand count {count + 1}")
        initialPos = Coordinate(500,0)
        stable = False
        while not stable:
            nextPos = getNextPosition(initialPos)
            if nextPos == initialPos:
                print("Sand now stable")
                print(f"Sand fell at {nextPos}")
                count += 1
                cave.add(nextPos)
                stable = True
            if nextPos.y > ground:
                print("Fall in Abyss")
                inAbyss = True
                break
            initialPos = nextPos
    print(count)

def solvePart2():
    inAbyss = False
    count = 0
    while not inAbyss:
        print(f"Sand count {count + 1}")
        initialPos = Coordinate(500,0)
        stable = False
        while not stable:
            nextPos = getNextPosition(initialPos, True)
            if nextPos == initialPos:
                print("Sand now stable")
                print(f"Sand fell at {nextPos}")
                count += 1
                cave.add(nextPos)
                stable = True
            if nextPos == Coordinate(500,0):
                inAbyss = True
                break
            initialPos = nextPos
    print(count)

if __name__ == "__main__":
    # solvePart1()
    solvePart2()
