t = 0
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if not line: continue
        t += max(int(line[i] + line[j]) for i in range(len(line)) for j in range(i + 1, len(line)))
print(t)