#!/usr/bin/env python3
"""Exact, standard-library-only arithmetic audit of centered concatenations."""
from collections import Counter
from fractions import Fraction as Q
from itertools import permutations
from math import factorial
import json

def digit(n):
    return len(str(n))

def ell(n):
    return (10**n-1)//9

def centered(p):
    c = 0
    for n in p:
        c = c*10**digit(n)+n
    return (c-sum(p))//9

def distribution(K, modulus):
    """Prepend each unused block to a suffix; all operations are integers."""
    m = K-1
    size = 1 << m
    lengths = [0]*size
    for mask in range(1,size):
        low = mask & -mask
        lengths[mask] = lengths[mask^low]+digit(low.bit_length())
    e = [ell(d)%modulus for d in range(lengths[-1]+1)]
    dp = [[0]*modulus for _ in range(size)]
    dp[0][0] = 1
    for mask in range(size):
        for b in range(m):
            if mask & (1<<b):
                continue
            shift = (b+1)*e[lengths[mask]]%modulus
            dst = dp[mask | (1<<b)]
            for r,v in enumerate(dp[mask]):
                dst[(r+shift)%modulus] += v
    assert sum(dp[-1]) == factorial(m)
    return dp[-1]

def summarize(K):
    N = factorial(K-1)
    c = distribution(K,27)
    d9 = [sum(c[a::9]) for a in range(9)]
    d3 = [sum(c[a::3]) for a in range(3)]
    assert d3[1] == d3[2]
    a1 = Q(2*d3[0]-d3[1]-d3[2],2*N)
    L = [Q(1), Q(d3[0],N),Q(d9[0],N),Q(c[0],N)]
    shells = [L[n]-L[n+1] for n in range(3)]
    cs = [Q(3,2)*3**n*shells[n] for n in range(3)]
    lam1 = cs[1]/cs[0] if cs[0] else None
    lam2 = 2*cs[2]/cs[0]-lam1**2 if cs[0] else None
    theta = sum(n*ell(sum(digit(k) for k in range(1,K))-digit(n)) for n in range(1,K))
    m=K-1
    assert theta%9 == (digit(m)*m*(m-1)*(m+1)//2)%9
    assert all(d9[a] == d9[(theta-a)%9] for a in range(9))
    collision9 = sum(Q(x,N)**2 for x in d9)
    return dict(K=K,N=N,counts3=d3,counts9=d9,counts27=c,
                A1=str(a1),theta_mod9=theta%9,
                shell_counts_first3=[int(x*N) for x in shells],
                c_first3=[str(x) for x in cs],lambda1=str(lam1),lambda2=str(lam2),
                collision9=str(collision9),excess9=str(9*collision9-1))

def self_check():
    for K in range(2,9):
        brute = Counter(centered(p)%27 for p in permutations(range(1,K)))
        assert distribution(K,27)==[brute[a] for a in range(27)]
        for p in permutations(range(1,K)):
            D=sum(digit(n) for n in p)
            theta=sum(n*ell(D-digit(n)) for n in p)
            correction=0
            for i,n in enumerate(p):
                P=sum(digit(a) for a in p[:i])
                S=sum(digit(a) for a in p[i+1:])
                correction += n*ell(P)*ell(S)
            assert centered(p)+centered(p[::-1]) == theta-9*correction
            for i in range(len(p)-1):
                a,b=p[i:i+2]
                p2=p[:i]+(b,a)+p[i+2:]
                suffix=sum(digit(n) for n in p[i+2:])
                assert centered(p)-centered(p2)==10**suffix*(a*ell(digit(b))-b*ell(digit(a)))
    targets={3:'-1/2',4:'-1/2',5:'-1/4',6:'1/10',7:'1/10',8:'3/70',9:'-1/80',10:'-1/80',11:'-1/200',12:'331/61600',13:'331/61600'}
    rows=[summarize(K) for K in range(2,14)]
    for row in rows:
        if row['K'] in targets:
            assert row['A1']==targets[row['K']], (row,targets[row['K']])
    assert rows[3]['lambda1']=='9/20' and rows[3]['lambda2']=='-81/400'
    assert rows[4]['lambda1']=='31/24' and rows[4]['lambda2']=='479/576'
    assert Q(rows[7]['counts27'][0],rows[7]['N']) != Q(rows[8]['counts27'][0],rows[8]['N'])
    return rows

if __name__ == '__main__':
    rows=self_check()
    with open('mighty_k_exact_results.json','w') as f:
        json.dump(rows,f,indent=2)
    for r in rows:
        print(json.dumps(r))
