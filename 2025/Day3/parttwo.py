t = 0
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if not line: continue
        drop = len(line) - 12
        out = []
        for d in line:
            while drop and out and out[-1] < d:
                out.pop()
                drop -= 1
            out.append(d)
        t += int(''.join(out[:12]))
print(t)