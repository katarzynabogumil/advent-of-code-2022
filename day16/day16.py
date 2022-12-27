class Valve:
  def __init__(self, name, flow_rate, tunnels):
    self.name = name
    self.flow_rate = flow_rate
    self.tunnels = tunnels
    self.connections = dict()

  def __str__(self):
    return f'Valve {self.name}, flow rate: {str(self.flow_rate)}, tunnels: {self.tunnels}, connections: {self.connections}'


class Step:
  def __init__(self, start, pressure, open_valves, visited):
    self.start = start
    self.pressure = pressure
    self.open_valves = open_valves
    self.visited = visited

  def __str__(self):
    return f'Step from {self.start}, pressure: {str(self.pressure)}, open: {self.open_valves}, visited: {self.visited}'


def main():
  with open('input_data.txt', 'r') as input_data:
    rows = [line.strip() for line in input_data.readlines()]

  valves = parse_input(rows)
  starting_point = 'AA'
  valves_to_open = find_valves_to_open(valves)
  
  # time_limit_p1 = 30
  # last_visited_p1 = [Step({1: {starting_point: 0}}, 0, {}, set())]
  # for i in range(time_limit_p1):
  #   last_visited_p1 = next_move(valves, i, time_limit_p1, last_visited_p1, valves_to_open, [])
  # print('part 1:', max([s.pressure for s in last_visited_p1]))
  
  time_limit_p2 = 26
  last_visited_p2 = [Step({1: {starting_point: 0}, 2: {starting_point: 0}}, 0, {}, set())]
  for i in range(time_limit_p2):
    last_visited_p2 = next_move(valves, i, time_limit_p2, last_visited_p2, valves_to_open, [])
  print('part 2:', max([s.pressure for s in last_visited_p2]))


def next_move(valves, time, time_limit, last_visited, valves_to_open, final_steps):
  next_steps = []
  max_pressure = max([s.pressure for s in last_visited])

  for step in last_visited:
    pressure = step.pressure + pressure_per_minute(valves, step)

    if set(valves_to_open).issubset(step.open_valves.keys()) or time == time_limit - 1 or not step.start:
      next_steps.append(Step(None, pressure, step.open_valves, step.visited))
    elif time > 7 and step.pressure < max_pressure * 0.5: # to speed up part2: estimated parameter
      pass
    elif time > 14 and step.pressure < max_pressure * 0.9: # to speed up part2: estimated parameter
      pass
    else:
      new_possible_starts = {}
      open_valves = step.open_valves.copy()
      for actor, actor_steps in step.start.items():
        for actor_start, time_when_free in actor_steps.items():
          new_possible_starts_per_actor = {}
          if time_when_free > time:
            new_possible_starts_per_actor[actor_start] = time_when_free
          elif actor_start not in open_valves.keys() and valves[actor_start].flow_rate != 0:
            open_valves[actor_start] = time
            new_possible_starts_per_actor[actor_start] = time + 1
          else:
            for valve, steps in valves[actor_start].connections.items():
              if steps != 0 and valve not in open_valves.keys() and valve not in step.visited:
                new_possible_starts_per_actor[valve] = time + steps
          if len(new_possible_starts_per_actor.keys()) != 0:
            new_possible_starts[len(new_possible_starts.keys()) + 1] = new_possible_starts_per_actor

      if len(new_possible_starts.keys()) == 2:
        pairs = set()
        for valve_1, time_1 in new_possible_starts[1].items():
          for valve_2, time_2 in new_possible_starts[2].items():
            pair = (valve_1, valve_2)
            if valve_1 != valve_2 and pair not in pairs and (valve_2, valve_1) not in pairs:
              pairs.add(pair)
              
              if time_1 >= time_limit and time_2 >= time_limit:
                new_start = None
              elif time_1 >= time_limit:
                new_start = {1: {valve_2: time_2}}
              elif time_2 >= time_limit:
                new_start = {1: {valve_1: time_1}}
              else:
                new_start = {1: {valve_1: time_1}, 2: {valve_2: time_2}}

              visited = step.visited.copy()
              visited.add(valve_1)
              visited.add(valve_2)
              next_steps.append(Step(new_start, pressure, open_valves, visited))

      elif len(new_possible_starts.keys()) != 0:
        for valve_1, time_1 in new_possible_starts[1].items():
          new_start = {1: {valve_1: time_1}} if time_1 < time_limit else None
          visited = step.visited.copy()
          visited.add(valve_1)
          next_steps.append(Step(new_start, pressure, open_valves, visited))

  return next_steps


def find_valves_to_open(valves):
  return [k for k, v in valves.items() if v.flow_rate != 0]


def pressure_per_minute(valves, step):
  pressure = sum([v.flow_rate for k, v in valves.items() if k in step.open_valves.keys()])
  return pressure


def parse_input(data):
  valves = dict()

  for line in data:
    parts = line.replace('Valve ', '').replace('has flow rate=', '').replace('tunnels lead to valves ', '').replace('tunnel leads to valve ', '').split('; ') 
    name, flow_rate = parts[0].split(' ')
    flow_rate = int(flow_rate)
    tunnels = parts[1].split(', ')
    valves[name] = Valve(name, flow_rate, tunnels)

  for k, v in valves.items():
    for tunnel in v.tunnels:
      check_distance(valves, 1, k, None, tunnel, [])

  return valves


def check_distance(valves, counter, start, last_tunnel, tunnel, checked):
  if counter <= len(valves.keys()):
    if valves[start].connections.get(tunnel, counter + 1) > counter:
      checked = [] if valves[start].connections.get(tunnel, 0) > counter else checked
      checked.append(tunnel)
      if valves[tunnel].flow_rate != 0:
        valves[start].connections[tunnel] = counter if start != tunnel else 0
      for further_tunnel in valves[tunnel].tunnels:
        if valves[start].connections.get(further_tunnel, counter + 1) > counter and further_tunnel != last_tunnel:
          check_distance(valves, counter + 1, start, tunnel, further_tunnel, checked)


if __name__ == "__main__":
    main()