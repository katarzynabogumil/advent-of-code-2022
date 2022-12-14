from json import loads

def main():
  with open('input_data.txt', 'r') as input_data:
    rows = [line.strip() for line in input_data.readlines()]

  right_indexes = check_right_order(rows)
  print('part 1:', sum(right_indexes))

  divider_packets = [[[2]], [[6]]]
  input_part_2 = [loads(row) for row in rows if len(row) != 0] + divider_packets
  sort_packets(input_part_2)
  index_1, index_2 = [input_part_2.index(i) + 1 for i in divider_packets]
  print('part 2:', index_1 * index_2)


def sort_packets(rows):
  changed = False
  for i in range(len(rows)-1):
    for j in range(0, len(rows)-i-1):
      if not compare_lists(rows[j], rows[j + 1]):
        rows[j], rows[j + 1] = rows[j + 1], rows[j]
        changed = True
    if not changed:
      return


def check_right_order(rows):
  right_order = []
  for i, row in enumerate(rows):
    if i % 3 == 0:
      if compare_lists(loads(row), loads(rows[i+1])):
        right_order.append(i//3 + 1)
  return right_order


def compare_lists(left, right):
  for i in range(len(left)):
    a = left[i]
    try:
      b = right[i]
    except IndexError:
      return 0

    result = compare_elements(a, b)
    if result in [1, 0]:
      return result

  # if there still are elements in right
  if len(right) > len(left):
    return 1


def compare_elements(a, b):
  # compare if both ints
  if isinstance(a, int) and isinstance(b, int):
    if a < b:
      return 1
    elif a > b:
      return 0
  else:
    # convert to lists
    if isinstance(a, list) and isinstance(b, list):
      pass
    elif isinstance(a, list):
      b = [b]
    else:
      a = [a]

    # check lists
    sub_result = compare_lists(a, b)
    if sub_result in [1, 0]:
      return sub_result


if __name__ == "__main__":
    main()

    