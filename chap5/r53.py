import sys
data=[]
old_size = 0
print("adding elements to list...")
for k in range(35):
    a=len(data)
    size=sys.getsizeof(data)
    if old_size != size:
        print(f"Length: {a:3d}, Size in Bytes: {size:4d}")
        old_size=size
    data.append(None)

print("removing elements from list...")
for k in range(35,0,-1):
    a=len(data)
    size=sys.getsizeof(data)
    if old_size != size:
        print(f"Length: {a:3d}, Size in Bytes: {size:4d}")
        old_size=size
    data.pop()

