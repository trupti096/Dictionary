dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic4={}
for i in dic2:
    if i in dic1:
        dic2[i]=dic2[i]+dic1[i]
        dic4.update(dic1)
        dic4.update(dic2)
        dic4.update(dic3)
        for i,j in dic1.items():
            for m,n in dic2.items():
                for k,l in dic3.items():
                    if i==m:
                        dic4[i]==j+m
print(dic4)