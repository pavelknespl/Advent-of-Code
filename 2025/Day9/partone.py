from itertools import combinations
pts = []
with open('input.txt') as f:
    for line in f:
        coords = list(map(int, line.strip().split(',')))
        pts.append(coords)
max_area = 0
for (x1, y1), (x2, y2) in combinations(pts, 2):
    width = abs(x1 - x2) + 1
    height = abs(y1 - y2) + 1
    area = width * height
    if area > max_area:
        max_area = area
print(max_area)