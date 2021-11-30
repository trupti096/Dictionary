a='w3resource'
n={}
c=0
for i in a:
    a.split()
    if i in n:
        n[i]+=1
    else:
        n[i]=1
print(n)