#%%
with open('input.txt') as f:
    lines = f.read().splitlines()
seats = [[c for c in l] for l in lines]
#%%
test_start = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
seats = [[c for c in l] for l in test_start.splitlines()]
# %%
def count_neighbors(seats, r, c):
    count_occupied = 0
    for dr in [-1,0,1]:
        for dc in [-1,0,1]:
            if not (dr==0 and dc==0):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(seats) and 0 <= nc < len(seats[0]):
                    # print(nr, nc, seats[nr][nc])
                    if seats[nr][nc] == '#':
                        count_occupied = count_occupied + 1
    return count_occupied

def print_seats(seats):
    for row in seats:
        print(''.join(row))
    print('\n\n')
# %%
changes = True
iteration = 0
print_seats(seats)
while changes or iteration == 0:
    iteration = iteration + 1
    changes = []
    for r, row in enumerate(seats):
        for c, this_seat in enumerate(row):
            if this_seat != '.':
                neighbors = count_neighbors(seats, r, c)
                if this_seat == 'L' and neighbors == 0:
                    changes.append((r,c,'#'))
                elif this_seat == '#' and neighbors >= 4:
                    changes.append((r,c,'L'))
    for r, c, value in changes:
        seats[r][c] = value
    total = sum([row.count('#') for row in seats])
    print(iteration, total)
print(total)
# %% PART 2

# %%
