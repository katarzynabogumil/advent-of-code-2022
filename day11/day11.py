from functools import reduce

class Monkey:
  def __init__(self, func, func_variable, devisible_test_value, a, b):
    self.items = []
    self.operation = func
    self.operation_var = func_variable
    self.test = devisible_test_value
    self.test_true = a
    self.test_false = b
    self.counter = 0


def main():
  monkeys = set_monkeys()

  magic_divide = reduce(lambda x, y: x * y, [monkey.test for monkey in monkeys.values()])

  round_limit = 10000 # 20 for part 1
  for _ in range(round_limit):
    for monkey in monkeys.values():
      for _ in range(len(monkey.items)):
        inspect(monkeys, monkey, magic_divide)

  max2_counter, max_counter = sorted([monkey.counter for monkey in monkeys.values()])[-2:]
  
  print(max_counter * max2_counter)


def inspect(monkeys, monkey, magic_divide):
  item = monkey.items[0]
  item = monkey.operation(item, monkey.operation_var)
  # item = item // 3 # for part 1
  item = item % magic_divide

  if item % monkey.test == 0:
    receiving_monkey = monkey.test_true
    monkeys[receiving_monkey].items.append(item)
  else:
    receiving_monkey = monkey.test_false
    monkeys[receiving_monkey].items.append(item)

  monkey.items.pop(0)
  monkey.counter += 1


def set_monkeys():
  monkeys = {}

  with open('input_data.txt', 'r') as input_data:
    rows = [line.strip() for line in input_data.readlines()]

  for i, row in enumerate(rows):
    if row.startswith('Monkey'):
      monkey_index = int(row[-2])
      starting_items = rows[i + 1][16:].split(', ')

      operation_line = rows[i + 2]
      try:
        operation_variable = int(operation_line.split(' ')[-1])
      except ValueError:
        operation_variable = None

      if operation_line.endswith('old * old'):
        def operation(x, y):
          return x * x
      elif '*' in operation_line:
        def operation(x, y):
          return x * y
      else:
        def operation(x, y):
          return x + y

      test_value = int(rows[i + 3].split(' ')[-1])
      test_true = int(rows[i + 4].split(' ')[-1])
      test_false = int(rows[i + 5].split(' ')[-1])

      monkey = Monkey(operation, operation_variable, test_value, test_true, test_false)
      for n in range(len(starting_items)):
        monkey.items.append(int(starting_items[n]))

      monkeys[monkey_index] = monkey

  return monkeys


if __name__ == "__main__":
    main()

