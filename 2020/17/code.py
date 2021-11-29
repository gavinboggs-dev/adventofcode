#%%
input_str = """....#...
.#..###.
.#.#.###
.#....#.
...#.#.#
#.......
##....#.
.##..#.#"""

# input_str = """.#.
# ..#
# ###"""

start_state = [[c == '#' for c in line] for line in input_str.splitlines()]
#%% PART 1
# def get_neighbors(position):
#     z,r,c = position
#     neighbors = []
#     for dz in [-1, 0, 1]:
#         for dr in [-1, 0, 1]:
#             for dc in [-1, 0, 1]:
#                 if any([i != 0 for i in [dz,dr,dc]]):
#                     nz, nr, nc = (z+dz, r+dr, c+dc)
#                     neighbors.append((nz, nr, nc))
#     return neighbors

# def get(array, position):
#     print('position', position)
#     if any([p < 0 for p in position]):
#         return False
#     z, r, c = position
#     try:
#         return array[z][r][c]
#     except IndexError:
#         return False

# def apply_rules(position, big_array):
#     active = get(big_array, position)
#     neighbors = get_neighbors(position)
#     cnt_neighbors = [get(big_array, n) for n in neighbors].count(True)
#     if active:
#         if cnt_neighbors in [2, 3]:
#             return True
#         else:
#             return False
#     else:
#         if cnt_neighbors == 3:
#             return True
#         else:
#             return False

# def to_str(array):
#     for i, z in enumerate(array):
#         print('z =', i)
#         for r in z:
#             out = ['#' if c else '.' for c in r]
#             print(''.join(out))


# # %%
# big_array = [start_state]
# for cycle in range(6):
#     width = len(big_array[0][0]) + 2
#     height = len(big_array[0]) + 2
#     zsize = len(big_array) + 2
#     next_array = [[[False for w in range(width)] for h in range(height)] for z in range(zsize)]
#     for c in range(width):
#         for r in range(height):
#             for z in range(zsize):
#                 next_array[z][r][c] = apply_rules((z-1,r-1,c-1), big_array)
#     big_array = next_array
#     # to_str(big_array)

# total_cnt = 0
# for z in big_array:
#     for r in z:
#         total_cnt = total_cnt + r.count(True)
# print(total_cnt)

#%% PART 2
def get_neighbors(position):
    w,z,r,c = position
    neighbors = []
    for dw in [-1, 0, 1]:
        for dz in [-1, 0, 1]:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if any([i != 0 for i in [dw,dz,dr,dc]]):
                        nw, nz, nr, nc = (w+dw, z+dz, r+dr, c+dc)
                        neighbors.append((nw, nz, nr, nc))
    return neighbors

def get(array, position):
    if any([p < 0 for p in position]):
        return False
    w,z,r,c = position
    try:
        return array[w][z][r][c]
    except IndexError:
        return False

def apply_rules(position, big_array):
    active = get(big_array, position)
    neighbors = get_neighbors(position)
    cnt_neighbors = [get(big_array, n) for n in neighbors].count(True)
    if active:
        if cnt_neighbors in [2, 3]:
            return True
        else:
            return False
    else:
        if cnt_neighbors == 3:
            return True
        else:
            return False

def to_str(array):
    for i, w in enumerate(array):
        for j, z in enumerate(w):
            print('w =', i, 'z =', j)
            for r in z:
                out = ['#' if c else '.' for c in r]
                print(''.join(out))
# %%
big_array = [[start_state]]
for cycle in range(6):
    width = len(big_array[0][0][0]) + 2
    height = len(big_array[0][0]) + 2
    zsize = len(big_array[0]) + 2
    wsize = len(big_array) + 2
    print('size:', width, height, zsize, wsize)
    next_array = [[[[False for c in range(width)] for r in range(height)] for z in range(zsize)] for w in range(wsize)]
    for c in range(width):
        for r in range(height):
            for z in range(zsize):
                for w in range(wsize):
                    next_array[w][z][r][c] = apply_rules((w-1,z-1,r-1,c-1), big_array)
    big_array = next_array
#%%
total_cnt = 0
for w in big_array:
    for z in w:
        for r in z:
            total_cnt = total_cnt + r.count(True)
print(total_cnt)
# %%
