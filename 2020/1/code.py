#%%
with open('input.txt') as f:
    lines = f.read().splitlines()
# %%
nums = [int(l) for l in lines]
while nums:
    test = nums.pop()
    diff = 2020 - test

    if diff in nums:
        print(test*diff)
# %%
nums = [int(l) for l in lines]
while nums:
    test = nums.pop()
    for i, d1 in enumerate(nums):
        for d2 in nums[i:]:
            if (d1 + d2 + test) == 2020:
                print(test * d1 * d2)
                break
