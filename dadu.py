
import random
play = True
while play :
    pilih = input ('wanna roll? (y/n) : ')
    if pilih == 'y' : 
        print ('you have rolled: ' , random.randint (1,6))
        continue
    else: 
        play = False

