N = int(input())

while True:
    result = True
    for i in str(N):
        if i != '4' and i != '7':
            result = False
            N -= 1
    if result:
        print(N)
        break