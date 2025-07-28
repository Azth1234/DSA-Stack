class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # circular connection
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        print("Circular List: ", end="")
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

    def delete(self, key):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        prev = None

        while True:
            if current.data == key:
                if current == self.head:
                    # If only one node
                    if current.next == self.head:
                        self.head = None
                    else:
                        # Find the last node
                        last = self.head
                        while last.next != self.head:
                            last = last.next
                        self.head = current.next
                        last.next = self.head
                else:
                    prev.next = current.next
                print("Deleted", key, "from the list.")
                return

            prev = current
            current = current.next

            if current == self.head:
                break

        print(key, "not found in the list.")


cll = CircularLinkedList()

cll.insert_end(10)
cll.insert_end(20)
cll.insert_end(30)

cll.display()

cll.delete(20)
cll.display()

cll.delete(100)
