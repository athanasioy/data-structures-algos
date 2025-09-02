"""
Implement a pop method for the DynamicArray class, given in Code Frag-
ment 5.3, that removes the last element of the array, and that shrinks the
capacity, N, of the array by half any time the number of elements in the
array goes below N/4.
"""

import ctypes

class DynamicArray:

    def __init__(self,size=4):
        self._A = self._make_array(size)
        self._capacity = size
        self._n = 0

    def __getitem__(self,k):
        if k > self._n:
            raise IndexError("Index out of range")
        return self._A[k]

    def append(self,elem):
        if self._n == self._capacity:
            self._resize(self._capacity*2)
        self._A[self._n] = elem
        self._n+=1

    def pop(self):
        if self._n == 0:
            raise IndexError("Pop from empty array")
        self._n-=1
        elem = self._A[self._n]
        self._A[self._n] = None
        if self._n < self._capacity//4:
            self._resize(self._capacity//2)
        return elem

    def _resize(self,new_size):
        B = self._make_array(new_size)

        # Copy elements from A to B
        for i in range(self._n):
            B[i] = self._A[i]
        self._A = B
        self._capacity = new_size

    def _make_array(self,size_of=4):
        return (size_of*ctypes.py_object)()

    def __len__(self):
        return self._n


array = DynamicArray()
array.append(0)
array.append(1)
array.append(2)
print(len(array))
array.pop()
print(len(array))
for i in range(len(array)):
    print(array[i])
