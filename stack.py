class Stack:
    def __init__(self,max_size):
        self.items = []  # Initialize an empty list to store stack elements
        self.max_size = max_size
    
    def is_empty(self):
        return len(self.items) == 0
    
    def is_full(self):
        return len(self.items) == self.max_size
    
    def push(self, item):
        if not self.is_full():
            self.items.append(item)  # Add item to the top of the stack
        else:
            print("Overflow")
    
    def pop(self):
        if not self.is_empty():
            print(self.items.pop())  # Remove and return the top item
        else:
            print("Underflow")    
    def peek(self):
        if not self.is_empty():
            print(self.items[-1])  # Return the top item without removing it
        else:
            print("Stack is Empty")
    
    def size(self):
        return len(self.items)

# Example usage
stack = Stack(3)
stack.push(30)
stack.push(20)
stack.push(10)
stack.push(5)
stack.peek() # Output: 
stack.pop() 
stack.pop()
print(stack.size()) # Output: 2
print(stack.is_empty()) # Output: False
stack.pop()
stack.peek() # Output: 
stack.pop()