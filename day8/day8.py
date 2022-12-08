def is_visible(x, y):
  height = int(rows[y][x])
  row = [int(i) for i in rows[y]]
  column = []
  for i in range(size_y):
    column.append(int(rows[i][x]))

  if x in [0, size_x - 1] or y in [0, size_y - 1]:
    return True
  elif height > max(row[:x]) or height > max(row[x+1:size_x]):
    return True
  elif height > max(column[:y]) or height > max(column[y+1:size_y]):
    return True
  return False


def check_score(x, y):
  height = int(rows[y][x])
  counter_left, counter_right, counter_up, counter_down = [0, 0, 0, 0]
  
  # checking left
  for i in range(x - 1, -1, -1):
    if height > int(rows[y][i]):
      counter_left += 1
    else:
      counter_left += 1
      break
  
  # checking right
  for i in range(1, size_x - x):
    if x == (size_x - 1):
      break
    if height > int(rows[y][x + i]):
      counter_right += 1
    else:
      counter_right += 1
      break

  # checking up
  for i in range(y - 1, -1, -1):
    if height > int(rows[i][x]):
      counter_up += 1
    else:
      counter_up += 1
      break
  
  # checking down
  for i in range(1, size_y - y):
    if y == size_y - 1:
      break
    if height > int(rows[y + i][x]):
      counter_down += 1
    else:
      counter_down += 1
      break

  return counter_left * counter_right * counter_up * counter_down


with open('input_data.txt', 'r') as input_data:
  rows = [line.strip() for line in input_data.readlines()]

size_x = len(rows[0])
size_y = len(rows)

counter = 0
scenic_scores = []

for y, row in enumerate(rows):
  for x, height in enumerate(row):
    if is_visible(x, y):
      counter += 1
      scenic_scores.append(check_score(x, y))

print('part 1:', counter)
print('part 2:', max(scenic_scores))