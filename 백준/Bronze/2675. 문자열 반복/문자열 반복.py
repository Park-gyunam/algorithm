T_case = int(input())

for i in range(T_case):
    R, S = input().split()
    result = ''
    for i in S:
        result += int(R) * i
    print(result)