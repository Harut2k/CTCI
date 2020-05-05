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
        if not self.Head:
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


def partition(head, pivot):
    a_head, a_tail = None, None
    b_head, b_tail = None, None
    node = head
    while node:
        if node.Data < pivot:
            if a_head:
                a_tail.NextPtr, a_tail = node, node
            else:
                a_head, a_tail = node, node
        else:
            if b_head:
                b_tail.NextPtr, b_tail = node, node
            else:
                b_head, b_tail = node, node
        node = node.NextPtr
    a_tail.NextPtr = b_head
    return a_head



myLL = LinkedList()

myLL.insert(5)
myLL.insert(3)
myLL.insert(2)
myLL.insert(5)
myLL.insert(4)
myLL.insert(8)
myLL.Head = partition(myLL.Head,4)
myLL.display()
