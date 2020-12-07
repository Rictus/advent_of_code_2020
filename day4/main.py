import re

valid_dicts = 0
current_dict = None


def is_valid(passport_dict):
    test = 'ecl' in passport_dict and \
           'pid' in passport_dict and \
           'eyr' in passport_dict and \
           'hcl' in passport_dict and \
           'byr' in passport_dict and \
           'iyr' in passport_dict and \
           'hgt' in passport_dict
    if not test:
        return False
    if 'byr' in passport_dict:
        passport_dict['byr'] = int(passport_dict['byr'])
        test = test and 1920 <= passport_dict['byr'] <= 2002

    if 'iyr' in passport_dict:
        passport_dict['iyr'] = int(passport_dict['iyr'])
        test = test and 2010 <= passport_dict['iyr'] <= 2020

    if 'eyr' in passport_dict:
        passport_dict['eyr'] = int(passport_dict['eyr'])
        test = test and 2020 <= passport_dict['eyr'] <= 2030

    if 'hgt' in passport_dict and passport_dict['hgt'].endswith('cm'):
        test = test and 150 <= int(passport_dict['hgt'].split('cm')[0]) <= 193
    elif 'hgt' in passport_dict and passport_dict['hgt'].endswith('in'):
        test = test and 59 <= int(passport_dict['hgt'].split('in')[0]) <= 76
    else:
        return False
    test = test and passport_dict['hcl'] and re.match(r'^#[a-zA-Z0-9]{6}$', passport_dict['hcl'])
    test = test and passport_dict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    test = test and re.match(r'^\d{9}$', passport_dict['pid'])
    return test


for line in tuple(open('input', 'r')):
    if len(line.strip()) > 0:
        if current_dict is None:
            current_dict = dict(map(lambda x: x.split(':'), line.strip().split(' ')))
        else:
            current_dict = {**current_dict, **dict(map(lambda x: x.split(':'), line.strip().split(' ')))}
    else:
        valid_dicts += 1 if is_valid(current_dict) else 0
        current_dict = None

valid_dicts += 1 if is_valid(current_dict) else 0
current_dict = None

print(valid_dicts)
