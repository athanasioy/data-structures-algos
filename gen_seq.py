import string
def gen_seq(k,S,U):
    for e in list(U):
        S.append(e)
        U.remove(e)
        if k==1:
            print(f'Solution:{S}')
        else:
            gen_seq(k-1,S,U)
        S.pop()
        U.append(e)


gen_seq(3,[],['a','b','c','d'])
