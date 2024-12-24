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





#####################
def negatif_toplam2 (array, index=0):
    if index == len(array):
        return 0

    if array[index] < 0:
        return array[index] + negatif_toplam2(array, index + 1)
    else:
        return negatif_toplam2(array, index + 1)
        
numara = [1, -2, 3, -4, 5, -6, 7, -8]
sonuc = negatif_toplam2(numara)
print(sonuc)
