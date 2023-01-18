word = list(input())
alpa = 'abcdefghijklmnopqrstuvwxyz'

for i in alpa:
    if i in word:
        print(word.index(i), end=' ')
    else:
        print(-1, end=' ')