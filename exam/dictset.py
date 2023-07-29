#Generate a dictionary where keys are numbers and values consist of a set of its factors in a specified range.
#Factors = {1:{1} , 2:{1,2}, 3: {1,3}, 4:{1,2,4} , 5:{1,5}, 6:{1,2,3,6}, 7:{1,7}, 8:{1,2,4,8}, 9:{1,3,9,}}

d = dict()
for x in range(1,10):
    s = set()
    for i in range(1,x+1):
        if x%i == 0:
            s.add(i)
    d[x] = s
print("Factors: ",d)
