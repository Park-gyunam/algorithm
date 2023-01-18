score = int(input())
test_s = score

if test_s >= 90:
    print('A')
elif test_s >= 80 and test_s <= 89:
    print('B')
elif test_s >= 70 and test_s <= 79:
    print('C')
elif test_s >= 60 and test_s <= 69:
    print('D')
else:
    print('F')