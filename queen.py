def solve(n, col=[], d1=[], d2=[], r=0):
    if r == n:
        print(col)
        return
    for c in range(n):
        if c not in col and r-c not in d1 and r+c not in d2:
            solve(n, col+[c], d1+[r-c], d2+[r+c], r+1)

solve(4)