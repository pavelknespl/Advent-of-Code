from fractions import Fraction
from itertools import product

total_presses = 0
def get_rref(matrix, target):
    rows = len(matrix)
    if rows == 0: return None, None, None
    cols = len(matrix[0])
    m = [row[:] + [val] for row, val in zip(matrix, target)]
    pivot_row = 0
    pivots = []
    for col in range(cols):
        if pivot_row >= rows: break
        if m[pivot_row][col] == 0:
            for r in range(pivot_row + 1, rows):
                if m[r][col] != 0:
                    m[pivot_row], m[r] = m[r], m[pivot_row]
                    break
            else:
                continue
        pivots.append(col)
        pivot_val = m[pivot_row][col]
        m[pivot_row] = [x / pivot_val for x in m[pivot_row]]
        for r in range(rows):
            if r != pivot_row and m[r][col] != 0:
                factor = m[r][col]
                m[r] = [mx - factor * px for mx, px in zip(m[r], m[pivot_row])]
        pivot_row += 1
    for r in range(rows):
        if all(c == 0 for c in m[r][:-1]):
            if m[r][-1] != 0:
                return None, None, None # Nemá řešení
    return m, pivots, [c for c in range(cols) if c not in pivots]
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if not line: continue
        parts = line.split()
        target = list(map(int, parts[-1][1:-1].split(',')))
        n_equations = len(target)
        buttons = []
        for p in parts[1:-1]:
            if p.startswith('('):
                vec = [0] * n_equations
                indices = [int(x) for x in p[1:-1].split(',')]
                for idx in indices:
                    if idx < n_equations:
                        vec[idx] = 1
                buttons.append(vec)
        n_vars = len(buttons)
        if n_vars == 0: continue
        matrix = [[0] * n_vars for _ in range(n_equations)]
        for btn_idx, btn_vec in enumerate(buttons):
            for eq_idx, val in enumerate(btn_vec):
                matrix[eq_idx][btn_idx] = Fraction(val)
        target_frac = [Fraction(x) for x in target]
        rref, pivots, free_vars = get_rref(matrix, target_frac)
        if rref is None:
            continue
        min_machine_presses = float('inf')
        bounds = []
        for f_idx in free_vars:
            affected_targets = [target[i] for i in range(n_equations) if buttons[f_idx][i] > 0]
            limit = min(affected_targets) if affected_targets else 0
            bounds.append(range(limit + 1))
        for free_vals in product(*bounds):
            solution = [Fraction(0)] * n_vars
            for i, val in enumerate(free_vals):
                solution[free_vars[i]] = Fraction(val)
            possible = True
            current_sum = 0
            for r, p_col in enumerate(pivots):
                val = rref[r][-1] # RHS
                for f_idx, f_val in zip(free_vars, free_vals):
                    val -= rref[r][f_idx] * Fraction(f_val)
                if val.denominator != 1 or val < 0:
                    possible = False
                    break
                solution[p_col] = val
            if possible:
                s = sum(int(x) for x in solution)
                if s < min_machine_presses:
                    min_machine_presses = s
        if min_machine_presses != float('inf'):
            total_presses += min_machine_presses
print(total_presses)