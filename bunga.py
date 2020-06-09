Flowers =[]
class Flower: 
    def __init__ (self,bunga,kelopak,harga):
        self.bunga = bunga
        self.kelopak = kelopak
        self.harga = harga
    
    def cetak (self):
        return f'Bunga {self.bunga}, kelopak {self.kelopak} , harga {self.harga} '

while True: 
    mau = input ('ingin masukkan data? (y/n): ' )
    if mau == 'y': 
        nama= str(input('nama bunga:'))
        petals=int(input('jumlah kelopak:'))
        total=float(input('harga:'))

        flowerr = Flower(nama,petals,total)
        Flowers.append(flowerr)
    else: 
        break
for x in Flowers:
    print (x.cetak())

