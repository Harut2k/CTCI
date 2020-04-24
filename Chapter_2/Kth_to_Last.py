class Node:
    def __init__(self,Data = None,NextPtr = None):
        self.Data = Data
        self.NextPtr = NextPtr

class LinkedList:
    def __init__(self):
        self.Head = None
    def return_Head(self):
        return self.Head
    def insert(self,Data):
        if(self.Head==None):
            self.Head = Node(Data)
        else:
            CurrPtr = self.Head
            while(CurrPtr.NextPtr != None):
                CurrPtr = CurrPtr.NextPtr
            CurrPtr.NextPtr = Node(Data)
    def delete(self,num):
        if(num==0 and self.Head != None):
            self.Head = self.Head.NextPtr
        else:
            CurrPtr = self.Head
            PrevPtr = None
            while(num!=0 and CurrPtr):
                num-=1
                PrevPtr = CurrPtr
                CurrPtr = CurrPtr.NextPtr
            PrevPtr.NextPtr = CurrPtr.NextPtr

    def display(self):
        CurrPtr = self.Head
        while(CurrPtr != None):
            print(CurrPtr.Data)
            CurrPtr = CurrPtr.NextPtr



def kth_from_last(HeadPtr,num):
    CurrPtr = HeadPtr
    count = 0
    while(CurrPtr):
        count+=1
        CurrPtr = CurrPtr.NextPtr
    index = count - num
    CurrPtr = HeadPtr
    while(index!=0):
        CurrPtr = CurrPtr.NextPtr
        index-=1
    print(CurrPtr.Data)




myLL = LinkedList()
myLL.insert(3)
myLL.insert(2)
myLL.insert(5)
myLL.insert(4)
myLL.insert(5)
myLL.insert(8)
kth = int(input("Enter kth to last element to display"))
kth_from_last(myLL.return_Head(),kth)
