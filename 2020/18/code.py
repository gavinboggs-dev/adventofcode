#%%
def parse_parens(s):
    stack = []
    out = [(0, 0, len(s), s)]
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            start = stack.pop()
            out.append((len(stack)+1, start, i+1, s[start+1:i]))
    return out

def run_math(s):
    parts = s.split()
    numbers = [int(p) for i,p in enumerate(parts) if i%2==0]
    operators = [p for i,p in enumerate(parts) if i%2==1]
    result = numbers.pop(0)
    for i, op in enumerate(operators):
        if op == '+':
            result = result + numbers[i]
        elif op == '*':
            result = result * numbers[i]
    return result
# %%
with open('input.txt') as f:
    lines = f.read().splitlines()
# %%
result_list = []
for expression in lines:
    while True:
        ops = sorted(parse_parens(expression))
        level, start, end, exp = ops.pop()
        result = run_math(exp)
        expression = expression[0:start] + str(result) + expression[end:]
        if expression == str(result):
            print(result)
            result_list.append(result)
            break
# %%
sum(result_list)
# %% PART 2
def run_math_2(s):
    parts = s.split()
    numbers = [int(p) for i,p in enumerate(parts) if i%2==0]
    operators = [p for i,p in enumerate(parts) if i%2==1]
    i = 0
    while i < len(operators):
        op = operators[i]
        if op == '+':
            numbers[i] = numbers[i] + numbers.pop(i+1)
            operators.pop(i)
        else:
            i = i+1
    result = 1
    for n in numbers:
        result = result * n
    return result

# %%
result_list = []
for expression in lines:
    while True:
        ops = sorted(parse_parens(expression))
        level, start, end, exp = ops.pop()
        result = run_math_2(exp)
        expression = expression[0:start] + str(result) + expression[end:]
        if expression == str(result):
            print(result)
            result_list.append(result)
            break
# %%
sum(result_list)
# %%
