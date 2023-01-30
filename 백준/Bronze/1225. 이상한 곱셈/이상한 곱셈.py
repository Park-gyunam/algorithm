a, b = input().split()
c = 0
d = 0
for i in range(len(a)):
    c += int(a[i])
for j in range(len(b)):
    d += int(b[j])
print(c*d)