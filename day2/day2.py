with open('input_data.txt', 'r') as input_data:
  rows = [line.strip() for line in input_data.readlines()]

# Part 1
def game_p1(first, second):
  if first == 'A':
    if second == 'X':
      return 3
    elif second == 'Y':
      return 6
    elif second == 'Z':
      return 0
  elif first == 'B':
    if second == 'X':
      return 0
    elif second == 'Y':
      return 3
    elif second == 'Z':
      return 6
  elif first == 'C':
    if second == 'X':
      return 6
    elif second == 'Y':
      return 0
    elif second == 'Z':
      return 3

round_score = 0
total_score = 0

for row in rows:
  opponents_choice = row[0]
  your_choice = row[2]

  result = game_p1(opponents_choice, your_choice)
  round_score += result

  # add shape score
  if your_choice == 'X':
    round_score += 1
  elif your_choice == 'Y':
    round_score += 2
  elif your_choice == 'Z':
    round_score += 3

  total_score += round_score
  round_score = 0

print('part 1:', total_score)

# Part 2
def game_p2(first, second):
  if second == 'X':
    result = 0
  elif second == 'Y':
    result = 3
  elif second == 'Z':
    result = 6
  
  if first == 'A':
    if second == 'X':
      result += 3  
    elif second == 'Y':
      result += 1  
    elif second == 'Z':
      result += 2  
  elif first == 'B':
    if second == 'X':
      result += 1  
    elif second == 'Y':
      result += 2  
    elif second == 'Z':
      result += 3  
  elif first == 'C':
    if second == 'X':
      result += 2  
    elif second == 'Y':
      result += 3  
    elif second == 'Z':
      result += 1  

  return result

round_score = 0
total_score = 0

for row in rows:
  opponents_choice = row[0]
  condition = row[2]

  result = game_p2(opponents_choice, condition)
  round_score += result

  total_score += round_score
  round_score = 0


print('part 2:', total_score)
