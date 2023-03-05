class Node:
    def __init__(self, index):
        self.index = index
        self.children = []

def compute_height(n, parents):
    nodes = [Node(i) for i in range(n)]
    root = None
    for i, parent_index in enumerate(parents):
        if parent_index == -1:
            root = nodes[i]
        else:
            parent_node = nodes[parent_index]
            parent_node.children.append(nodes[i])
    
    def get_height(node):
        if not node.children:
            return 1
        else:
            return 1 + max(get_height(child) for child in node.children)
    
    return get_height(root)

n = int(input())
parents = list(map(int, input().split()))
print(compute_height(n, parents))
