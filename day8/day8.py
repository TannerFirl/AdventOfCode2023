import re
import sys
MAP_MATCHR = re.compile(r'(\S+) = \(([^,]+), ([^)]+)\)')
network = {}
instructions = ''
nodes = []
with open('day8/day8.txt') as f:
    instructions = next(f).strip()
    print(f'{instructions=}')
    next(f)
    for line in f:
        match = MAP_MATCHR.match(line.strip())
        if match is None:
            print(f'Failed to match {line=}')
            sys.exit(1)
        network[match.group(1)] = (match.group(2), match.group(3))
        # for part 2
        if match.group(1)[-1] == 'A':
            nodes.append(match.group(1))
node = 'AAA'
idx = 0
instruction_len = len(instructions)
steps = 0
while node != 'ZZZ':
    node = network[node][0] if instructions[idx] == 'L' else network[node][1]
    idx +=1
    steps += 1
    if idx == instruction_len:
        idx = 0
print(f'{steps=}')

print('Part 2')
from collections import defaultdict

print(f'{nodes=}')
steps = 0
# while any([node[-1] != 'Z' for node in nodes]):
#     for i in range(len(nodes)):
#         nodes[i] = network[nodes[i]][0] if instructions[idx] == 'L' else network[nodes[i]][1]
#     idx += 1
#     steps += 1
#     if idx == instruction_len:
#         idx = 0
print(instruction_len)
instr_to_node = [[] for i in range(instruction_len)]
node_to_offset_period = {}
while nodes:
    pop_idxs = []
    for i in range(len(nodes)):
        instruction_idx = steps % instruction_len
        next_node = network[nodes[i]][0] if instructions[idx] == 'L' else network[nodes[i]][1]
        # print(instr_to_node, instruction_idx)
        if next_node in instr_to_node[instruction_idx]:
            pop_idxs.append(i)
            # offset = instruction_idx + instruction_len*instr_to_node[instruction_idx].index(next_node)
            # period = instruction_len*(len(instr_to_node[instruction_idx]) - instr_to_node[instruction_idx].index(next_node))
            # node_to_offset_period[i] = (offset, period)
        else:
            instr_to_node[instruction_idx].append(next_node)
            nodes[i] = next_node
    for idx in pop_idxs:
        nodes.pop(idx)
    steps += 1
    idx += 1
    if idx == instruction_len:
        idx = 0
print(f'{node_to_offset_period}')

# offset_cycles = []
# for node in nodes:
#     traversed_nodes

