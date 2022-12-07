with open('input_data.txt', 'r') as input_data:
  data = [line.strip() for line in input_data.read()]

n = 14 # marker length (part1 = 4, part2 = 14)
check = []
for i in range(len(data)):
  if data[i] not in check:
    check.append(data[i])
  if i >= n:
    recent_data = [data[i - j] for j in range(1, n)]
    if data[i - n] in check and data[i - n] not in recent_data:
      check.remove(data[i - n])
    if len(check) == n:
      result = i + 1
      break

print(result)