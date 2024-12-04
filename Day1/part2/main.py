with open('input.txt', 'r') as f:
    data = f.readlines()
    data = list(map(lambda x: x.strip().split("   "), data))
    data = list(map(lambda x: list(map(int, x)), data))

left = [x[0] for x in data]
right = [x[1] for x in data]
hasH_table = {}

for elem in right:
    if elem in hasH_table:
        hasH_table[elem] += 1
    else:
        hasH_table[elem] = 1

result = 0
for elem in left:
    try:
        result += elem * hasH_table[elem]
    except KeyError:
        pass

print(result)
