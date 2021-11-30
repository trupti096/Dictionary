list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
i=0
dict={}
while i<len(list1):
    dict[list1[i]]=(list2[i])
    i=i+1
print(dict)

#{1:6,2:7,3:8,4:9,5:10}
