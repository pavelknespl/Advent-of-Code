from functools import lru_cache

adj = {}
for l in open('input.txt'):
    parts = l.strip().split(': ')
    if len(parts) == 2:
        adj[parts[0]] = parts[1].split()

@lru_cache(None)
def count(u):
    if u == 'out': return 1
    return sum(count(v) for v in adj.get(u, []))

print(count('you'))