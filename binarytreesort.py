import random
import networkx
from pyvis.network import Network


class BST:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return self.root.print()

    def fill(self, nodes, lo=0, hi=100):
        """
        add a specified number of nodes with random values to the tree
        :param nodes: number of nodes (including the root)
        :param lo: minimum value of nodes
        :param hi: maximum value of nodes
        """
        i = 0
        while i < nodes:
            self.addnode(random.randint(lo, hi))
            i += 1

    def addnode(self, data):
        """
        add a node of the specified value to the tree
        :param data:
        :return:
        """
        if not self.root:
            self.root = Node(data)
        else:
            self.root.addbelow(data)

    def converttonetx(self, graph):
        graph.add_node(self.root.data, color="red")
        self.root.converttonetx(graph)


class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

    def print(self):
        left = ''
        right = ''
        if self.left:
            left = self.left.print() + ' '
        if self.right:
            right = self.right.print() + ' '

        return left + str(self.data) + ' ' + right

    def addbelow(self, data):
        """
        adds a node in the proper space below this one (recursive)
        :param data: data to be stored in the new node
        """
        if data < self.data:
            if self.left:
                self.left.addbelow(data)
            else:
                self.left = Node(data)

        else:  # if the data is the same as current data, it'll be to the right
            if self.right:
                self.right.addbelow(data)
            else:
                self.right = Node(data)

    def converttonetx(self, graph):
        if self.left:
            graph.add_edge(self.data, self.left.data)
            self.left.converttonetx(graph)
        if self.right:
            graph.add_edge(self.data, self.right.data)
            self.right.converttonetx(graph)


if __name__ == "__main__":
    tree = BST()
    tree.fill(10)
    print(tree)

    treegraph = networkx.Graph()
    tree.converttonetx(treegraph)

    pnet = Network()
    pnet.from_nx(treegraph)
    pnet.show(
        "graphvis.html")
    # cross-links are due to duplicate numbers - the error is in the way i'm visualizing not the way i'm linking my graph
