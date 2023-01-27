start = input()
problem = 0

while True:
    end = input()
    if end == '고무오리 디버깅 끝':
        break
    else:
        if end == '문제':
            problem += 1
        elif end == '고무오리':
            if problem == 0:
                problem += 2
            else:
                problem -= 1
if problem == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')