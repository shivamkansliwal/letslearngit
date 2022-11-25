#duplicate element in a list
#duplicate element in the perticular list
list=[1,2,3,4,1,2,5,3,5,100,100,51]
result=[]
for i in list:
    if i not in result:
        result.append(i)
print(result)        