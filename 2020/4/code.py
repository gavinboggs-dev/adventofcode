#%%
import re

with open('input.txt') as f:
    input = f.read().split('\n\n')

passports = []
for psp in input:
    items = psp.split()
    d = {k:v for i in items for (k,v) in [i.split(':')]}
    passports.append(d)
# %% PART 1
req_fields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
]

cnt_valid = 0
for passport in passports:
    if all([
            field in passport for field in req_fields
        ]):
            cnt_valid = cnt_valid + 1
print(cnt_valid)

#%% PART 2

def test_hgt(s):
    unit = s[-2:]
    hgt = int(s[0:-2])
    if unit == 'cm':
        return 150 <= hgt <= 193
    elif unit == 'in':
        return 59 <= hgt <= 76
    return

tests = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': test_hgt,
    'hcl': lambda x: re.fullmatch(r'#[0-9a-f]{6}', x),
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: re.fullmatch(r'[0-9]{9}', x),
}

def check_req_fields(passport):
    return all(
            [field in passport for field in tests.keys()]
        )

def check_values(passport):
    for field, val in passport.items():
        test = tests.get(field, lambda x: True)
        try:
            res = test(val)
        except:
            res = False
        if not res:
            return
    return True
        
# %%
valid = 0
for passport in passports:
    if check_req_fields(passport):
        req = req + 1
        if check_values(passport):
            valid = valid + 1
print(valid)

# %%
