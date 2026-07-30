"""
Give a pseudo-code description of the delitem map operation when
sing a skip list.
"""

"""
routine del_item(k):
    pos = skipsearch(k)
    if pos == null:
        return null
    above = pos
    while above != null:
        pos.before.next = pos.after
        above = pos.above
    return pos

"""
