from math import sqrt, floor
from itertools import combinations

def gen_oblong_sums(M):
    oblongs = []
    for i in range(1, M):
        n = i*(i+1)
        s = "{}*{}".format(i,i+1)
        for r in range(len(oblongs)):
            for S in combinations(oblongs,r+1):
                N = sum([x for (x,y) in S]) + n
                if is_oblong(N):
                    I = floor(sqrt(N))
                    cur_str = '{}+{} = {}*{}'.format('+'.join([y for (x,y) in S]), s, I, I+1)
                    print(cur_str)
        oblongs.append( (n, s) )
    return

def is_oblong(n):
    i = floor(sqrt(n))
    return n == i*(i+1)

