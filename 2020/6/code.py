#%%
with open('input.txt') as f:
    groups = f.read().split('\n\n')

#%% PART 1
totals = []
for grp in groups:
    people = grp.splitlines()
    uniq_answers = {ans for person in people for ans in person}
    totals.append(len(uniq_answers))
print(sum(totals))
# %% PART 2
totals = []
for grp in groups:
    people = grp.splitlines()
    answers = [{ans for ans in person} for person in people]
    everyone_answers = answers[0].intersection(*answers)
    totals.append(len(everyone_answers))
print(sum(totals))
# %%
