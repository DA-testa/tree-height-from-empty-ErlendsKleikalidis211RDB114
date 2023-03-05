n = int(input())
parents = list(map(int, input().split()))

tree = [[] for i in range(n)]
for i in range(n):
    if parents[i] == -1:
        root = i
    else:
        tree[parents[i]].append(i)

def compute_height(node):
    if not tree[node]:
        return 1
    else:
        heights = [compute_height(child) for child in tree[node]]
        return 1 + max(heights)

print(compute_height(root))
