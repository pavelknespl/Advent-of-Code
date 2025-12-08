from itertools import combinations
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
comps = len(pts)
for _, u, v in pairs:
    root_u = find(u)
    root_v = find(v)
    if root_u != root_v:
        parent[root_u] = root_v
        comps -= 1
        if comps == 1:
            print(pts[u][0] * pts[v][0])
            break