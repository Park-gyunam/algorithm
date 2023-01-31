words = []
for i in range(5):
    word = input()
    words.append(word)

for j in range(15):
    for i in range(5):
        if j < len(words[i]):
            print(words[i][j], end='')