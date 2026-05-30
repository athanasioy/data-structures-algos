"""
Give a pseudo-code description of an insertion into a hash table that uses
quadratic probing to resolve collisions, assuming we also use the trick of
replacing deleted entries with a special “deactivated entry” object.
"""

"""
Answer:
set_item:
    idx <- hash(key)
    first_avail_pos <- -1
    i <- 0
    while i <= table.length
    {
        probe <- (idx + i**2) mod table.length
        if table[probe] is null
        {
            pos <- first_avail_pos if first_avail_pos != -1 else probe
            table[pos] <- value
            return
        }
        if first_avail_pos == -1 and table[probe] == DEACTIVATED
        {
            first_avail_pos <- probe
        }

        if table[probe].key == key
        {
            table[probe] <- value
            return
        }
        i++
    }
    table[first_vail_pos] <- value

"""
