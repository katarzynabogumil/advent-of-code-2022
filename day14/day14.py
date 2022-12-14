def main():
  with open('input_data.txt', 'r') as input_data:
    rows = [line.strip().split(' -> ') for line in input_data.readlines()]
  
  rocks = set_rocks(rows)
  lowest_rock = find_lowest(rocks)

  print('part 1:', sand_unit_counter(rocks, lowest_rock, 1))
  print('part 2:', sand_unit_counter(rocks, lowest_rock + 2, 2) + 1)


def sand_unit_counter(rocks, lowest, part):
  start = (500, 0)
  counter = 0
  sand = rocks.copy()
  while True:
    if move(sand, start, lowest, part):
      break
    counter += 1
  return counter


def move(sand, start, lowest, part):
  x, y = start
  if part == 1 and y > lowest:
    return 1
  elif part == 2 and (y + 1) == (lowest):
    sand.add(start)
  elif (x, y + 1) not in sand:
    if move(sand, (x, y + 1), lowest, part):
      return 1
  elif (x - 1, y + 1) not in sand:
    if move(sand, (x - 1, y + 1), lowest, part):
      return 1
  elif (x + 1, y + 1) not in sand:
    if move(sand, (x + 1, y + 1), lowest, part):
      return 1
  else:
    sand.add(start)
    if start == (500, 0):
      return 1


def find_lowest(points):
  lowest_point = None

  for point in points:
    if not lowest_point:
      _, lowest_point = point
    _, y = point
    if y > lowest_point:
      lowest_point = y

  return lowest_point


def set_rocks(data):
  rocks = set()

  for line in data:
    last_point = None
    for point in line:
      point = point.split(',')
      x, y = int(point[0]), int(point[1])
      point = (x, y)
      rocks.add(point)
      if last_point:
        x_last, y_last = last_point
        if x_last != x:
          dif_x = x_last - x
          for i in range(abs(dif_x)):
            vector = dif_x // abs(dif_x)
            rocks.add((x + (i * vector), y))
        elif y_last != y:
          dif_y = y_last - y
          for i in range(abs(dif_y)):
            vector = dif_y // abs(dif_y)
            rocks.add((x, y + (i * vector)))
      last_point = point

  return rocks


if __name__ == "__main__":
  main()