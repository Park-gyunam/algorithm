train_p = []
pe = 0

for _ in range(4):
    leave, enter = map(int, input().split())
    pe += enter
    pe -= leave
    train_p.append(pe)
print(max(train_p))