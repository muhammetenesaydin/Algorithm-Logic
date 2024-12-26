"""Herhangi bir negatif olmayan tam sayıyı argüman olarak alabilen bir
 fonksiyon oluşturmak ve onu rakamları azalan sırayla döndürmektir. 
 Temelde, rakamları yeniden düzenleyerek mümkün olan en yüksek sayıyı oluşturun.
Örnek 
Giriş: 42145 Çıkış: 54421
Giriş: 145263 Çıkış: 654321
Giriş: 123456789 Çıkış: 987654321
"""


def sıralama(a):
    a = sorted(a, reverse=True) 
    for num in a:
        print(num, end="")  
    print()  
    return  


num = [int(x) for x in input("Sayı giriniz: ")]
sıralama(num)







