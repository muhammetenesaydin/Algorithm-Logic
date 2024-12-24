"""Kendisine parametre olarak gelen tek boyutlu 
sayısal dizi içindeki negatif sayıların toplamını geri 
döndüren rekürsif methot yazınız.
"""

arr=[-1,-2,-3,-4,1,2,3,4,5,6,]

def negatif_toplam(arr):
    sum=0
    for i in arr:
        if i<0:
            sum+=i
        else :
            continue    
    return sum  
print(negatif_toplam(arr))