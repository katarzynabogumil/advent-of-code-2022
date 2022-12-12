def main():
  with open('input_data.txt', 'r') as input_data:
    rows = [line.strip() for line in input_data.readlines()]

  start_p1 = find_start(rows, 'S')
  start_p2 = find_start(rows, 'a')

  print('part 1:', find_shortest_way(rows, start_p1))
  print('part 2:', find_shortest_way(rows, start_p2))


def find_shortest_way(grid, starting_points):
  counter = 0
  previous_steps = set(starting_points)
  possible_routes = {0: set(starting_points)}

  while True:
    counter += 1
    found_E = find_next_steps(grid, possible_routes, counter, previous_steps)

    if found_E:
      return max(possible_routes.keys())
    elif not possible_routes[counter]:
      return 'no E found'


def find_next_steps(grid, routes, step, previous_steps):
  positions = routes[step - 1]
  next_steps = set()
  if_found = False

  for start in positions:
    a, b = start
    start_value = grid[b][a]
    if start_value == 'S':
      start_value = '`'
    for x in [max(a - 1, 0), a, min(a + 1, len(grid[0]) - 1)]:
      for y in [max(b - 1, 0), b, min(b + 1, len(grid) - 1)]:
        next_step = (x, y)
        next_value = grid[y][x]
        if next_step in previous_steps:
          pass
        elif x != a and y != b:
          pass
        elif start_value == 'z' and next_value == 'E':
          next_steps.add(next_step)
          if_found = True
        elif ord(next_value) > 96 and ord(next_value) <= ord(start_value) + 1:
          next_steps.add(next_step)
          previous_steps.add(next_step)
          
  routes[step] = next_steps
  return if_found


def find_start(grid, n):
  points = []
  for y, row in enumerate(grid):
    for x, value in enumerate(row):
      if value == n:
        points.append((x, y))
  return points


if __name__ == "__main__":
    main()

