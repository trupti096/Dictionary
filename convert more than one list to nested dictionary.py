a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92]
i=0
dict={}
list=[]
while i<len(a):
    dict[a[i]]={b[i]:c[i]}
    i=i+1
list.append(dict)
print(list)

#[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
