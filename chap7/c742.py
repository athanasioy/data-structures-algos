"""
Write a Scoreboard class that maintains the top 10 scores for a game application using a singly linked list, rather than the array that was used in
Section 5.5.1.

H -> 10 -> 20 -> 30 -> 40 -> None
H -> None
H -> 10 -> None
H -> 10 -> 15 -> None
H -> 1 -> 10 -> 15 -> None
H -> 5 -> 10 -> 15 -> None

H -> 40 -> 30 -> 20 -> 10 -> None
add 35
H -> 40 -> 35 -> 30 -> 20 -> None

H-> 40
H-> 40 -> 30
H -> 30 -> 40 -> 50 -> None
H -> 30 -> 35 -> 40 -> 50 -> None
H -> 30 -> 40 -> 45 -> 50 -> None
"""


class _Node:
    def __init__(self, next_node,element):
        self.next = next_node
        self.element = element

    def __repr__(self):
        return f"Value={self.element}"


class Scoreboard:


    class _ScoreStorage2:
        """
        Stores the lowest score at the head
        """
        def __init__(self, n:int):
            self._head = _Node(None,None)
            self._size = 0
            assert n>0
            self._n = n

        def add(self,e):
            if self._size == self._n and self._head.next.element > e:
                return
            cursor = self._head.next
            prev = self._head
            while cursor is not None and cursor.element < e:
                prev = cursor
                cursor = cursor.next
            newest = _Node(cursor,e)
            prev.next = newest
            if self._size < self._n:
                self._size+=1
            else:
                self._head.next = self._head.next.next

        def __iter__(self):
            c = self._head.next
            while c is not None:
                yield c.element
                c = c.next

        def __getitem__(self,k):
            if self._size <=k:
                raise IndexError("Index out of range")
            c = self._head.next
            for _ in range(k):
                c = c.next
            return c.element

    class _ScoreStorage:
        """ Stores the highest score at the head.
        """
        def __init__(self,n:int=10):
            self._head = _Node(None,None)
            self._n = n
            self._size = 0

        def add(self,e):
            cursor = self._head.next
            prev = self._head

            while cursor is not None and cursor.element > e:
                prev = cursor
                cursor = cursor.next
            newest = _Node(cursor, e)
            prev.next = newest

            if self._size == self._n:
                self._trim()
            else:
                self._size +=1

        def _trim(self):
            c = self._head.next
            for _ in range(self._n -1):
                c = c.next
            c.next =None


        def __iter__(self):
            c = self._head.next
            while c is not None:
                yield c.element
                c = c.next

        def __getitem__(self,k):
            if self._size <=k:
                raise IndexError("Index out of range")
            c = self._head.next
            for _ in range(k):
                c = c.next
            return c.element

    def __init__(self, n:int=10):
        self._board = self._ScoreStorage2(n)
        self._top_n=n

    def add_score(self, score):
        self._board.add(score)

    def get_scores(self):
        return [score for score in self._board]

    def __getitem__(self,k):
        return self._board[k]


b = Scoreboard(3)

b.add_score(1)
b.add_score(20)
b.add_score(50)
b.add_score(2)
b.add_score(25)
b.add_score(-1)

for e in b._board:
    print(e)
print(b.get_scores())
print(b[0])
print(b[1])
print(b[2])
print(b[3])
