message = input()

emo_happy = message.count(':-)')
emo_sad = message.count(':-(')

if emo_happy == 0 and emo_sad == 0:
    print('none')
elif emo_happy == emo_sad:
    print('unsure')
elif emo_happy > emo_sad:
    print('happy')
elif emo_happy < emo_sad:
    print('sad')