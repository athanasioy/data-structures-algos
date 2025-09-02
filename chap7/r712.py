"""
Redo the previously problem with max as a method of the PositionalList
class, so that calling syntax L.max( ) is supported.
"""

class PositionalList:

    def max(self):
        m = None
        for e in self:
            if m is None or e>m:
                m = e
        return m


    def __iter__(self):
        _next = self.first()
        while _next is not None:
            yield _next.element()
            _next = self.after(_next)
