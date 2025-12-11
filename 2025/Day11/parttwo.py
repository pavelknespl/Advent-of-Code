from functools import lru_cache

adj = {}
for l in open('input.txt'):
    p = l.strip().split(': ')
    if len(p) == 2: adj[p[0]] = p[1].split()

@lru_cache(None)
def solve(u, m):
    if u == 'dac': m |= 1
    if u == 'fft': m |= 2
    
    if u == 'out': return 1 if m == 3 else 0
    return sum(solve(v, m) for v in adj.get(u, []))

print(solve('svr', 0))