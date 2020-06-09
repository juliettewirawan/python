class Luas : 
    def __init__ (self,panjang,lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def dikali (self):
        return f'Jadi luas Persegi Panjang adalah: {self.panjang*self.lebar}'


luas1 = Luas(12, 10)
print (luas1.dikali())
