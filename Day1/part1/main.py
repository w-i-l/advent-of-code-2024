with open('input.txt', 'r') as f:
    data = f.readlines()
    data = list(map(lambda x: x.strip().split("   "), data))
    data = list(map(lambda x: list(map(int, x)), data))

result = 0

left = [x[0] for x in data]
left.sort()
right = [x[1] for x in data]
right.sort()

for a, b in zip(left, right):
    result += abs(a - b)

print(result)