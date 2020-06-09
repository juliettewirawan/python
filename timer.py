import time
print ('COUNTDOWN')
print('======')
fill= int (input('Insert time (in chosen until):'))
start= (input('Type "Yes" to start:'))
if start.lower().strip() == 'yes':
  count=fill
  while count >0 :
    print (count)
    count = count - 1
    time.sleep (1)
    
  print ("Okay Thanks!")