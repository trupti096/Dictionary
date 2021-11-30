d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
dic={}
for x in d1.keys():
    for y in d2.keys():
        if x==y:
            dic[x]=d1[x]+d2[y]
else:
    dic[x]=d1[x]
    dic[y]=d2[y]
print(dic)

#{'a':400,'b':400,'c':300,'d':400}
