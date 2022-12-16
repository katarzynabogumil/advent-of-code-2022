from math import inf

def main():
  with open('input_data.txt', 'r') as input_data:
    rows = [line.strip() for line in input_data.readlines()]

  sensors = parse_input(rows)
  checked_points = get_row_coverage(sensors, 2000000)
  print('part 1:', checked_points)

  search_range = (0, 4000000)
  (x, y) = beacon_search(sensors, search_range)
  frequency = x * 4000000 + y
  print('part 2:', frequency)


def beacon_search(data, search_range):
  for row in range(search_range[0], search_range[1] + 1):
    checked_x = get_row_coverage(data, row, search_range)
    if checked_x:
      return (checked_x, row)


def get_row_coverage(data, row, search_range=None):
  checked_ranges = []

  for sensor, beacon in data:
    x, y = sensor
    a, b = beacon
    distance = abs(b - y) + abs(a - x)
    if row >= (y - distance) and row <= (y + distance):
      distance_x = distance - abs(y - row)
      x_min = x - distance_x
      x_max = x + distance_x
      checked_ranges.append([x_min, x_max])

  sorted(checked_ranges)
  sum_accumulator = 0
  right_edge_accumulator = -inf 
  for integer_range in sorted(checked_ranges):
    left_edge = max(integer_range[0], right_edge_accumulator +1)
    right_edge = integer_range[1]

    if not search_range:
      sum_accumulator += max(0, right_edge - left_edge + 1)
    else:
      if left_edge == right_edge_accumulator + 2 and left_edge < search_range[1] and right_edge_accumulator > search_range[0]:
        return left_edge - 1
    
    right_edge_accumulator = max(right_edge, right_edge_accumulator)

  if not search_range:
    for beacon in {beacon for sensor, beacon in data}:
      if beacon[1] == row:
        sum_accumulator -= 1
    return sum_accumulator
  else:
    return 0


def parse_input(data):
  sensors = []

  for line in data:
    lines = line.split(': ')
    sensor = lines[0].replace('Sensor at x=', '').split(', y=')
    sensor_tuple = (int(sensor[0]), int(sensor[1]))
    beacon = lines[1].replace('closest beacon is at x=', '').split(', y=')
    beacon_tuple = (int(beacon[0]), int(beacon[1]))
    sensors.append([sensor_tuple, beacon_tuple])

  return sensors


if __name__ == "__main__":
  main()