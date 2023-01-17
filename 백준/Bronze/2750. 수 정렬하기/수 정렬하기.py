N = int(input())
num_list = []
for i in range(N):
    num_list.append(int(input()))
    #print(num_list)
num_list1 = sorted(num_list)
for i in range(len(num_list)):
    print(num_list1[i])