print('Part 1')
MAX_RGB = [12,13,14]
id_sum = 0
with open('day2.txt') as f:
    for line in f:
        id_str, games = line.split(':')
        id_val = int(id_str[5:])
        rgb = [0,0,0]
        val = 0
        for c in games:
            if c.isdigit():
                val = 10*val + int(c)
            elif c is 'r' and val is not 0:
                rgb[0] = val
                val = 0
            elif c is 'g' and val is not 0:
                rgb[1] = val
                val = 0
            elif c is 'b' and val is not 0:
                rgb[2] = val
                val = 0
            elif c is ';' or c is '\n':
                possible = all(this<=limit for this,limit in zip(rgb,MAX_RGB))
                if not possible:
                    break
                if c is '\n':
                    id_sum += id_val
                val = 0
                rgb = [0, 0, 0]
print(id_sum)

print('Part 2')
power_sum = 0
with open('day2.txt') as f:
    for line in f:
        games = line.split(':')[1]
        max_rgb = [0,0,0]
        this_rgb = [0,0,0]
        val = 0
        for c in games:
            if c.isdigit():
                val = 10*val + int(c)
            elif c is 'r' and val is not 0:
                this_rgb[0] = val
                val = 0
            elif c is 'g' and val is not 0:
                this_rgb[1] = val
                val = 0
            elif c is 'b' and val is not 0:
                this_rgb[2] = val
                val = 0
            elif c is ';' or c is '\n':
                max_rgb = [max(old, new) for old, new in zip(max_rgb, this_rgb)]
                val = 0
                this_rgb = [0, 0, 0]
                # Make sure there is \n at the end of the last line of your file!
                if c is '\n':
                    power_sum += max_rgb[0]*max_rgb[1]*max_rgb[2]
print(power_sum)
        
