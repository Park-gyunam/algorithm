X = int(input())
N = int(input())
total = 0

for i in range(1, N+1):
    price, count = map(int, input().split())
    total += price * count
if total == X:
    print('Yes')
else:
    print('No')