list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
i=0
dict={ }
while i<len(list1):
    dict[list1[i]]=list2[i]
    i=i+1      
print(dict)

#{'one':1,'two':2,'three':3,'four':4,'five':5}
