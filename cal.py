print ('--------------')
print ('CALCULATOR')
print ('--------------')
angka1= int(input('Masukkan angka pertama:'))
print(f'Angka pertama adalah:{angka1}')
angka2= int(input('Masukkan angka kedua:'))
print(f'Angka kedua adalah:{angka2}')
print ('1= tambah')
print ('2= kurang')
print ('3= kali')
print ('4= bagi')
operasi= int(input('Masukkan operasi hitung:'))
tambah=angka1+angka2
kurang=angka1-angka2
kali=angka1*angka2
bagi=angka1/angka2
if operasi == 1:
    print(f'Hasil: {tambah}')
elif operasi == 2:
    print(f'Hasil: {kurang}')
elif operasi == 3:
    print(f'Hasil: {kali}')
elif operasi == 4:
    print(f'Hasil: {bagi}')
else:
    print ('invalid operator')

