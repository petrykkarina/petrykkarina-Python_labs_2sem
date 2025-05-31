from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = str(value)
        self.left = left
        self.right = right


def sum_of_depths(root):
    def dfs(node, d):
        if not node:
            return 0
        return d + dfs(node.left, d + 1) + dfs(node.right, d + 1)

    return dfs(root, 0)


def bfs(root):
    q = deque([root])
    print("BFS:", end=" ")
    while q:
        n = q.popleft()
        print(n.value, end=" ")
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)
    print()


def print_tree(node, indent="", last=True):
    if node:
        print(indent, "└── " if last else "├── ", node.value, sep="")
        indent += "    " if last else "│   "
        has_left = node.left is not None
        has_right = node.right is not None
        if has_left or has_right:
            print_tree(node.left, indent, not has_right)
            print_tree(node.right, indent, True)


root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3)

print("Сума глибин:", sum_of_depths(root))
bfs(root)
print("Дерево:")
print_tree(root)
