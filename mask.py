"""Genellikle bir şey satın aldığınızda, kredi kartı numaranızın, telefon numaranızın
veya en gizli sorunuza verdiğiniz cevabın hala doğru olup olmadığı sorulur. 
Ancak, biri omzunuzun üzerinden bakabileceği için, bunu ekranınızda göstermek istemezsiniz.
Bunun yerine, bunu maskeleriz.
Göreviniz, son dört karakter hariç hepsini '#' olarak değiştiren bir fonksiyon yazmaktır.
2763547124245#########4245"""

def maskify(cc):
    l = len(cc)
    if l <= 4:
         return cc
    return (l - 4) * '#' + cc[-4:] 

print(maskify("4556364607935616"))