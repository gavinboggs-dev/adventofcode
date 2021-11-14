#%%
import math

with open('input.txt') as f:
    lines = f.read().splitlines()
trees = [[c=='#' for c in l] for l in lines]
# %%
height = len(trees)
width = len(trees[0])

#%% PART 1
x = 0
cnt_trees = 0
for row in trees:
    if row[x]:
        cnt_trees = cnt_trees + 1
    x = (x + 3) % width
print(cnt_trees)
# %% PART 1
slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]
totals = []
for right, down in slopes:
    y = 0
    x = 0
    cnt_trees = 0
    while y < height:
        if trees[y][x]:
            cnt_trees = cnt_trees + 1
        y = y + down
        x = (x + right) % width
    totals.append(cnt_trees)
# %%
math.prod(totals)
# %%
