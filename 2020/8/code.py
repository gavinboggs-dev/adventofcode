#%%
with open('input.txt') as f:
    lines = f.read().splitlines()
# %%
accumulator = 0
line_number = 0
line_history = []

def acc(x):
    global accumulator, line_number
    accumulator = accumulator + x
    line_number = line_number + 1

def jmp(x):
    global line_number
    line_number = line_number + x

def nop(x):
    global line_number
    line_number = line_number + 1

cmd_lookup = {
    'acc': acc,
    'jmp': jmp,
    'nop': nop
}

#%%
instructions = []
for l in lines:
    cmd_str, num_str = l.split(' ')
    cmd = cmd_lookup[cmd_str]
    num = int(num_str)
    instructions.append((cmd, num))

# %% PART 1
while line_number not in line_history:
    line_history.append(line_number)
    cmd, num = instructions[line_number]
    cmd(num)
    print(accumulator)
# %% PART 2
instruction_sets = {}

def switch_op(inst):
    op, num = inst
    if op == nop: return (jmp, num)
    elif op == jmp: return (nop, num)
    else: return inst

for i, inst in enumerate(instructions):
    if inst[0] in [jmp, nop]:
        temp = instructions.copy()
        temp[i] = switch_op(temp[i])
        instruction_sets[i] = temp

def run_instructions(instructions):
    line_history = []
    global accumulator
    accumulator = 0
    global line_number
    line_number = 0

    while line_number < len(instructions):
        if line_number in line_history:
            return False
        line_history.append(line_number)
        cmd, num = instructions[line_number]
        cmd(num)
    return accumulator
# %%
for k, test_inst in instruction_sets.items():
    res = run_instructions(test_inst)
    if res:
        print(res)
        break
