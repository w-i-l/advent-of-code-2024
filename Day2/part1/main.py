with open('input.txt', 'r') as f:
    data = f.readlines()
    data = list(map(lambda x: x.strip().split(" "), data))
    data = list(map(lambda x: list(map(int, x)), data))

result = 0
for line in data:
    pattern = "up" if line[0] < line[1] else "down"

    for i in range(1, len(line)):
        if pattern == "up":
            if line[i] < line[i-1] or line[i] - line[i-1] > 3 or line[i] == line[i-1]:
                break
        elif pattern == "down":
            if line[i] > line[i-1] or line[i-1] - line[i] > 3 or line[i-1] == line[i]:
                break
    else:
        result += 1

print(result)