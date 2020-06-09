from random import randint

print ('')
print ('==================================')
print ('     Yuk main tebak tebakan       ')
print ('==================================')
print ('')


def generator():
    return randint (1,10)

def ran_guess():
    random_number = generator()
    guess_left= 8
    flag = 0

    while guess_left > 0:
        try: 
            guess= int(input('pilih angka untuk menebak:'))
            if guess == random_number:
           
                return True
            guess_left -= 1
        except:
            print ('WHOOPS salah!')

    return False

if __name__ =='__main__':
    if ran_guess() is True :
        print ("yayy benar!")
    else: 
        print ("coba lagii yuk!")
