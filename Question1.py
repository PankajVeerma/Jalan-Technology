def alternate_pos_neg(arr):
    pos = [num for num in arr if num > 0]
    neg = [num for num in arr if num < 0]
    
    result = []
    i, j = 0, 0
    
    while i < len(pos) and j < len(neg):
        result.append(pos[i])
        result.append(neg[j])
        i += 1
        j += 1
        
    # Append remaining positive numbers, if any
    while i < len(pos):
        result.append(pos[i])
        i += 1
    
    # Append remaining negative numbers, if any
    while j < len(neg):
        result.append(neg[j])
        j += 1
    
    return result


array = []
n = int(input("Enter the length of Array"))
for i in range(0,n):
   array_element = int(input())
   array.append(array_element)
print(array)   
print(alternate_pos_neg(array))