ogrenciler = [""]

# Ogrenci Ekleme Fonksiyonu
def ogrenciEkle():
    adSoyad = input("Lutfen eklemek istediginiz ogrencinin adini ve soyadini giriniz: ")
    ogrenciler.append(adSoyad)
    print("{} basariyla eklendi!".format(adSoyad))

# Ogrenci Silme Fonksiyonu
def ogrenciSil():
    adSoyad = input("Lutfen silmek istediginiz ogrencinin adini ve soyadini giriniz: ")
    ogrenciler.remove(adSoyad)
    print("{} basariyla silindi!".format(adSoyad))

# Birden Fazla Ogrenci Silme Fonksiyonu
def ogrencilerEkle():
    while True:
        adSoyad = input("Ongrenci adi ve soyadi (cikmak icin 'q' harfine basiniz): ")
        if(adSoyad == "q"):
            break
        ogrenciler.append(adSoyad)
        print("{} basariyla eklendi!".format(adSoyad))

# Ogrenci Listeleme Fonksiyonu
def ogrencilerListe():
    if(len(ogrenciler) == 0):
        print("Ogrenci kaydi bulunmamaktadir.")
    else:
        for i in ogrenciler:
            print(i)

# Ogrenci Numarasi Sorgulama Fonksiyonu
def ogrenciNumarasi():
    adSoyad = input("Lutfen ogrencinin adini ve soyadini giriniz: ")
    if (adSoyad in ogrenciler):
        numara = ogrenciler.index(adSoyad)
        print("{} adiyla kayitli ogrencinin numarasi : {}".format(adSoyad,numara))
    else:
        print("Lutfen ogrenci ad soyadini kontrol ediniz!")

# Birden Fazla Ogrenci Silme Fonksiyonu
def ogrencilerSil():
    while True:
        adSoyad = input("Ogrenci adi ve soyadi (cikmak icin 'q' harfine basiniz): ")
        if(adSoyad == "q"):
            break
        elif(adSoyad in ogrenciler):
            ogrenciler.remove(adSoyad)
            print("{} basariyla silindi.".format(adSoyad))
        else:
            print("Lutfen ogrenci ad soyadini kontrol ediniz!")

print("""
********************************************
OGRENCİ KAYIT SISTEMINE HOSGELDINIZ! LUTFEN YAPMAK ISTEDIGINIZ ISLEMI SECINIZ.
1. OGRENCI EKLE
2. OGRENCI SIL
3. BIRDEN FAZLA OGRENCI EKLE
4. BIRDEN FAZLA OGRENCI SIL
5. OGRENCILERI LISTELE
6. OGRENCI NUMARASI SORGULA
CIKIS YAPMAK ICIN '0' RAKAMINI GIRINIZ.
********************************************""")

while True:
    islem = input("Lutfen yapmak istediginiz islemi giriniz: ")

    if (islem == "0"):
        print("Cikis yaptiniz.")
        break
    elif(islem == "1"):
        ogrenciEkle()
    elif(islem == "2"):
        ogrenciSil()
    elif(islem == "3"):
        ogrencilerEkle()
    elif(islem == "4"):
        ogrencilerSil()
    elif(islem == "5"):
        ogrencilerListe()
    elif(islem == "6"):
        ogrenciNumarasi()
    else:
        print("Hatali bir islem girdiniz!")
        break        
    

















