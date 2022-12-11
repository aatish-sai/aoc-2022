from typing import Dict, List

m0: List[int] = [99, 67, 92, 61, 83, 64, 98]
m1: List[int] = [78, 74, 88, 89, 50]
m2: List[int] = [98, 91]
m3: List[int] = [59, 72, 94, 91, 79, 88, 94, 51]
m4: List[int] = [95, 72, 78]
m5: List[int] = [76]
m6: List[int] = [69, 60, 53, 89, 71, 88]
m7: List[int] = [72, 54, 63, 80]

# online tool to caluclate the LCM of the test clause
# part 1 divide // by 3
# part 2 module % by lcm
lcm = 9_699_690 # part 2

def operation(index, value):
    if index == 0:
        operation = value * 17
        operation = operation % lcm
        if operation % 3 == 0:
            m4.append(operation)
        else:
            m2.append(operation)
    if index == 1:
        operation = value * 11
        operation = operation % lcm
        if operation % 5 == 0:
            m3.append(operation)
        else:
            m5.append(operation)
    if index == 2:
        operation = value + 4
        operation = operation % lcm
        # operation = operation // 3
        if operation % 2 == 0:
            m6.append(operation)
        else:
            m4.append(operation)
    if index == 3:
        operation = value * value
        operation = operation % lcm
        # operation = operation // 3
        if operation % 13 == 0:
            m0.append(operation)
        else:
            m5.append(operation)
    if index == 4:
        operation = value + 7
        operation = operation % lcm
        # operation = operation // 3
        if operation % 11 == 0:
            m7.append(operation)
        else:
            m6.append(operation)
    if index == 5:
        operation = value + 8
        operation = operation % lcm
        # operation = operation // 3
        if operation % 17 == 0:
            m0.append(operation)
        else:
            m2.append(operation)
    if index == 6:
        operation = value + 5
        operation = operation % lcm
        # operation = operation // 3
        if operation % 19 == 0:
            m7.append(operation)
        else:
            m1.append(operation)
    if index == 7:
        operation = value + 3
        operation = operation % lcm
        # operation = operation // 3
        if operation % 7 == 0:
            m1.append(operation)
        else:
            m3.append(operation)


interaction = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
for i in range(10_000):
    for index in range(8):
        if index == 0:
            interaction[index] += len(m0)
            for x in m0:
                operation(index, int(x))
            m0 = []
        if index == 1:
            interaction[index] += len(m1)
            for x in m1:
                operation(index, int(x))
            m1 = []
        if index == 2:
            interaction[index] += len(m2)
            for x in m2:
                operation(index, int(x))
            m2 = []
        if index == 3:
            interaction[index] += len(m3)
            for x in m3:
                operation(index, int(x))
            m3 = []
        if index == 4:
            interaction[index] += len(m4)
            for x in m4:
                operation(index, int(x))
            m4 = []
        if index == 5:
            interaction[index] += len(m5)
            for x in m5:
                operation(index, int(x))
            m5 = []
        if index == 6:
            interaction[index] += len(m6)
            for x in m6:
                operation(index, int(x))
            m6 = []
        if index == 7:
            interaction[index] += len(m7)
            for x in m7:
                operation(index, int(x))
            m7 = []

x = sorted(list(interaction.values()), reverse=True)

print(x[0] * x[1])
