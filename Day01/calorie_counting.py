import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--input", help="Input file Name")

args = parser.parse_args()

input_file = args.input
file = open(input_file, 'r')
lines = file.readlines()
elvis = []
tmp = 0
max1 = 0
max2 = 0
max3 = 0
for index, line in enumerate(lines):
    if line == '\n' or index == len(lines) - 1:
        elvis.append(tmp)
        if tmp >= max1:
            max3 = max2
            max2 = max1
            max1 = tmp
        elif tmp >= max2:
            max3 = max2
            max2 = tmp
        elif tmp >= max3:
            max3 = tmp
        tmp = 0
    else:
        tmp += int(line)

print(max1 + max2 + max3)
