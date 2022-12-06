import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--input", help="Input File name")

args = parser.parse_args()

fileName = args.input

files = open(fileName, 'r')

lines = files.readlines()
result = 0
for index, value in enumerate(lines):
    length = len(value)
    x = set()

    for idx, char in enumerate(value):
        if idx >= length / 2 - 1:
            break

        if char in value[int(length / 2):length + 1] and char not in x:
            x.add(char)
            if char.isupper():
                pval = ord(char) - 38
            else:
                pval = ord(char) - 96
            result += pval
print(result)
