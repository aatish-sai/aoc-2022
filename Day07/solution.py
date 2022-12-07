import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--input", help="Input File name")

args = parser.parse_args()

fileName = args.input

files = open(fileName, 'r')

lines = files.readlines()

files = {}
directory = {}
cwd = ""


def process_command(cmd):
    global cwd
    if cmd.split(" ")[1] == "cd":
        tmp = cmd.split(" ")[2].strip()
        if tmp == "..":
            cd = cwd.rsplit("-", 1)[0]
        else:
            cd = "/" if tmp == "/" else "-".join([cwd, tmp])
        cwd = cd
    return


def process_result(value):
    global cwd
    if not value.startswith("dir"):
        fileName = value.split(" ")[1].strip()
        size = int(value.split(" ")[0])
        files["-".join([cwd, fileName])] = size


for index, value in enumerate(lines):
    if value.startswith('$'):
        process_command(value)
    else:
        process_result(value)

for k, v in files.items():
    tmp_dir = k
    while True:
        dir = tmp_dir.rsplit("-", 1)[0]

        if dir in directory:
            directory[dir] += v
        else:
            directory[dir] = v

        if dir == "/":
            break
        tmp_dir = dir
result = 0
result2 = None
min = 99_999_999
required = 30_000_000 - 70_000_000 + directory['/']
print(f"required {required}")
for k, v in directory.items():
    if v <= 1_00_000:
        result += v
    if v >= required and v < min:
        result2 = k
        min = v
print(result)
print(directory[result2])
print(result2)
