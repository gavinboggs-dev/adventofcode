#%%
import re
import parse
pr = parse.compile('{rule}: {lower1:d}-{upper1:d} or {lower2:d}-{upper2:d}')

with open('rules.txt') as f:
    lines = f.read().splitlines()
rules_temp = [pr.parse(line).named for line in lines]
rules = {r.pop('rule'):r for r in rules_temp}
# %%
with open('nearby_tickets.txt') as f:
    lines2 = f.read().splitlines()
# %%
nearby = [[int(i) for i in line.split(',')] for line in lines2]
# %%
def fits_rules(i):
    for r in rules.values():
        if r['lower1'] <= i <= r['upper1'] or r['lower2'] <= i <= r['upper2']:
            return True
    return False

total = 0
for n in nearby:
    for i in n:
        if not fits_rules(i):
            total = total + i
print(total)
# %% PART 2
nearby_good = []
for n in nearby:
    if all([fits_rules(i) for i in n]):
        nearby_good.append(n)

def check_rule(rule, val):
    if rule['lower1'] <= val <= rule['upper1'] or rule['lower2'] <= val <= rule['upper2']:
        return True
    else:
        return False

result = {}
for i in range(len(nearby_good[0])):
    result[i] = []
    for r,v in rules.items():
        if all([check_rule(v, n[i]) for n in nearby_good]):
            result[i].append(r)
# %%
matches = {}
#%%
while any(result.values()):
    for k,v in result.items():
        if len(v) == 1:
            matches[v[0]] = k
            for r,l in result.items():
                result[r] = [j for j in l if j!=v[0]]

# %%
matches

# %%
your_ticket = [157,73,79,191,113,59,109,61,103,101,67,193,97,179,107,89,53,71,181,83]
prod = 1
for m, idx in matches.items():
    if m.split(' ')[0] == 'departure':
        prod = prod * your_ticket[idx]
print(prod)
# %%
