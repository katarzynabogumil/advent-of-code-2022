with open('input_data.txt', 'r') as input_data:
  rows = [line.strip() for line in input_data.readlines()]

def check_contain_1(a, b):
  for num in a:
    if num not in b:
      return 0
  return 1

def check_contain_2(a, b):
  for num in a:
    if num in b:
      return 1
  return 0

with open('input_data.txt', 'r') as input_data:
  rows = [line.strip() for line in input_data.readlines()]

counter_1 = 0
counter_2 = 0

for row in rows:
  sections = [[int(num) for num in section.split('-')] for section in row.split(',')]
  
  for i in [0,1]:
   sections[i] = [j for j in range (sections[i][0], sections[i][1] + 1)]

  if len(sections[0]) > len(sections[1]):
    counter_1 += check_contain_1(sections[1], sections[0])
    counter_2 += check_contain_2(sections[1], sections[0])
  else:
    counter_1 += check_contain_1(sections[0], sections[1])
    counter_2 += check_contain_2(sections[0], sections[1])

print('part 1:', counter_1)
print('part 2:', counter_2)
