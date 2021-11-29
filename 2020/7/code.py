#%%
import re
with open('input.txt') as f:
    lines = f.read().splitlines()
#%%
def process_lines(lines):
    rules = {}
    for line in lines:
        outer, inner_str = line.split(' bags contain ')
        inner_str = inner_str.split(', ')
        inner_str = [re.sub(' bag.*', '', i) for i in inner_str]
        inner_bags = {}
        for b in inner_str:
            cnt, color = b.split(' ', 1)
            if cnt != 'no': inner_bags[color] = int(cnt)
        rules[outer] = inner_bags
    return rules
rules = process_lines(lines)
# %% PART 1
test_bags = ['shiny gold']
all_outer_bags = set()
while test_bags:
    next_test_bags = []
    for test in test_bags:
        for outer_bag, inner_bags in rules.items():
            if test in inner_bags and inner_bags[test]>0:
                next_test_bags.append(outer_bag)
    test_bags = next_test_bags
    all_outer_bags = all_outer_bags.union(set(test_bags))
print(len(all_outer_bags))
# %% PART 2
small_test = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""
rules = process_lines(small_test.splitlines())
#%%
def recurse_rules(bag):
    contents = rules.get(bag)
    if not contents:
        return 1
    total = 1
    for inner_bag, cnt in contents.items():
        total = total + cnt * recurse_rules(inner_bag)
    return total

out = recurse_rules('shiny gold')
print(out - 1)
