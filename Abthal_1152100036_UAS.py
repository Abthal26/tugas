'''
Abthal Fajar Aufar
1152100036
Informatika

'''

class Penjual:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal
    
    def jual_barang(self):
        print(f'{self.nama} adalah seorang pedagang yang berasal dari {self.asal}')
    

    

class Pembeli:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal
   
    def beli_barang(self):
        print(f'{self.nama} adalah seorang pembeli yang berasal dari {self.asal}')

class Barang(Penjual,Pembeli):
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga =int(harga)
    
    def info(self):
        print(f'Barang tersebut adalah {self.nama} dengan harga {self.harga}')
    

    

def main():


    print("Suatu hari di sebuah pasar di daerah Jakarta")
    tono = Penjual(nama = "Tono",asal = "Jakarta")
    tono.jual_barang()
    toni = Pembeli(nama = "Toni",asal = "Bandung")
    toni.beli_barang()
    sepeda = Barang(nama = "Sepeda",harga=2000000)
    sepeda.info()
    


main()