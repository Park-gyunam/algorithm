score_sum = 0
for i in range(5):
    a = int(input())
    if a < 40:
        score_sum += 40
    else:
        score_sum += a
print(int(score_sum/5))