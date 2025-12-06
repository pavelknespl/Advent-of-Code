lines = [l.rstrip('\r\n') for l in open('input.txt')]
if not lines:
    print("Empty")
w = max(len(l) for l in lines)
lines = [l.ljust(w) for l in lines]
grand_total = 0
start = 0
for c in range(w + 1):
    is_empty = True
    if c < w:
        for row in lines:
            if row[c] != ' ':
                is_empty = False
                break
    if is_empty:
        block_text = ""
        for row in lines:
            block_text += row[start:c] + " "
        parts = block_text.split()
        if parts:
            nums = []
            op = None
            for p in parts:
                if p in '+*':
                    op = p
                else:
                    nums.append(int(p))
            if op == '+':
                grand_total += sum(nums)
            elif op == '*':
                res = 1
                for n in nums: res *= n
                grand_total += res
        start = c + 1
print(grand_total)