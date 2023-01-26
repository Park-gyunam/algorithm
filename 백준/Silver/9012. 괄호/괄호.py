t = int(input())

for i in range(t):
    vps = input()
    vps_list = list(vps)
    compare = 0
    for j in vps_list:
        if j == '(':
            compare += 1
        elif j == ')':
            compare -= 1
        if compare < 0:
            print('NO')
            break
    if compare > 0:
        print('NO')
    elif compare == 0:
        print('YES')


