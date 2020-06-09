import time
login = ""
password = "halo"
while login != password :
    login = input ('Password:')
    if login == password: 
        a=0
        c=3
    while a<c :
        for x in range (0,4):
            time.sleep (0.2)
            b='Loading'+ '.' * x
            print (b)
        a+= 1
print ("========================")
print ("DAFTAR KRIMINAL")
print ("========================")
criminal1 = {
    'Name': 'Dave',
    'Age' :'45',
    'Crime':'Nyolong'
    }
for key, value in criminal1.items():
    print (f'{key}: {value}')

criminal2 = {
    'Name': 'Hamsa',
    'Age' :'5',
    'Crime':'Membunuh'
    }
for key, value in criminal2.items():
    print (f'{key}:{value}')

    criminal3 = {
    'Name': 'Marcel',
    'Age' :'30',
    'Crime':'Mencuri'
    }
for key, value in criminal3.items():
    print (f'{key}:{value}')
    break
else:
    print ('Wrong')



