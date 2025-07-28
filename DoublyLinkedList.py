class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
        
    def _insert_at_beginning(self,data):
        np=Node(data) 
        np.next=self.head
        self.head=np
        np.prev=None
        
    def _insert_at_ending(self,data):
        np=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=np
        np.prev=temp
    
    def _insert_at_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        np.prev=temp
        np.next=temp.next
        temp.next.prev=np
        temp.next=np
        
        
    def _delete_at_beginning(self):
         temp=self.head
         self.head=temp.next
         temp.next=None
         self.head.prev=None
         
    def _delete_at_ending(self):
        temp=self.head.next
        before=self.head
        while temp.next is not None:
            temp=temp.next
            before=before.next
        before.next=None
        temp.prev=None
    
    def _delete_at_position(self,pos):
        temp=self.head.next
        before=self.head
        for i in range (1,pos-1):
            temp=temp.next
            before=before.next
        before.next=temp.next
        temp.next.prev=before
        temp.next=None
        temp.prev=None        
        
    def display(self):
        if self.head is None:
            print('empty')
        else:
            temp=self.head
            while temp:
                print(temp.data,end="-->")
                temp=temp.next
            print('Null')
L=DLL()
n1=Node(10)
L.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(30)
n2.next=n3
n3.prev=n2
n4=Node(40)
n3.next=n4
n4.prev=n3
L._insert_at_beginning(19)
L._insert_at_ending(20)
L.display()
L._insert_at_position(4,100)
L.display()
L._delete_at_beginning()
L._delete_at_ending()
L.display()
L._delete_at_position(3)
L.display()