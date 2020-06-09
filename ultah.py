from datetime import date
play = True
while play :
    pilih = input('apakah ingin menggunakan calculator umur? (y/n) :')
    if pilih == 'y' :
        today= date.today()
        tgl = int(input('masukkan tanggal lahir:'))
        bln = int(input('masukkan bulan lahir:'))
        thn = int(input('masukkan tahun lahir:'))
        print (f'tanggal lahir kamu: {tgl}-{bln}-{thn}')
        umur = int (today.year - thn)
        hari = int (today.day - tgl)
        bulan = int (today.month - bln)
        print (f'umur kamu {umur} tahun kurang {abs(bulan)} bulan , kurang{abs(hari)} hari')
    elif pilih == 'n': 
        play = False
    else :
        print ('masukkan y/n saja')
