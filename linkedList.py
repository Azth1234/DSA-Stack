class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        nb = Node(data)
        nb.next=self.head
        self.head=nb
        
    def insert_at_end(self, data):
        ne = Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
        # ne.next=None

    def insert_at_pos(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        # np.data=data
        np.next=temp.next
        temp.next=np
        
        

    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            print("Linked List:", end=" ")
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

    def delete_at_begin(self):
        temp = self.head
        self.head=temp.next
        temp.next=None
        
    def delete_at_end(self):
        temp = self.head.next
        prev=self.head
        while temp.next:
            temp=temp.next
            prev=prev.next
        prev.next=None
        
    def delete_at_pos(self,pos):
        temp = self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None


L = SingleLinkedList()
n1=Node(10)
L.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
L.display()
L.insert_at_begin(5)
L.display()
L.insert_at_end(40)
L.display()
L.insert_at_pos(3,25)
L.display()
L.delete_at_begin()
L.display()
L.delete_at_end()
L.display()
L.delete_at_pos(4)
L.display()


