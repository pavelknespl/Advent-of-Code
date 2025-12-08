from itertools import combinations
from collections import Counter
pts = [list(map(int, l.split(','))) for l in open('input.txt')]
pairs = []
for (i, p1), (j, p2) in combinations(enumerate(pts), 2):
    d = sum((c1 - c2)**2 for c1, c2 in zip(p1, p2))
    pairs.append((d, i, j))
pairs.sort()
parent = list(range(len(pts)))
def find(i):
    if parent[i] != i:
        parent[i] = find(parent[i])
    return parent[i]
for _, u, v in pairs[:1000]:
    root_u = find(u)
    root_v = find(v)
    if root_u != root_v:
        parent[root_u] = root_v
counts = Counter(find(i) for i in range(len(pts))).values()
top3 = sorted(counts, reverse=True)[:3]
res = 1
for x in top3:
    res *= x
print(res)