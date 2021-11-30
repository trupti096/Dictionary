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

# {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
