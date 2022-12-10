import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--input", help="Input File name")

args = parser.parse_args()

fileName = args.input

files = open(fileName, 'r')

lines = files.readlines()

signals = [1]

for index, value in enumerate(lines):
    line = value.strip().split(" ")

    if line[0] == "addx":
        signals.extend([0,int(line[1])])
    else:
        signals.extend([0])

print(len(signals))
strength = 0
strength += sum(signals[:20]) * 20
strength += sum(signals[:60]) * 60
strength += sum(signals[:100]) * 100
strength += sum(signals[:140]) * 140
strength += sum(signals[:180]) * 180
strength += sum(signals[:220]) * 220


print(strength)


for i in range(1,241):
    if i % 40 == 0:
        pos = 40
    else:
        pos = i % 40
    if pos in [sum(signals[:i]),sum(signals[:i])+1,sum(signals[:i])+2]:
        print_char = "#"
    else:
        print_char = "."
    if i % 40 == 0:
        print(f"{print_char}")
    else:
        print(f"{print_char}", end="")
