from Binary_tree_ import Tree

res = []
def in_order_helper(n):
    global res
    if n.left != None:
        in_order_helper(n.left)
    res.append(n.v)
    if n.right != None:
        in_order_helper(n.right)

def in_order(tree):
    global res
    res = []
    in_order_helper(tree.nodes[0])
    print("\nInorder : ")
    for i in res:
        print(f"{tree.weights[i]}", end=" ")

    print("\n\n")

def pre_order_helper(n):
    global res

    res.append(n.v)

    if n.left != None:
        pre_order_helper(n.left)
    if n.right != None:
        pre_order_helper(n.right)

def pre_order(tree):
    global res
    res = []
    pre_order_helper(tree.nodes[0])
    print("Preorder : ")
    for i in res:
        print(f"{tree.weights[i]}", end=" ")

    print("\n\n")

def post_order_helper(n):
    global res

    if n.left != None:
        post_order_helper(n.left)
    if n.right != None:
        post_order_helper(n.right)
    res.append(n.v)

def post_order(tree):
    global res
    res = []
    post_order_helper(tree.nodes[0])
    print("Postorder : ")
    for i in res:
        print(f"{tree.weights[i]}", end=" ")

    print("\n\n")

if __name__ == '__main__':
    visited = [False]*6
    t1 = Tree(5)
    t1.add_edge(1,2)
    t1.add_edge(1,3)
    t1.add_edge(2,4)
    t1.add_edge(2,5)
    t1.add_weights([45, 75, 25, 15, 35])
    t1.print_tree()

    in_order(t1)
    pre_order(t1)
    post_order(t1)
