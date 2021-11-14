#%%
with open('input.txt') as f:
    lines = f.read().splitlines()

#%%
rows = 128
def get_row(seat):
    r = 0
    B = [s == 'B' for s in seat[0:7]]
    for i, val in enumerate(B):
        r = r + (val * (rows / (2 ** (i+1))))
    return int(r)

cols = 8
def get_col(seat):
    c = 0
    R = [s == 'R' for s in seat[7:]]
    for i, val in enumerate(R):
        c = c + (val * (cols / (2 ** (i+1))))
    return int(c)

def get_seat_id(row, col):
    return row * 8 + col
# %% PART 1
seat_ids = []
for seat in lines:
    row = get_row(seat)
    col = get_col(seat)
    seat_ids.append(get_seat_id(row, col))

print(max(seat_ids))
# %% PART 2
seat_ids = sorted(seat_ids)

for i, seat in enumerate(seat_ids[0:-1]):
    next_seat = seat_ids[i+1]
    if next_seat - seat == 2:
        print(seat+1)
# %%
