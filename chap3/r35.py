"""
Assuming it is possible to sort n numbers in O(n log n) time, show that it
is possible to solve the three-way set disjointness problem in O(n log n)
time.

Answer:
I will create a new array of S1+S2+S3=S' with a total of N elements in 3n time, which is O(n). Then i Will sort S' in O(nlogn) time. Then I will compare each element of S' with the next one, for a total of 3n-1 times, which runs in O(n). If every element is not equal to each other, then the tree sets are disjoint.
"""
