t = 0
with open('input.txt') as f:
    for r in f.read().strip().split(','):
        a, b = map(int, r.split('-'))
        for x in range(a, b + 1):
            s = str(x)
            if s in (s + s)[1:-1]:
                t += x
print(t)