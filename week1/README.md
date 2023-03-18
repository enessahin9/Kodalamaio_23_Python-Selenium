  ### 1) Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.
  `Text Type:` str (String) ifadesi ile yazılır ve metinsel ifade çift tırnak içerisinde olmalıdır.
   
```python
a = "Merhaba Python!"
b = "16"
```
    
`Numeric Types:` int, float ve complex sayısal veri tipleridir. int (integer) sınırsız uzunluktaki pozitif ve negatif tam sayıları, float ondalık sayıları ve complex karmaşık sayıları ifade etmektedir.
    
```python
x = 7 #int 
y = 3.1 #float
z = 2 + 2j #complex
```

`Sequence Types:` list[], ve tuple() bu gruba giren veri tipleridir. tuple ve list birden çok ögeyi tek bir değişkende saklama imkanı verir. list'ler mutable'dır yani elemanlarını değiştirebilir, silebilir veya eleman ekleyebiliriz. Ama tuple'lar immutabledır, elemanlarını değiştiremeyiz.
 
```python
list1 = [6, 9, "Enes", "3"]
tuple1 = (6, 9, "Enes", "3")
```

`set:` list ve tuple'lar gibi birden çok elemanı tek bir değişkende saklayabilir. Fakat list ve tuple'lar gibi yinelenen elemanlara izin vermez ve sıralı değillerdir. Ayrıca immutable'dır.

```python
set1 = {"Enes", "Ertuğrul", "Doğuş"}
```

`dict:` Veri tiplerini key ve value şeklinde tutmamızı sağlar ve bir mapping işlemi yapmış oluruz. Duplicate değerlere izin vermez ve mutabledır.

```python
dict1 = {"brand": "Apple", "model": "iPhone", "year": "2007"}
print(dict1) #{'brand': 'Apple', 'model': 'iPhone', 'year': '2007'}
print(type(dict1)) #<class 'dict'>
print(dict1["year"]) #2007
```

`bool:` boolean veri tipidir. True ve False olarak iki değer verebilir.

```python
a = true
b = false
```

  ### 2) Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.
String: Ders Programı, Değerlendirme, Ödev 1, Ödev 2

int: Eğitim tamamlanma oranı

list: Kurslarım kategorisindeki seçenekler

  ### 3) Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.
  Kullanıcı Girişi:
```python
email = "abcd@gmail.com"
password = "abcd"
input1 = input("mail giriniz: ")
input2 = input("parola giriniz: ")
if(input1 == email and input2 == password):
    print("Giriş başarılı.")
else:
    print("E-postanız veya şifreniz yanlış.")
```



























    
 
