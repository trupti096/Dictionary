list = [1, 2, 3, 4] 
d={}
a=d
for i in list:
    d[i]={}
    d=d[i]
print(a)

#{1: {2: {3: {4: {}}}}}
