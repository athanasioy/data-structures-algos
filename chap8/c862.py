"""
Note that the build expression tree function of the ExpressionTree class
is written in such a way that a leaf token can be any string; for example,
it parses the expression (a*(b+c)) . However, within the evaluate
method, an error would occur when attempting to convert a leaf token to
a number. Modify the evaluate method to accept an optional Python dictionary
that can be used to map such string variables to numeric values,
with a syntax such as T.evaluate({ a :3, b :1, c :5 }). In this way,
the same algebraic expression can be evaluated using different values.
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

    def evaluate(self, variables:dict[str,int] = {}):
        return self._evaluate(self.root(),variables)

    def _evaluate(self, p, variables):
        if self.is_leaf(p):
            if _is_digit(p.element()):
                return int(p.element())  # return the value
            elif _is_char(p.element()):
                try:
                    return variables[p.element()]
                except KeyError:
                    raise ValueError(f"Variable {p.element()} is not present in variables")
            else:
                assert False, "Impossible Code Path"
        left = self._evaluate(self.left(p), variables)
        operator = p.element()
        right = self._evaluate(self.right(p), variables)

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

def _is_char(token:str):
    i = 0
    while i < len(token):
        c = token[i]
        if c in string.ascii_letters:
            i +=1
        else:
            return False
    return True

def build_expr_tree(tokens:list[str]): # (((3x2)+1)/2)
    stack = []
    for t in tokens:
        if t in "+/-*x":
            stack.append(t)  #append the operator
        elif _is_digit(t) or _is_char(t):
           stack.append(ExpressionTree(t))
        elif t == ")":
            right = stack.pop()
            op = stack.pop()
            left = stack.pop()
            stack.append(ExpressionTree(op, left, right))

    return stack.pop()

def build_expr_tree2(tokens:list[str]) -> ExpressionTree:
    return _build_expr_tree2(iter(tokens))


def _build_expr_tree2(token_iterator):
    token = next(token_iterator)
    if token in "*x/+-":
        op = token
        return op
    elif _is_digit(token) or _is_char(token):
        return ExpressionTree(token)
    elif token == "(":
        left = _build_expr_tree2(token_iterator)
        op = _build_expr_tree2(token_iterator)
        right = _build_expr_tree2(token_iterator)
        return ExpressionTree(op,left,right)
    elif token == ")":
        return _build_expr_tree2(token_iterator)  #Next token please [call again to move the iteraror forward]

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
        elif c in string.ascii_letters:
            start = i
            while expr[i] in string.ascii_letters:
                i +=1
                if i >= len(expr):
                    break
            tokens.append(expr[start:i])
        else:
            raise ValueError(f"Invalid input {expr}. Unreconginzed char {c}")


    return tokens



expr = "(((2xa)/10)+(13-bb))"
tokens = tokenize(expr)
print(tokens)
vars = {}
vars["a"] = 20
vars["bb"]= 13

t = build_expr_tree2(tokens)
print(t.evaluate(vars))
