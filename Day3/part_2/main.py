import re

'''
Problem:
https://adventofcode.com/2024/day/3
'''

with open('input.txt') as f:
    data = "".join(f.readlines())

    result = 0

    mults = []
    conditions = []

    # finding all valid multiplications
    regex = r'mul\((\d){1,3},(\d){1,3}\)'
    matches = re.finditer(regex, data, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        found_match = match.group()
        position = match.start()
        a, b = map(int, found_match[4:-1].split(","))
        mults.append((position, (a, b)))

    # finding all valid conditions
    regex = r"do\(\)|don't\(\)"
    matches = re.finditer(regex, data, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        found_match = match.group()
        condition = True if found_match == "do()" else False
        position = match.start()
        conditions.append((position, condition))

    # overlaping the two lists for the correct order
    index_mult = 0
    index_condition = 0
    overlapped = []

    while index_mult < len(mults) and index_condition < len(conditions):
        cond_position = conditions[index_condition][0]
        mult_position = mults[index_mult][0]

        if mult_position < cond_position:
            overlapped.append(mults[index_mult])
            index_mult += 1
        else:
            overlapped.append(conditions[index_condition])
            index_condition += 1

    if index_mult < len(mults):
        overlapped.extend(mults[index_mult:])
    elif index_condition < len(conditions):
        overlapped.extend(conditions[index_condition:])

    # calculating the result
    can_mult = True
    for elem in overlapped:
        if type(elem[1]) == tuple:
            if can_mult:
                result += elem[1][0] * elem[1][1]
        else:
            can_mult = elem[1]

    print(result)
