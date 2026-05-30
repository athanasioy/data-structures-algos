"""
Our Position classes for lists and trees support the eq method so that
two distinct position instances are considered equivalent if they refer to the
same underlying node in a structure. For positions to be allowed as keys
in a hash table, there must be a definition for the hash method that
is consistent with this notion of equivalence. Provide such a hash
method.
"""


class Position:

    def __init__(self, node, container):
        self._node = node
        self._container = container

    def element(self):
        return self._node.value

    def __eq__(self, other):
        return type(self) is type(other) and self._node is other._node

    def __hash__(self):
        return hash(self._node)
