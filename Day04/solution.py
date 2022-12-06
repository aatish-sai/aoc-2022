import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--input", help="Input File name")

args = parser.parse_args()

fileName = args.input

files = open(fileName, 'r')

lines = files.readlines()

count = 0
partial = 0

for index, value in enumerate(lines):
    pairs = value.strip().split(",")

    [first_low, first_high] = [int(s) for s in pairs[0].strip().split("-")]
    [second_low, second_high] = [int(s) for s in pairs[1].strip().split("-")]

    if first_high < second_low and first_low < second_low:
        continue

    if second_high < first_low and second_low < first_low:
        continue

    partial += 1

    if first_low >= second_low and first_high <= second_high:
        count += 1
        continue

    if second_low >= first_low and second_high <= first_high:
        count += 1
        continue

print(count)
print(partial)
