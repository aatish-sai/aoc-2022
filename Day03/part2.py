import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--input", help="Input File name")

args = parser.parse_args()

fileName = args.input

files = open(fileName, 'r')

lines = files.readlines()
input_length = len(lines)
result = 0
x = set()
for index in range(0, input_length, 3):

    common = set(lines[index].strip()).intersection(
        set(lines[index + 1].strip()), set(lines[index + 2].strip()))
    print(common)
    for char in common:
        if char.isupper():
            pval = ord(char) - 38
        else:
            pval = ord(char) - 96
        result += pval
print(result)
