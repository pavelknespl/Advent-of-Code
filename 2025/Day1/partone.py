def solve():
    pos = 50
    count = 0
    with open('input.txt') as f:
        for line in f:
            d = line[0]
            val = int(line[1:])
            if d == 'R':
                pos = (pos + val) % 100
            else:
                pos = (pos - val) % 100
            if pos == 0:
                count += 1
    print(count)
solve()