"""

Give a direct implementation of the num_children method within the class
BinaryTree.

"""


class Tree:
    class Position:

        def element(self):
            raise NotImplementError()


    def root(self):
        raise NotImplementError()

    def parent(self,p):
        raise NotImplementError()

    def num_children(self,p):
        children = [c for c in self.children(p)]
        return len(children)

    def children(self,p):
        raise NotImplementError()

    def __len__(self):
        raise NotImplementError()
