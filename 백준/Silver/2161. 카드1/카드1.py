n = int(input())
num_list = list(range(1, n+1))
discard_cards = []

while len(num_list) > 1:
    discard_cards.append(num_list.pop(0))
    num_list.append(num_list.pop(0))

print(*discard_cards, num_list[0])