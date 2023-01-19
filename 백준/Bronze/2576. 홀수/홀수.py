odd_num = []

for i in range(7):
    number = int(input())
    if number % 2 == 1:
        odd_num.append(number)
if odd_num:
    print(sum(odd_num))
    print(min(odd_num))
else:
    print(-1)