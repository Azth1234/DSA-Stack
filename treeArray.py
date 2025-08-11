class BinaryTree:
    def __init__(self, size):
        # Create an array with size+1 to start indexing at 1
        self.tree = [None] * (size + 1)
        self.size = size
        self.last_index = 0  # No nodes yet, start at 0

    def insert(self, value):
        if self.last_index < self.size:
            self.last_index += 1
            self.tree[self.last_index] = value
        else:
            print("Tree is full")

    def display(self):
        print("Binary Tree (1-based index array):")
        # Skip index 0 as it's unused
        print(self.tree[1:self.last_index + 1])

    def get_left_child(self, i):
        left_index = 2 * i
        if left_index <= self.last_index:
            return self.tree[left_index]
        return None

    def get_right_child(self, i):
        right_index = 2 * i + 1
        if right_index <= self.last_index:
            return self.tree[right_index]
        return None

    def get_parent(self, i):
        if i == 1:
            return None  # Root has no parent
        parent_index = i // 2
        if parent_index >= 1:
            return self.tree[parent_index]
        return None


bt = BinaryTree(10)
bt.insert(10)  # index 1 (root)
bt.insert(20)  # index 2 (left child of root)
bt.insert(30)  # index 3 (right child of root)
bt.insert(40)  # index 4 (left child of node at index 2)

bt.display()

print("Left child of node at index 1:", bt.get_left_child(1))   # 20
print("Right child of node at index 1:", bt.get_right_child(1)) # 30
print("Parent of node at index 4:", bt.get_parent(4))           # 20
