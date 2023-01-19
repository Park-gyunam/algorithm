alpabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
sec = 0

for element in alpabet:
    #print(element) => 리스트에 있는 요소들을 꺼냄
    for i in element:
        #print(i) => 각 요소들을 한 글자씩 분리
        for j in word: # => 입력받는 문자열 한 글자씩 분리
            if i == j:
                sec += alpabet.index(element)+3 # => ABC를 걸려면 3초가 걸림, 인덱스 위치는 0이므로 +3
print(sec)