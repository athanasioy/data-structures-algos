"""
Give an alternative implementation of the build expression tree method
of the ExpressionTree class that relies on recursion to perform an implicit
Euler tour of the tree that is being built.
"""
from abc import ABC, abstractmethod
import string


class Position(ABC):
    def __init__(self, container):
        self.container = container
    @abstractmethod
    def element(self):
        ...

class Tree(ABC):

    @abstractmethod
    def root(self):
        ...

    @abstractmethod
    def parent(self,p:Position)->Position:
        ...

    @abstractmethod
    def children(self,p:Position):
        ...

    @abstractmethod
    def add_root(self,value):
        ...

    def num_childern(self,p):
        return len(self.children(p))

    @abstractmethod
    def is_leaf(self,p):
        ...


class BTreePosition(Position):
    def __init__(self, container, node):
        super().__init__(container)
        self.node = node

    def element(self):
        return self.node.value

class Node:
    def __init__(self, left, right, parent, value):
        self.value =value
        self.left = left
        self.right = right
        self.parent =parent

class LinkedBinaryTree(Tree):

    def __init__(self):
        self._size = 0
        self._root = None

    def _make_pos(self, n):
        if n is not None:
            return BTreePosition(self, n)

    def _validate_pos(self, p:BTreePosition):
        if not isinstance(p, BTreePosition):
            raise TypeError(f"p is not of type BTreePosition.(p is type of {type(p)})")
        if p.container is not self:
            raise ValueError("position does not belong to this tree")
        if p.node.parent == p.node:
            raise ValueError("Position has been invalidated")

        return p.node

    def add_root(self, value):
        assert self._root is None
        new = Node(None,None,None, value)
        self._root = new
        self._size +=1
        return self._make_pos(new)

    def root(self):
        return self._make_pos(self._root)

    def parent(self,p):
        n = self._validate_pos(p)
        return self._make_pos(n.parent)

    def left(self,p):
        n = self._validate_pos(p)
        return self._make_pos(n.left)

    def right(self,p):
        n = self._validate_pos(p)
        return self._make_pos(n.right)

    def is_leaf(self,p):
        n = self._validate_pos(p)
        return n.left is None and n.right is None

    def children(self,p):
        n = self._validate_pos(p)
        yield n.left
        yield n.right

    def add_left(self,p,value):
        n = self._validate_pos(p)
        new = Node(None,None,n,value)
        n.left = new
        self._size +=1
        return self._make_pos(new)

    def add_right(self,p,value):
        n = self._validate_pos(p)
        new = Node(None,None,n,value)
        n.right = new
        self._size +=1
        return self._make_pos(new)

    def __len__(self):
        return self._size

    def _attach(self, p, left, right):
        assert self.is_leaf(p)
        n = self._validate_pos(p)
        lroot = left.root()
        n.left = lroot.node
        lroot.node.parent = n

        rroot = right.root()
        n.right = rroot.node
        rroot.node.parent = n

        self._size += len(left)
        self._size += len(right)

        left._root = None
        left._size = 0

        right._root = None
        right._size = 0


class ExpressionTree(LinkedBinaryTree):
    def __init__(self, token, left:'ExpressionTree' = None, right:'ExpressionTree' = None):
        super().__init__()

        assert isinstance(token, str)
        self.add_root(token)
        if (left is None) ^ (right is None):
            raise ValueError("Both right and left trees must be supplied with a valid expression tree or nther of them ")
        if left is not None:
            assert token in "+-x/"
            self._attach(self.root(), left, right)

    def evaluate(self):
        return self._evaluate(self.root())

    def _evaluate(self, p):
        if self.is_leaf(p):
            return int(p.element())  # return the value
        left = self._evaluate(self.left(p))
        operator = p.element()
        right = self._evaluate(self.right(p))

        if operator == "+": return left + right
        elif operator == "-": return left - right
        elif operator == "/": return left / right
        else: return left * right

def _is_digit(token:str):
    i = 0
    while i < len(token):
        c = token[i]
        if c in string.digits:
            i +=1
        else:
            return False
    return True
def build_expr_tree(tokens:list[str]): # (((3x2)+1)/2)
    stack = []
    for t in tokens:
        if _is_digit(t):
           stack.append(ExpressionTree(t))
        elif t in "+/-*x":
            stack.append(t)  #append the operator
        elif t == ")":
            right = stack.pop()
            op = stack.pop()
            left = stack.pop()
            stack.append(ExpressionTree(op, left, right))

    return stack.pop()


def build_expr_tree2(token_iterator):
    token = next(token_iterator)
    if _is_digit(token):
        return ExpressionTree(token)
    if token in "*x/+-":
        op = token
        return token
    elif token == "(":
        left = build_expr_tree2(token_iterator)
        op = build_expr_tree2(token_iterator)
        right = build_expr_tree2(token_iterator)
        return ExpressionTree(op,left,right)
    elif token == ")":
        return build_expr_tree2(token_iterator)  #Next token please

class EulerTour:

    def __init__(self, tree:LinkedBinaryTree):
        self._tree = tree

    def exec(self):
        self._tour(self._tree.root(), 0, [])

    def _tour(self, p,depth,path):
        self._previsit(p, d, path)
        left = self._tree.left(p)
        right = self._tree.right(p)
        results = []
        if left is not None:
            path.append(0)
            results[0] = self._tour(left, depth+1, path)
            path.pop()

        self._invisit(p,depth,path)
        if right is not None:
            path.append(1)
            results[1] = self._tour(left, depth+1, path)
            path.pop()
        self._postvisit(p,d,path,results)
        return results

    def _previsit(self,p,depth,path):
        pass

    def _invisit(self,p,depth,path):
        pass

    def _postvisit(self,p,depth,path,results):
        pass
def tokenize(expr:str) -> list[str]:
    tokens = []
    i = 0
    while i < len(expr):
        c = expr[i]
        if c in "()":
            tokens.append(c)
            i+=1
        elif c in "x+/-*":
            tokens.append(c)
            i+=1
        elif c in string.digits:
            start = i
            while expr[i] in string.digits:
                i +=1
                if i >= len(expr):
                    break
            tokens.append(expr[start:i])
        else:
            raise ValueError(f"Invalid input {expr}. Unreconginzed char {c}")


    return tokens



expr = "(((2x6)/10)+13-2)"
expr2 = "(((2x6)x3)x10)"
expr3 = "(((2x10)+5)/5)"
tokens = tokenize(expr)
tokens2 = tokenize(expr2)
tokens3 = tokenize(expr3)
print(tokens)
print(tokens2)
expr2 = build_expr_tree2(iter(tokens3))
print(expr2.evaluate())
expr_tree = build_expr_tree(tokens)
t2 = build_expr_tree(tokens2)
print(expr_tree.evaluate())
print(t2.evaluate())
