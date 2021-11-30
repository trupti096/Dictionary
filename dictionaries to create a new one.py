dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic=dict(dic1)
dic.update(dic2)
dic.update(dic3)
for i,j in dic1.items():
    for m,n in dic2.items():
        for k,l in dic3.items():
            if i==m:
                dic[i]==j+m
print(dic)

#{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
