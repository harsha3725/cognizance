lists=[]

lists.append(['No  Name  Marks'])
lists.append([1 ,  'Abc' , 90])
lists.append([2 ,  'Def'  ,95])
lists.append([3 , 'Ghi'  ,85])


for i in range(len(lists)):
    for j in range(len(lists[i])):
        print(lists[i][j],end="   ")
    print("")


for k in range(len(lists[2])):
    print(lists[2][k],end="\t")