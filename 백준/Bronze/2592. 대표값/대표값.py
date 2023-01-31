n = 10
avg = []
for _ in range(n):
    number = int(input())
    avg.append(number)
print(sum(avg)//10)

temp = list(set(avg)) # -> avg 리스트의 중복값 제거 [40, 10, 50, 20, 60, 30]
m_number = []
for i in range(len(temp)):
    m_number.append(avg.count(temp[i])) # -> temp 각 인덱스의 값을 카운트
print(temp[m_number.index(max(m_number))])

