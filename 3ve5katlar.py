"""Girilen sayının altındaki 3 veya 5'in tüm katlarının toplamını 
döndürecek şekilde program yazmanız isteniyor.
Ek olarak, sayı negatifse, 0 döndürün.
Not: Sayı hem 3'ün hem de 5'in katıysa, yalnızca bir kez sayın.
Örnek: 10'un altındaki 3 veya 5'in katları olan tüm doğal sayıları listelersek,
 3, 5, 6 ve 9'u elde ederiz. Bu katların toplamı 23'tür."""



def katlar(a):
    if a < 0:
        return [] 
    else:
        sonuclar = []  
        while a > 0:
            if a % 3 == 0 and a % 5 == 0:
                sonuclar.append(a)  
            a -= 1  
        return sonuclar  

a = int(input("Sayı girin: ")) 
print(katlar(a))