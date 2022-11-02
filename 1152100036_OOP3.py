'''
Abthal Fajar Aufar
1152100036
Informatika

'''





class Hero:
    def __init__ (self, nama, diamond, bp, tiket):

        self.__nama = nama
        self.__diamond = int(diamond)
        self.__bp = int(bp)
        self.__tiket = int(tiket)
        Hero.jumlahHero +=1

    def get_hero_desc(self):
        return "Tipe {} \n\tNama Hero : {} \n\tDiamond : {} \n\tBp : {} \n\tTiket : {}  " .f(self.__jenis,self.__nama,self.__diamond,self.__bp,self.__tiket)
    

class Magic(Hero):
    def __init__(self, nama, diamond, bp, tiket, jenis, atribut):
     super().__init__(self, nama, diamond, bp, tiket)
     self.__jenis = jenis
     self.__atribut = int(atribut)

class Physical(Hero):
    def __init__(self, nama, diamond, bp, tiket, jenis, atribut):
     super().__init__(self, nama, diamond, bp, tiket)
     self.__jenis = jenis
     self.__atribut = int(atribut)

class Support(Hero):
    def __init__(self, nama, diamond, bp, tiket, jenis, atribut):
     super().__init__(self, nama, diamond, bp, tiket)
     self.__jenis = jenis
     self.__atribut = int(atribut)

class Role:
    def __init__ (self, nama, kh):

        self.nama = nama
        self.kh = kh
    
    def list_hero():
        pass
    def add_hero():
        input(Hero.get_hero_desc()).split("")
    def search_hero():
         Hero.get_hero_desc()

class Jungler(Role):
    pass

class Offlaner(Role):
    pass

class Midlanner(Role):
    pass

class Roeamer(Role):
    pass

class Akun:
    def add_role():
        pass
    def add_hero():
        input(Hero.get_hero_desc()).split("")
    def search_hero():
        Hero.get_hero_desc()

def main():
    print("Selamat datang di Mobile Legends Bang Bang")
    print("Silahkan masukan perintah!")
    while (True):
        print("Perintah anda :")
        perintah = input()
        if(perintah == "Exit"):
            break

        elif(perintah == "LIST"):
            pass

        elif(perintah == "Search"):
            
            if (perintah == False):
                print(f'Hero dengan nama {Hero.self.__nama} Tidak ditemukan')
                break

            elif (perintah == True):
                print(f"Hero dengan nama  {Hero.self.__nama} ditemukan")
                Akun.search_hero()
        
        elif(perintah == "Add Hero"):
            Akun.add_hero()
        
        elif(perintah == "Add Role"):
            Akun.add_hero()

        else:
            False

                

main()    