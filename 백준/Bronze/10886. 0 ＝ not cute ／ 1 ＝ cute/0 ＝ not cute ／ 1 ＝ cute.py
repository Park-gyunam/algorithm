N = int(input())
cute = 0
no_cute = 0
for i in range(1, N+1):
    a = int(input())
    if a == 0:
        no_cute += 1
    else:
        cute += 1
if no_cute > cute:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')