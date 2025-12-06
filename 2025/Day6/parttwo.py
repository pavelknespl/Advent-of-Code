lines = [l.rstrip('\n') for l in open('input.txt')]
if not lines: 
    print("Empty")
w = max(len(l) for l in lines)
lines = [l.ljust(w) for l in lines]
grand_total = 0
block = []
for c in range(w - 1, -1, -1):
    col = [row[c] for row in lines]
    if all(ch == ' ' for ch in col):
        if block:
            nums = []
            op = '+' 
            for col_chars in block:
                if col_chars[-1] in '*+':
                    op = col_chars[-1]
                num_str = "".join(col_chars[:-1]).replace(" ", "")
                if num_str:
                    nums.append(int(num_str))
            if op == '+':
                grand_total += sum(nums)
            else:
                res = 1
                for n in nums: res *= n
                grand_total += res
            block = []
    else:
        block.append(col)
if block:
    nums = []
    op = '+'
    for col_chars in block:
        if col_chars[-1] in '*+':
            op = col_chars[-1]
        num_str = "".join(col_chars[:-1]).replace(" ", "")
        if num_str:
            nums.append(int(num_str))
    if op == '+':
        grand_total += sum(nums)
    else:
        res = 1
        for n in nums: res *= n
        grand_total += res
print(grand_total)