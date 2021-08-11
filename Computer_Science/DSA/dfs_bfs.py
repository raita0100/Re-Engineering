from Binary_tree_ import Tree

visited = []
res = []
def dfs_helper(n):
    global res
    if not visited[n.v]:
        visited[n.v] = True
        res.append(n.v)
    if n.left != None:
        dfs_helper(n.left)
    if n.right != None:
        dfs_helper(n.right)

def depth_first_search(tree):

    global res, visited
    res = []
    visited = [False]*(tree.N+1)
    root = tree.nodes[0]
    print("\n\n")
    dfs_helper(root)
    for i in res:
        print(f"{i}", end=" ")
        #print(tree.weights[i], end=" ")
    print("\n\n")

def bfs_helper(n):
    global res
    global visited
    if n == None:
        return
    if not visited[n.v]:
        visited[n.v] = True
        res.append(n.v)
    if n.left != None:
        res.append(n.left.v)
        visited[n.left.v] = True
    if n.right != None:
        res.append(n.right.v)
        visited[n.right.v] = True
    bfs_helper(n.left)
    bfs_helper(n.right)


def breadth_first_search(tree):
    global res
    global visited
    res = []
    visited = [False]*(tree.N+1)
    bfs_helper(tree.nodes[0])
    print("\n\n")
    for i in res:
        print(f"{i}", end=" ")
        #print(tree.weights[i], end=" ")
    print("\n\n")

if __name__ == '__main__':
    visited = [False]*6
    t1 = Tree(5)
    t1.add_edge(1,2)
    t1.add_edge(1,3)
    t1.add_edge(2,4)
    t1.add_edge(2,5)
    t1.add_weights([45, 75, 25, 15, 35])
    print("\nTree : ")
    t1.print_tree()
    print("\nDFS : ")
    depth_first_search(t1)
    print("\nBFS : ")
    breadth_first_search(t1)
