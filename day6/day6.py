import math
import re
# Use the quadratic formula to get lower/upper bounds on hold times
# producing winning results
def get_lower_upper_win_holds(time, dist):
    lower = math.ceil((time - (time**2 - 4*1*dist)**.5)/(2*1))
    # must be > distance
    if dist == (time-lower)*lower:
        lower += 1
    upper = int((time + (time**2 - 4*1*dist)**.5)/(2*1))
    # must be > distance
    if dist == (time-upper)*upper:
        upper -= 1
    return lower, upper

times = []
dists = []
with open('day6/day6.txt') as f:
    times = [int(num) for num in re.split(r'\s+', next(f).split(':')[1].strip())]
    dists = [int(num) for num in re.split(r'\s+', next(f).split(':')[1].strip())]
# print(times)
# print(dists)
total_wins = 1
for time, dist in zip(times, dists):
    lower, upper = get_lower_upper_win_holds(time, dist)
    wins = upper-lower+1
    # print(f'{lower=} {upper=} {wins=}')
    total_wins *= wins
print(f'{total_wins=}') 

with open('day6/day6.txt') as f:
    time = int(''.join(next(f).split(':')[1].split()))
    dist = int(''.join(next(f).split(':')[1].split()))
    lower, upper = get_lower_upper_win_holds(time, dist)
    total_wins = upper-lower+1
    print(f'{total_wins=}')


# dist = (time-hold_time)*hold_time
# 244 = (41-hold_time)*hold_time
# hold_time**2 - 41*hold_time + 244 = 0
# hold_time = (41 + (41**2-4*1*244)**.5)/2*1
# hold_time = (41 - (41**2-4*1*244)**.5)/2*1

#dist = time*hold_time - hold_time**2
#hold_time**2 - time*hold_time - dist = 0