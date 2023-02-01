n, m = map(int, input().split())
choice_num = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if choice_num[i] + choice_num[j] + choice_num[k] > m:
                continue
            else:
                result = max(result, choice_num[i] + choice_num[j] + choice_num[k])
print(result)