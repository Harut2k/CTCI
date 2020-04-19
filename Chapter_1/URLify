
#time complexity is O(n)
def urlify(list,size):
    numspace=0
    for i in range(0,size-1):
        if(list[i]==' '):
            numspace+=1
    indexChar = size-1
    indexPlace = size - 1 + 2 * numspace
    while(indexChar != -1):
        if(list[indexChar]==' '):
            list[indexPlace]='0'
            indexPlace-=1
            list[indexPlace]='2'
            indexPlace-=1
            list[indexPlace]='%'
            indexPlace-=1
            indexChar-=1

        else:
            list[indexPlace]=list[indexChar]
            indexPlace-=1
            indexChar-=1
    for i in range(0,size+2*numspace):
        print(List[i])



string =  "Mr John Smith    "#13
size = 13
List = []
for i in string:
    List.append(i)



urlify(List,size)
