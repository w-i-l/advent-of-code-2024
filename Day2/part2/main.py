'''
Problem here
https://adventofcode.com/2024/day/2
'''

with open('input.txt', 'r') as f:
    data = f.readlines()
    data = list(map(lambda x: x.strip().split(" "), data))
    data = list(map(lambda x: list(map(int, x)), data))

result = 0
for line in data:
    pattern = "up" if line[0] < line[1] else "down"
    has_tollerate = False

    for i in range(1, len(line)):
        if pattern == "up":
            if line[i] < line[i-1] or line[i] - line[i-1] > 3 or line[i] == line[i-1]:
                if not has_tollerate:
                    has_tollerate = True
                else:
                    break

        elif pattern == "down":
            if line[i] > line[i-1] or line[i-1] - line[i] > 3 or line[i-1] == line[i]:
                if not has_tollerate:
                    has_tollerate = True
                else:
                    break
    else:
        result += 1

print(result)