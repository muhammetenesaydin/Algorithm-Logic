"""
8) Bir veya daha fazla kelimeden oluşan bir dizeyi alan ve aynı dizeyi döndüren, ancak beş veya daha fazla harfi ters olan tüm kelimelerle döndüren bir fonksiyon yazın (Tıpkı bu Kata'nın adı gibi). Geçirilen dizeler yalnızca harflerden ve boşluklardan oluşacaktır. Boşluklar yalnızca birden fazla kelime mevcut olduğunda dahil edilecektir.
"hey fellow warriors" --> "hey wollef sroirraw"
"this is a test --> "this is a test"
"this is another test" --> "this is rehtona test"

"""

def spin_words(sentence):

    words = sentence.split(" ")
    
    for i in range(len(words)):
        if len(words[i]) >= 5:
            words[i] = words[i][::-1]

    return " ".join(words)

print(spin_words("hey fellow warriors"))  
print(spin_words("this is a test"))       
print(spin_words("this is another test")) 
