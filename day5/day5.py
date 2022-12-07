def crane_1(x, a, b):
  for i in range(x):
      stacks[b].append(stacks[a].pop())

def crane_2(x, a, b):
  stacks[b].extend(stacks[a][-x:])
  stacks[a] = stacks[a][:-x]

with open('input_data.txt', 'r') as input_data:
  rows = [line for line in input_data.readlines()]

for row in rows:
  if row[1] == '1':
    stacks = [[] for i in range(int(row.strip()[-1]))]
    break

for row in rows:
  if row[0] == 'm':
    row = row.strip().split(' ')
    amount, st_from, st_to = [int(n) for n in row if n.isnumeric()]
    # crane_1(amount, st_from-1, st_to-1) # part 1
    crane_2(amount, st_from-1, st_to-1) # part 2
  else:
    for i in range(len(row)):
      if row[i].isalpha():
        stacks[(i-1)//4].insert(0,row[i])
        
result = [stack.pop() for stack in stacks]
print(''.join(result))
