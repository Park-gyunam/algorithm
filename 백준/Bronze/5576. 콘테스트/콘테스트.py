w = []
k = []
for _ in range(10):
    w_score = int(input())
    w.append(w_score)
    
for _ in range(10):
    k_score = int(input())
    k.append(k_score)

w.sort(reverse=True)
k.sort(reverse=True)

w_score_sum = 0
k_score_sum = 0

for i in range(3):
    w_score_sum += w[i]
    k_score_sum += k[i]
print(w_score_sum, k_score_sum)
