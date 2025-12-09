from itertools import combinations

pts = [list(map(int, l.split(','))) for l in open('input.txt')]
if not pts: exit()
n = len(pts)
edges = []
for i in range(n):
    p1 = pts[i]
    p2 = pts[(i + 1) % n]
    edges.append((p1[0], p1[1], p2[0], p2[1]))
def is_inside(x, y):
    collisions = 0
    for x1, y1, x2, y2 in edges:
        if x1 == x2 and x1 > x:
            if (y1 > y) != (y2 > y):
                collisions += 1
    return collisions % 2 == 1
def intersects_boundary(rx1, ry1, rx2, ry2):
    rmin_x, rmax_x = min(rx1, rx2), max(rx1, rx2)
    rmin_y, rmax_y = min(ry1, ry2), max(ry1, ry2)
    for ex1, ey1, ex2, ey2 in edges:
        if ex1 == ex2:
            if rmin_x < ex1 < rmax_x:
                e_ymin, e_ymax = min(ey1, ey2), max(ey1, ey2)
                if max(rmin_y, e_ymin) < min(rmax_y, e_ymax):
                    return True
        else:
            if rmin_y < ey1 < rmax_y:
                e_xmin, e_xmax = min(ex1, ex2), max(ex1, ex2)
                if max(rmin_x, e_xmin) < min(rmax_x, e_xmax):
                    return True
    return False
candidates = []
for p1, p2 in combinations(pts, 2):
    area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
    candidates.append((area, p1, p2))
candidates.sort(key=lambda x: x[0], reverse=True)
max_valid_area = 0
for area, p1, p2 in candidates:
    if intersects_boundary(p1[0], p1[1], p2[0], p2[1]):
        continue
    mid_x = (p1[0] + p2[0]) / 2
    mid_y = (p1[1] + p2[1]) / 2
    if is_inside(mid_x, mid_y):
        max_valid_area = area
        break
print(max_valid_area)