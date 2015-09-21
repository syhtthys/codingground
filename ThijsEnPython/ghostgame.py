# Ghost Game

from random import randint
print ('Ghost Game')
feeling_brave = True
score = 0
while feeling_brave:
    ghost_door = randint (1,3)
    print ('drie deuren zijn zichtbaar...')
    print ('Een geest zit achter Ã©Ã©n deur.')
    print ('Welke deur maak je open?')
   # print ('(het is deur ',ghost_door)
    door = input ('1,2 of 3? ')
    door_num = int (door)
    if door_num == ghost_door:
        print ('GEEST!!!')
        feeling_brave = False
    else:
        print('Geen geest')
        print('Je betreedt de volgende kamer')
        score = score + 1
print ('Ren keihard weg Boehoehoehoehoehoehoe')
print ('Game over! Jouw score ', score)
