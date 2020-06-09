import random

suit = ["batu", "gunting", "kertas"]
random_main = random.choice (suit)
print (str(random_main))

score_player1 = 0 
score_player2 = 0 
while True: 
    main = input ('Mau main gaa? batu/gunting/kertas:')
    if main == 'batu' and random_main == 'kertas':
        print ('kalah')
        score_player2 += 1
        print (f'score: {score_player1}-{score_player2}')
    elif main == 'batu' and random_main == 'gunting':
        print ('menang')
        score_player1 += 1
        print (f'score: {score_player1}-{score_player2}')
    elif main == 'gunting' and random_main == 'kertas':
        print ('kalah')
        score_player2 += 1
        print (f'score: {score_player1}-{score_player2}')
    elif main == 'gunting' and random_main == 'batu':
        print ('kalah')  
        score_player2 += 1 
        print (f'score: {score_player1}-{score_player2}')
    elif main == 'kertas' and random_main == 'gunting':
        print ('kalah')
        score_player2 += 1
        print (f'score: {score_player1}-{score_player2}')
    elif main == 'kertas' and random_main == 'batu':
        print ('menang')
        score_player1 += 1
        print (f'score: {score_player1}-{score_player2}')
    else:
        print ('Seri kak')
        print (f'score: {score_player1}-{score_player2}')
   