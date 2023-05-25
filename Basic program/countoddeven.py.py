list1=[20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50]
even_count,odd_count=0,0
for num in list1:
    if num%2==0:
        even_count += 1
    else:
        odd_count += 1
print("the even num is:",even_count)
print("the odd num is:",odd_count)
