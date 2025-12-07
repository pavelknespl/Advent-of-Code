grid = [l.rstrip() for l in open('input.txt')]
beams = {}
start_row = 0
for r, line in enumerate(grid):
    if 'S' in line:
        beams[line.index('S')] = 1
        start_row = r
        break
for r in range(start_row, len(grid)):
    new_beams = {}
    for c, count in beams.items():
        if 0 <= c < len(grid[r]):
            if grid[r][c] == '^':
                new_beams[c-1] = new_beams.get(c-1, 0) + count
                new_beams[c+1] = new_beams.get(c+1, 0) + count
            else:
                new_beams[c] = new_beams.get(c, 0) + count
    beams = new_beams
print(sum(beams.values()))