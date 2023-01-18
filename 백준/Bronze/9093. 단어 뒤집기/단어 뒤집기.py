t_case = int(input())

for i in range(t_case):
    sentence = list(input().split())
    for j in sentence:
        print(j[::-1], end=' ')