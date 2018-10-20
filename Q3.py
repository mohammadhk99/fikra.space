file = open ("C:\\users\\hp\\Downloads\\oscar.csv","r")
line=file.readlines()
ItemsList = list();
for i in line:
    list=[]
    list.append(i)
    print(list)
    for ii in str(list[0]):
        print(ii)
file.close()



file = open ("C:\\users\\hp\\Downloads\\oscar.csv","r")

ItemsList = list();
for i in file:
    ItemsList.append(list(i))
ListItem = list()
for i in ItemsList:
    print(i[3])
print(ItemsList[0])
file.close()
