with open('input_data.txt', 'r') as input_data:
  rows = [line.strip() for line in input_data.readlines()]

counter = 0
max1 = 0
max2 = 0
max3 = 0

for row in rows:
  if row == '':
    if counter > max1:
      max1 = counter
    elif counter > max2:
      max2 = counter
    elif counter > max3:
      max3 = counter
    counter = 0
  else:
    counter += int(row)

print(max1, max2, max3)
print(max1 + max2 + max3)
