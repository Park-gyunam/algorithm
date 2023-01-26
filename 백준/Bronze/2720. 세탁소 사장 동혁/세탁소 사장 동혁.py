for t in range(int(input())):
    cent = int(input())
    cent_list = [25, 10, 5, 1]
    exchange = []
    for i in cent_list:
        exchange.append(cent//i)
        cent = cent % i
    print(*exchange)