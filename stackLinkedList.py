class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self,max_size):
        self.top=None
        self.max_size=max_size
        self.count = 0  # Track current size

    def is_Empty(self):
        return self.top is None

    def is_full(self):
        return self.count==self.max_size
    
    def push(self,data):
        if not self.is_full():
            new_node=Node(data)
            new_node.next=self.top
            self.top=new_node
            self.count += 1
        else:
            print("Overflow")

    
    def pop(self):
        if not self.is_Empty():
            popped_node=self.top
            self.top=popped_node.next
            popped_node.next=None
            self.count -= 1
            print(popped_node.data)
        else:
            print("underflow")

    def peek(self):
        if not self.is_Empty():
            print(self.top.data)
        else:
            print("Stack is Empty")

s = Stack(3 )
s.push(10)
s.push(20)
s.push(30)

s.peek()
s.pop()
s.pop()
s.pop()
s.pop()