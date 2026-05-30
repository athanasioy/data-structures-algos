"""
Explain why a hash table is not suited to implement a sorted map.
"""

"""Answer:
Hash tables store keys in a scattered way that
allows them to loopup random keys in constant time.
Hash tables have no efficient way of finding minimun
nor maximum keys apart from scanning each key
and returning the minimum or maximum. This
is an O(n) operation ,where n is the number of keys
stored in the hash table.
Similar arguments hold for finding keys less than
a given key, or calculating ranges between keys.
"""
