"""
Draw an example skip list S that results from performing the following
series of operations on the skip list shown in Figure 10.13: del S[38],
S[48] = x , S[24] = y , del S[55]. Record your coin flips, as well.
"""


"""
Answer:
    del S[38]
    SkipSearch(38)

    S1 <-> ... <-> 31 <-> 42 <-> ..
    S0 <-> ... <-> 20 <-> 31 <-> 39 <-> ..

    S[48] = 'x'

    S0 <-> .. <-> 44 <-> 48 <-> 50 <-> ..

    Coin Flip; 1 continue; 0 break
    random.randint(0,1) -> 0
    break

    S[24] = 'y'

    S0: <-> ... <-> 20 <-> 28 <-> 31 <-> ..
    CoinFlip;
    random.randint(0,1) -> 1
    S1: <-> ... 17 <-> 28 <-> 31 <-> ...
    CoinFlip;
    random.randint(0,1) -> 1
    S2: <-> .. <-> 17 <-> 28 <-> 31 <-> ...
    CoinFlip;
    random.randint(0,1) -> 0
    break;
"""
