a="MISSISSIPPI"
i=0
d=0
str=""
s={}
while i<len(a):
    count=0
    j=0
    while j<len(a):
        if a[i]==a[j]:
            count=count+1
        j=j+1
    if a[i] not in str:
        str=str+a[i]
        d=count
        s[a[i]]=d
    i=i+1
print(s)