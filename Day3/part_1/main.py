import re

'''
Problem:
https://adventofcode.com/2024/day/3
'''

with open('input.txt') as f:
    data = "".join(f.readlines())

    result = 0

    regex = r'mul\((\d){1,3},(\d){1,3}\)'
    matches = re.finditer(regex, data, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        match = match.group()
        a, b = map(int, match[4:-1].split(","))
        result += a * b

    print(result)
