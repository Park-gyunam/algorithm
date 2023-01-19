A = int(input())
B = int(input())
C = int(input())

result = list(str(A*B*C))
#print(result)
for i in range(10):
    print(result.count(str(i)))