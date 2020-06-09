print ('PEMBAYARAN')
print ('============')

def payment(hours, rate): 
    if hours > 40:
        return str (hours*rate*1.5)
    else:
        return str (hours*rate)

hoursinp = int(input('Enter hours:'))
rateinp = int(input('Enter rate:'))
results = payment (hoursinp, rateinp)
print ('Pay:'+ results)
