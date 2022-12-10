def main():
  with open('input_data.txt', 'r') as input_data:
    rows = [line.strip().split(' ') for line in input_data.readlines()]

  cycle_count = 0
  counter = 1
  strengths = []

  for row in rows:
    if row[0] == 'noop':
      cycle_count = add_check_cycles(cycle_count, counter, strengths)
    else:
      cycle_count = add_check_cycles(cycle_count, counter, strengths)
      cycle_count = add_check_cycles(cycle_count, counter, strengths)
      counter += int(row[1])
  
  print('part 1:', sum(strengths))


def draw_cycles(cycle_count, position):
  sprite = [i % 40 for i in [position - 1, position, position + 1]]
  if cycle_count % 40 in sprite:
    print('#', end='')
  else:
    print('.', end='')
  if cycle_count in [i for i in range(39, 240, 40)]:
    print('')


def add_check_cycles(cycle_count, counter, strengths):
  draw_cycles(cycle_count, counter) # only for part 2
  cycle_count += 1
  if cycle_count in [i for i in range(20, 221, 40)]:
    strengths.append(cycle_count * counter)
  return cycle_count


if __name__ == "__main__":
    main()

