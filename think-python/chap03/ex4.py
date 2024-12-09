def bottle_verse(num):
    print(f'{num} bottles of beer on the wall\n{num} bottles of beer\nTake one down, pass it around\n{num-1} bottles of beer on the wall')

bottle_verse(99)

for i in range(99, 0, -1):
    bottle_verse(i)
    print()