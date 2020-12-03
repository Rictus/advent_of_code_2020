count_valid = 0
count_valid_2 = 0


def is_valid(line):
    global count_valid, count_valid_2
    policy, password = line.split(':')
    password = password.strip()
    minmax, letter = policy.split(' ')
    _min, _max = minmax.split('-')
    _max = int(_max)
    _min = int(_min)
    # _is_valid = _min <= password.count(letter) <= _max
    first_letter = password[_min - 1] == letter
    second_letter = password[_max - 1] == letter
    _is_valid_2 = (first_letter and not second_letter) or (second_letter and not first_letter)
    # count_valid = count_valid + 1 if _is_valid else count_valid
    count_valid_2 = count_valid_2 + 1 if _is_valid_2 else count_valid_2


lines = tuple(open('input', 'r'))
lines = map(lambda l: l.strip(), lines)
lines = map(is_valid, lines)
list(lines)
print(count_valid_2)
