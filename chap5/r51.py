import sys
data=[]
for k in range(35):
    a=len(data)
    b=sys.getsizeof(data)
    print(f"Length: {a:3d}, Size in Bytes: {b:4d}")
    data.append(None)
