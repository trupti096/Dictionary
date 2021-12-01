a="MISSISSIPPI"
n={}
c=0
for i in a:
    a.split()
    if i in n:
        n[i]+=1
    else:
        n[i]=1
print(n)

#{'M':1,'I':4,'S':4,'P':2}
