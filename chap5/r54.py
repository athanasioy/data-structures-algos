import ctypes

class DynamicArray:

    def __init__(self,size=4):
        self._size = size
        self._A = self._make_array(size)
        self._n = 0

    def __getitem__(self,k):
        if abs(k)>=self._n:
            raise IndexError("Index out of range")
        if k>=0:
            return self._A[k]
        if k<0:
            return self._A[self._n+k]

    def append(self,obj):
        if self._n == self._size:
            self._resize(self._size*2)
        self._A[self._n]=obj
        self._n +=1

    def insert(self,k,obj):
        #r.5.6j
        if self._n == self._size:
            self._resize_append(self._size*2,k,obj)
            return
        for j in range(self._n,k,-1):
            self._A[j] = self._A[j-1]
        self._A[k]=obj
        self._n +=1

    def _make_array(self,size):
        return (size*ctypes.py_object)()

    def _resize(self,new_size):
        B = self._make_array(new_size)
        for i in range(self._n):
            B[i] = self._A[i]
        self._A = B
        self._size = new_size

    def _resize_append(self,new_size,k,obj):
        B = self._make_array(new_size)
        idx_appended = False
        for i in range(self._n+1):
            if i==k:
                B[i] = obj
                idx_appended =True
                continue
            if idx_appended:
                B[i] = self._A[i+1]
            else:
                B[i] = self._A[i]
        self._A = B
        self._size = new_size
    def __len__(self):
        return self._n

a = DynamicArray()
for i in range(10):
    a.append(i)
for i in range(len(a)):
    print(i)
    print(f"{i}={a[i]}")

for i in range(0, -len(a),-1):
    print(i)
    print(f"{i}={a[i]}")

