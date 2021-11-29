#%%
def mask(sum, array):
    for i, val in enumerate(array):
        diff = sum - val
        if diff in array[i+1:]:
            return True
    return False

with open('input.txt') as f:
    lines = f.read().splitlines()
lines = [int(l) for l in lines]
# %%
check_len = 25
for i, l in enumerate(lines[check_len:]):
    array = lines[i:i+check_len]
    if not mask(l, array):
        print(i, l)
        break
# %% PART 2
find_val = 27911108
list_len = len(lines)

for range_len in range(2,len(lines)):
    start = 0
    end = range_len
    print(range_len)
    s_array = []
    while end < list_len:
        if sum(lines[start:end]) == find_val:
            s_array = lines[start:end]
            print(s_array)
            print(min(s_array), max(s_array))
            print(min(s_array)+max(s_array))
            break
        start = start + 1
        end = end + 1
    if s_array: break
# %%
