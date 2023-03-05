import sys
import threading

def compute_height(node, tree):
    if not tree[node]:
        return 1
    else:
        heights = [compute_height(child, tree) for child in tree[node]]
        return 1 + max(heights)

def main():
    # input number of elements
    n = int(input())
    # input values in one variable, separate with space, split these values in an array
    parents = list(map(int, input().split()))
    # create a tree data structure as a list of lists
    tree = [[] for i in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)
    print(compute_height(root, tree))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
