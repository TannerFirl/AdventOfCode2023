print('Part 1')
s = 0
with open('day1.txt') as f:
    for line in f:
            s2 = '' 
            for c in line:
                    if c in ['0','1','2','3','4','5','6','7', '8', '9']:
                            s2 += c
                            break
            for c in reversed(line):
                    if c in ['0','1','2','3','4','5','6','7', '8', '9']:
                            s2 += c
                            break
            if len(s2) != 2:
                print('ruh roh: {line}')
            s += int(s2)
print(s)

print('Part 2')
import re
s = 0
MATCHR = r"([0-9]|one|two|three|four|five|six|seven|eight|nine)"
R_MATCHR = r"([0-9]|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)"
d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
MATCHR = '([0-9]|' + '|'.join([el for el in d]) + ')'
R_MATCHR = '([0-9]|' + '|'.join([el[::-1] for el in d]) + ')'

with open('day1.txt') as f:
    for line in f:
        line = line[:-1]
        matchd = re.search(MATCHR, line)
        s2 = str(d.get(matchd.group(1), matchd.group(1)))
        matchd = re.search(R_MATCHR, line[::-1])
        s2 += str(d.get(matchd.group(1)[::-1], matchd.group(1)))

        if len(s2) != 2:
                print('ruh roh: {line}')
        s += int(s2)

print(s)


