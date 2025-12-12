import sys

shapes_areas = {}
regions = []
current_id = None
current_shape_area = 0
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if not line: continue
        if ':' in line and not 'x' in line:
            if current_id is not None: 
                shapes_areas[current_id] = current_shape_area
            current_id = int(line.replace(':', ''))
            current_shape_area = 0
        elif 'x' in line:
            if current_id is not None:
                shapes_areas[current_id] = current_shape_area
                current_id = None
                current_shape_area = 0
            regions.append(line)
        else:
            current_shape_area += line.count('#')
    if current_id is not None: 
        shapes_areas[current_id] = current_shape_area
success_count = 0
for line in regions:
    dims, counts = line.split(': ')
    w, h = map(int, dims.split('x'))
    reqs = list(map(int, counts.split()))
    region_area = w * h
    total_needed_area = 0
    for sid, count in enumerate(reqs):
        if count > 0:
            total_needed_area += shapes_areas[sid] * count
    if total_needed_area <= region_area:
        success_count += 1
print(success_count)