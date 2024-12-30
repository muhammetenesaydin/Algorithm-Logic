
def sort_array(src):
    odds = sorted([x for x in src if x % 2 != 0])
    odd_index = 0
    result = []
    for number in src:
        if number % 2 == 0:
            result.append(number)  
        else:
            result.append(odds[odd_index])  
            odd_index += 1
    return result
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))