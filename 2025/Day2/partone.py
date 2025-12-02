def solve():
    t = 0
    with open('input.txt') as f:
        for r in f.read().strip().split(','):
            a, b = map(int, r.split('-'))
            for x in range(a, b + 1):
                s = str(x)
                l = len(s)
                if l % 2 == 0 and s[:l//2] == s[l//2:]:
                    t += x
    print(t)
solve()