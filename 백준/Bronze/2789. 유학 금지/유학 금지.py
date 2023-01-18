except_word = ['C','A','M','B','R','I','D','G','E']
result = ''
word = input()

for i in word:
    if i not in except_word:
        result += i
print(result)