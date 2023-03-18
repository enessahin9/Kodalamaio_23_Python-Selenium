faiz = 1.59
vade = "36"
krediAdi = "Ihtiyac Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade) + 12)
# print(int(krediAdi) + 12) // Hatali kodlama ornegi.
faiz = str(faiz)
print(type(faiz))

vade = 36 # int(input("Lutfen istediginiz vade sayisini giriniz: "))
print(type(vade))
vade = vade + 12

# string interpolation
# Sectiginiz vade sonucu ortaya cikan vade:
print("Sectiginiz vade sonucu ortaya cikan vade: " + str(vade))
print("Sectiginiz vade sonucu ortaya cikan vade: {vadeSayisi}".format(vadeSayisi=vade))
print(f"Sectiginiz vade sonucu ortaya cikan vade: {vade}")

isim = "Enes" # input("Adinizi giriniz: ")
metin = "Merhaba {name}".format(name = isim)
print(metin)

#  f-string
metin = f"Hos geldiniz {isim}"
print(metin)

# listeler
dizi = ["Konut Kredisi", 10, 5.2, True]
print(dizi)

krediler = ["Ihtiyac kredisi", "Tasit Kredisi", "Konut Kredisi"]
print(type(krediler))

print(krediler[0])
print(len(krediler)) # length fonksiyonu dizinin uzunlugunu ogrenmeye yarar.
# print(krediler[3]) -> Hata verir.

krediler.append("Ozel Kredi") # .append -> bir objeyi girilen listenin sonuna ekler.
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0) # .pop -> degeri verilmezse listenin sonundaki verilirse listenin o elemanini siler.
print(krediler)

krediler.append("Tasit Kredisi")
print(krediler)

krediler.remove("Tasit Kredisi")
print(krediler)

krediler.extend(["Y Kredisi", "Z Kredisi"])
print(krediler)

# donguler -> bir condition calistigi surece tekrar tekrar saglanmasi dongudur.

# for dongusu
for i in range(10): # aksi belirtilmezse default olarak 0'dan baslar.
    print("xx")
    print(i)

print("****************************")

for i in range(5,10):
    print(i)

print("****************************")

for i in range(0,50,10): # 0'dan 50'ye kadar 10'ar arttır.
    print(i)

print("****************************")

krediler = ["Ihtiyac kredisi", "Tasit Kredisi", "Konut Kredisi"]
for kredi in krediler:
    print(kredi)

print("****************************")

for i in range(len(krediler)):
    print(krediler[i])

print("****************************")

# while dongusu
i = 0
while i < 10:
    print("x")
    i = i + 1 # i += 1 diye de yazilabilir.
print("y")

print("****************************")

while True:
    print("X")
    break

print("****************************")

i = 0
while i < len(krediler):
    i += 1
    print(i)
    print(krediler[i])
    # i += 1 yaziminin konumu ciktiyi degistirir.
    if krediler [i] == "Konut Kredisi":
        break
    
# fonksiyonlar
fiyat = 100
indirim = 20

def calculate(): # definition define
    print(100-20)

def calculateWithParams(fiyat, indirim):
    print(fiyat - indirim)

def sayHello(name):
    print(f"Merhaba {name}")

calculate() 
calculateWithParams(50, 10)
calculateWithParams(100, 30)
sayHello("Enes")
sayHello("Erto")
sayHello("Dogus")

def calculateAndReturn(price, discount):
    return price - discount

yeniFiyat = calculateAndReturn(200, 50)
print(yeniFiyat + 10)

# void
def calculatePrice(price, discount):
    print(price - discount)

def calculatePriceAndReturn(price, discount):
    return price - discount

print("****************************")
fonk1 = calculatePrice(100,50)
fonk2 = calculatePriceAndReturn(300,100)
print(f"151. Satir: {fonk1}")
print(f"152. Satir: {fonk2}")
print("****************************")
