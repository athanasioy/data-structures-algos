"""
What values are returned during the following sequence of deque ADT op-
erations, on initially empty deque? add first(4), add last(8), add last(9),
add first(5), back( ), delete first( ), delete last( ), add last(7), first( ),
last( ), add last(6), delete first( ), delete first( ).

Answer:
add_first(4) -> [4]
add_last(8) -> [4,8]
add_last(9) -> [4,8,9]
add_first(5) -> [5,4,8,9]
back() -> RET 9
delete_first() -> RET 5
delete_last() -> RET 9
add_last(7) -> [4,8,7]
first() -> RET 4
last() -> RET 7
add_last(6) -> [4,8,7,6]
delete_first() -> RET 4
delete_first() -> RET 8
"""
