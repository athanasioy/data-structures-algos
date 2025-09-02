"""
Consider what happens if the loop in the ArrayQueue. resize method at
lines 53–55 of Code Fragment 6.7 had been implemented as:

```
for k in range(self.size):
    self.data[k] = old[k] # rather than old[walk]
```

Give a clear explanation of what could go wrong.

Answer:
In ArrayQueue, the logical sequenece of the
stored elements may differ from the physical
order of the backing array due to circular
way of storing. ArrayQueue thus holds a front
variable which keeps which element is next
in the queue. Since the backing array has a fixed
size, we need to loop around when the front value
reached the size of the array. This is done
by the modulus operator.


Copying the elements from the old to the array
without reordering (i.e. self._front=0 and copying
the front element to the first position of the new array) results
in erroneous calculations on the next available slot
in the new underlying array, since the "looping around"
achieved by the modulus operator would no longer
correspond to the self._front+self._size addition.

In other words, the old array stored the elements
in a circular manner for a given size of the array.
If the size of the array increases, then the looping
around would no longer correspond the the capacity
of the new array.

Assume for example an array of capacity=50, with
a front value of 40 and a size of 50.

the next enqueue operation would trigger a resize
such that the capacity would become 100 and every
element would be copying to the new underlying array
without reordering.

When enqueing, the computation of the next
available slot would naturally be front+size % capacity,
i.e. 40+50 % 100 99, which is obviously wrong,
since locations from 50 to 99 are unoccupied.

"""
