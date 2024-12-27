"""Narsisistik Sayı (veya Armstrong Sayısı), her biri belirli bir tabandakibasamak
sayısının kuvvetine yükseltilmiş kendi basamaklarının toplamı olan pozitif 
bir sayıdır. Bu soruda kendimizi ondalık (taban 10) ile sınırlayacağız.

Örneğin, narsisistik olan 153'ü (3 basamak) ele alalım:
1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
ve narsisistik olmayan 1652'yi (4 basamak):
1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
Verilen sayının 10 tabanında Narsisistik bir sayı olup olmadığına bağlı olarak kodunuz doğru 
veya yanlış ('doğru' ve 'yanlış' ) döndürmelidir."""

def is_narcissistic(number):
    digits = list(map(int, str(number)))
    num_digits = len(digits)
    narcissistic_sum = sum(digit ** num_digits for digit in digits)
    return "doğru" if narcissistic_sum == number else "yanlış"

print(is_narcissistic(153))  
print(is_narcissistic(1652)) 
