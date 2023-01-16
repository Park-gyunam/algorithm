N = int(input())
sum = 0
result = 0
P = list(map(int, input().split()))

for i in range(N):
    if P[i] == 1:
        sum += 1
        result += sum
    else:
        sum = 0
print(result)