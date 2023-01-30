surface = [[0] * 100 for _ in range(101)]
count = 0

for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            if surface[j][k] == 0:
                surface[j][k] = 1
                count += 1
print(count)