"""
What is the expected running time of the methods for maintaining a max-
ima set if we insert n pairs such that each pair has lower cost and perfor-
mance than one before it? What is contained in the sorted map at the end
of this series of operations? What if each pair had a lower cost and higher
performance than the one before it?
"""


"""
Answer:
Maxima sets container maximum points which dominate
all other points in terms of cost and perfomance. Maxima
sets hold cost values as keys and perfomance values as
value inside a SortedTableMap.

SortedTableMaps stores values inside a array that is
always sorted. When continuously adding to the maxima
set values such that each pair has lower cost and perfomance
than the previous one, we can surmise two things.
1. no pair dominates any other pair
2. we are constantly adding elements to the
first element in inside the sorted array.

Point #2 causes with each insertion a worst case
relocation of every element in the array, which results
in a 1+2+3...+n pattern of total operations, which is O(n^2).
Obviously, before inserting we do a 'less than' cost lookup
inside the SortedMap, which is O(nlogn), but that cost
gets dominated by O(n^2).

if every pair had lower cost and higher perfomance,
we would keep the underlying sorted array always
with Length = 1, which means that adding the
lower cost value at the first position would incur
a relocation cost of 1 + 1 + 1 ... + n which is O(n).
Binary searching for less than and greater than
cost with two elements at most is O(1). When
inserting n pairs, we incur a total cost of O(n).
Thus the resulting algorithm complexity is O(n).




"""
