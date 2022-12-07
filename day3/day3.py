from string import ascii_lowercase, ascii_uppercase

with open('input_data.txt', 'r') as input_data:
  rows = [line.strip() for line in input_data.readlines()]

counter = 0

for row in rows:
  row = row.strip()
  first = set(row[:len(row)//2])
  second = set(row[len(row)//2:])

  item = first.intersection(second).pop()

  if item in ascii_lowercase:
    counter += ord(item) - 96
  elif item in ascii_uppercase:
    counter += ord(item) - 38

print('part 1:', counter)

counter = 0

for i in range(0,len(rows)-2,3):
  first = set(rows[i].strip())
  second = set(rows[i+1].strip())
  third = set(rows[i+2].strip())
  badge = first.intersection(second).intersection(third).pop()

  if badge in ascii_lowercase:
    counter += ord(badge) - 96
  elif badge in ascii_uppercase:
    counter += ord(badge) - 38

print('part 2:', counter)
