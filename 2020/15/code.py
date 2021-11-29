#%%
starting = [7,12,1,0,16,2]
starting = [2,1,3]
numbers = starting
#%%
def rules(numbers):
    if numbers[-1] not in numbers[0:-1]:
        next_val = 0
    else:
        position = list(reversed(numbers[0:-1])).index(numbers[-1])
        next_val = position + 1
    numbers.append(next_val)
    return next_val
# %%
for i in range(len(starting), 2020):
    result = rules(numbers)
print(result)


# %% PART 2
# needs to be more efficient
numbers = [7,12,1,0,16,2]
memory = {n:i for i,n in enumerate(numbers[0:-1])}
hold = {numbers[-1]:len(numbers)-1}
value = numbers[-1]
for i in range(len(numbers), 30000000):
    # print(memory)
    last_i = memory.get(value)
    # print(value, last_i)
    if last_i is not None:
        value = i - last_i - 1
    else:
        value = 0
    memory.update(hold)
    hold = {value: i}
print(value)
# %%
