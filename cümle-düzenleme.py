"""
Her kelimenin ilk harfini sonuna taşıyın, sonra kelimenin sonuna "ay" ekleyin. Noktalama işaretlerini olduğu gibi bırakın.

Örnekler
Merhaba Dünya # erhabaMay ünyaDay
Hello World ! # elloHay orldWay !
"""

def düzenlemeli(cümle):
    kelimeler = cümle.split(" ")
    sonuç = []
    
    for kelime in kelimeler:
        if not kelime:  # Boş kelimeyi atla
            continue
        
        # Kelimenin sonundaki noktalama işaretini ayır
        noktalama = ""
        if len(kelime) > 0 and not kelime[-1].isalpha():
            noktalama = kelime[-1]
            kelime = kelime[:-1]  # Noktalama işaretini kelimeden çıkar
        
        # Kelimeyi düzenle (en az 1 karakter olmalı)
        if len(kelime) > 0:
            yeni_kelime = kelime[1:] + kelime[0] + "ay" + noktalama
            sonuç.append(yeni_kelime)
        else:
            sonuç.append(noktalama)  # Sadece noktalama işareti varsa
    
    return " ".join(sonuç)

n = input("Cümle girin: ")
print(düzenlemeli(n))


