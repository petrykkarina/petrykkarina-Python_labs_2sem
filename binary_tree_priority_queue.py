class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None

    def __repr__(self):
        return f"({self.value}, p={self.priority})"


class PriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        new_node = Node(value, priority)
        self.root = self._insert(self.root, new_node)

    def _insert(self, root, node):
        if root is None:
            return node

        if node.priority <= root.priority:
            root.right = self._insert(root.right, node)
            return root
        else:
            root.left = self._insert(root.left, node)
            return root

    def peek(self):
        return self.root.value if self.root else None

    def pop(self):
        if not self.root:
            return None
        max_node = self.root
        self.root = self._merge(self.root.left, self.root.right)
        return max_node.value

    def _merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        if left.priority > right.priority:
            left.right = self._merge(left.right, right)
            return left
        else:
            right.left = self._merge(left, right.left)
            return right

    def _inorder(self, node):
        if not node:
            return []
        return (
            self._inorder(node.left)
            + [(node.value, node.priority)]
            + self._inorder(node.right)
        )

    def view(self):
        return self._inorder(self.root)


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert("task1", 3)
    pq.insert("task2", 5)
    pq.insert("task3", 1)
    pq.insert("task4", 4)

    print("Queue (inorder):", pq.view())
    print("Highest priority:", pq.peek())
    print("Deleted:", pq.pop())
    print("Queue after delete:", pq.view())
