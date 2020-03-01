# Class
class Manusia():

    def __init__(self, iNama, iGender, iUmur):
        self.Nama = iNama
        self.Gender = iGender
        self.Umur = iUmur

    def Belajar(self, pKondisi):
        print(self.Nama, 'sedang belajar', pKondisi)

    def Makan(self, pLauk, pTempat, pKondisi):
        print(self.Nama, 'sedang makan', pTempat, pKondisi)

    def Identitas(self):
        print(self.Nama, 'ber jenis kelamin', self.Gender, 'dengan usia', self.Umur, 'tahun')


# Main Program
M1 = Manusia("Rizky Khapidsyah", "Laki-Laki", "28")

M1.Belajar("Saat mati listrik")
M1.Makan("Ikan", "di rumah", "dengan keadaan listrik padam")
M1.Identitas()
