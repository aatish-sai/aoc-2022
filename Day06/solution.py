import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--input", help="Input File name")

args = parser.parse_args()

fileName = args.input

files = open(fileName, 'r')

lines = files.readlines()
result = 0
result2 = 0 

def get_message_position(line):
    marker = []
    for idx, c in enumerate(line):
        if len(marker) >= 14:
            marker.pop()
        marker.insert(0,c)
        if len(set(marker)) >= 14:
            print(marker)
            return idx + 1

def get_marker_position(line):
    marker = []
    for idx, c in enumerate(line):
        if len(marker) >= 4:
            marker.pop()
        marker.insert(0,c)
        if len(set(marker)) >= 4:
            print(marker)
            return idx + 1

for index, value in enumerate(lines):
    result = get_marker_position(value)
    result2 = get_message_position(value)

print(result)
print(result2)
