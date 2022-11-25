#duplicate element in a list
list=[1,2,3,4,1,2,5,3,5]
result=[]
for i in list:
    if i not in result:
        result.append(i)
print(result)        