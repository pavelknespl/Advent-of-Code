from itertools import product

total_presses = 0
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if not line: continue
        parts = line.split()
        target_str = parts[0][1:-1]
        target = [1 if c == '#' else 0 for c in target_str]
        num_lights = len(target)
        buttons = []
        for p in parts[1:]:
            if p.startswith('('):
                btn_vec = [0] * num_lights
                indices = [int(x) for x in p[1:-1].split(',')]
                for idx in indices:
                    if idx < num_lights:
                        btn_vec[idx] = 1
                buttons.append(btn_vec)
        min_presses = float('inf')
        found = False
        for p_map in product([0, 1], repeat=len(buttons)):
            current_state = [0] * num_lights
            press_count = 0
            for i, press in enumerate(p_map):
                if press:
                    press_count += 1
                    for j in range(num_lights):
                        current_state[j] ^= buttons[i][j]
            if current_state == target:
                if press_count < min_presses:
                    min_presses = press_count
                found = True
        if found:
            total_presses += min_presses
print(total_presses)