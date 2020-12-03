integers = tuple(open('input', 'r'))
integers = map(lambda x: int(x.strip()), integers)
integers = sorted(integers)
print(integers)

for x in integers:
    for y in integers:
        for z in integers:
            if x + y + z == 2020:
                print(f'{x} + {y} + {z} = 2020.  {x}*{y}*{z}={z*x * y}')
