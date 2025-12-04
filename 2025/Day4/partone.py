grid = [line.strip() for line in open('input.txt')]
rows = len(grid)
cols = len(grid[0])

count = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '@':
            neighbors = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue 
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                        neighbors += 1
            if neighbors < 4:
                count += 1
print(count)