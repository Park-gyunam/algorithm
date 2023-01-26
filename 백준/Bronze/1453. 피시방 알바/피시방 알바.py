n = int(input())
seat_n = list(map(int, input().split()))
reject_cnt = 0
seat = []

for i in range(n):
    if seat_n[i] in seat:
        reject_cnt += 1
    else:
        seat.append(seat_n[i])
print(reject_cnt)