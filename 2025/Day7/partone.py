grid = [l.rstrip() for l in open('input.txt')]
beams = set()
start_row = 0
for r, line in enumerate(grid):
    if 'S' in line:
        beams.add(line.index('S'))
        start_row = r
        break
splits = 0
for r in range(start_row, len(grid)):
    new_beams = set()
    for c in beams:
        if 0 <= c < len(grid[r]):
            if grid[r][c] == '^':
                splits += 1
                new_beams.update({c-1, c+1})
            else:
                new_beams.add(c)
    beams = new_beams
print(splits)