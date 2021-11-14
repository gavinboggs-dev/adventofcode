# %%
import parse
pr = parse.compile('{:d}-{:d} {}: {}')

with open('input.txt') as f:
    lines = f.read().splitlines()
parts = [pr.parse(l) for l in lines]

# %% PART 1
valid = 0
for lower, upper, letter, password in parts:
    occurances = password.count(letter)
    if lower <= occurances <= upper:
        valid = valid+1
print(valid)
# %% PART 2
valid = 0
for lower, upper, letter, password in parts:
    if bool(password[lower-1] == letter) + bool(password[upper-1] == letter) == 1:
        valid = valid+1
print(valid)
