import argparse
import re

parser = argparse.ArgumentParser()

parser.add_argument("--input", help="Input File name")

args = parser.parse_args()

fileName = args.input

files = open(fileName, 'r')

lines = files.readlines()

stack = {}

reading_input = True


def process_change_new(line):
    task = [int(s) for s in re.findall(r"\d+", line)]

    move_from = task[1]
    move_to = task[2]

    move = stack[move_from][:task[0]]

    del stack[move_from][:task[0]]

    if not stack[move_from]:
        stack[move_from] = []
    stack[move_to] = move + stack[move_to]


def process_change(line):
    task = [int(s) for s in re.findall(r"\d+", line)]

    move_from = task[1]
    move_to = task[2]

    move = stack[move_from][:task[0]]

    del stack[move_from][:task[0]]

    if not stack[move_from]:
        stack[move_from] = []
    stack[move_to] = move[::-1] + stack[move_to]


def get_result():
    result = ['a'] * len(stack)

    for i in stack:
        result[i - 1] = stack[i][0]
    return "".join(result)


for index, value in enumerate(lines):
    if value.strip() == "":
        reading_input = False
        print(stack)
        continue

    if reading_input:
        for idx, v in enumerate(value):
            if v.isalpha():
                stack_index = idx // 4 + 1
                if stack_index in stack:
                    stack[stack_index].append(v)
                else:
                    stack[stack_index] = [v]
    else:
        process_change_new(value)

result = get_result()
print(result)
