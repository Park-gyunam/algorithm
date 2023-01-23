n = int(input())
pe = {}

for i in range(n):
    person, log = input().split()
    if log == 'enter':
        pe[person] = 'enter'
    else:
        if pe[person]:
            del pe[person]
for j in sorted(pe, reverse=True):
    print(j)