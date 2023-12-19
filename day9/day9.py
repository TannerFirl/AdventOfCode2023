import itertools
total = 0
total_p2 = 0
with open('day9/day9.txt') as f:
    for i, line in enumerate(f, start=1):
        all_nums = [[int(num) for num in line.strip().split(' ')]]
        while not all([num == 0 for num in all_nums[-1]]):
            all_nums.append([n2-n1 for n1, n2 in itertools.pairwise(all_nums[-1])])
        line_total = sum([nums[-1] for nums in all_nums])
        line_total_p2 = sum([((-1)**(row))*nums[0] for row, nums in enumerate(all_nums)])
        total += line_total
        total_p2 += line_total_p2
        print(f'line {i}: {line_total=} {line_total_p2=}')
print(f'Part 1 {total=}')
print(f'Part 2 {total_p2=}')

        