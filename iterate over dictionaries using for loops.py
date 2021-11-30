dict={"Subhashree":100,
"Subhadra":200,
"Puja":300,
"Sushree":400,
"Trupti":500}
sum=0
a={}
for i in dict.values():
    sum=sum+i
    a[i]=sum
print(sum)
