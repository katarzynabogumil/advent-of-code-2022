def sum_dir(idx):
  sum = 0 
  while True:
    row = rows[idx]
    try:
      sum += int(row.split(' ')[0])
    except ValueError:
      pass
    # if sub directory:
    if row[:5] == '$ cd ' and row != '$ cd ..': 
      sub_dir = sum_dir(idx+1)
      sub_sum = sub_dir[0]
      idx = sub_dir[1]
      dir_sums.append(sub_sum)
      sum += sub_sum
    if row == '$ cd ..' or idx == len(rows)-1:
      return (sum, idx)
    idx += 1  
      
with open('input_data.txt', 'r') as input_data:
  rows = [line.strip() for line in input_data.readlines()]

dir_sums = []
dir_sums.append(sum_dir(1)[0])
print('part 1:', sum([x for x in dir_sums if x <= 100000]))

free_space = 70000000 - dir_sums[-1]
needed_space = 30000000 - free_space
print('part 2:', min([x for x in dir_sums if x >= needed_space]))