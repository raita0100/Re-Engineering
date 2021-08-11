class Node():

    def __init__(self, data: int):

        self.v = data
        self.left = None
        self.right = None


class Tree():

    def __init__(self, N: int):
        self.N =  N
        self.nodes = [Node(i) for i in range(1, N+1)]
        self.weights = {i:0 for i in range(1, N+1)}


    def add_edge(self, u: int, v: int):
        if (self.nodes[u-1].left == None):
            self.nodes[u-1].left = self.nodes[v-1]
        else:
            self.nodes[u-1].right = self.nodes[v-1]

    def add_weights(self, w):
        for i in range(0, len(w)):
            self.weights[i+1] = w[i]

    def print_tree(self):

        for i in self.nodes:
            l = r = None
            if i.left != None:
                l = i.left.v
            if i.right != None:
                r = i.right.v
            print(f"{i.v} --> [{l}, {r}]")
