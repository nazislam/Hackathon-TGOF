f = open('moveCard.txt', 'r')

f1 = f.readlines()
for x in f1:
    h = x.split('|')
    print(h, end='')
    print()
print('----')
