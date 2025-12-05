parts = open('input.txt').read().split('\n\n')
ranges = [tuple(map(int, r.split('-'))) for r in parts[0].split()]
count = 0
for i in map(int, parts[1].split()):
    if any(a <= i <= b for a, b in ranges):
        count += 1
print(count)