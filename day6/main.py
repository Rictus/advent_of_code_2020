from functools import reduce

all_groups_data = []

current_group = {
    'answers': []
}

for line in open('test_input', 'r'):
    line = line.strip()
    if len(line) > 0:
        current_group['answers'].append(line)
    else:
        all_groups_data.append(current_group)
        current_group = {'answers': []}
all_groups_data.append(current_group)


def part_1():
    global all_groups_data
    sum_count_questions = 0

    for idx, group in enumerate(all_groups_data):
        all_groups_data[idx]['count_questions'] = len(set(''.join(group['answers'])))
        sum_count_questions += all_groups_data[idx]['count_questions']

    print(all_groups_data)
    print(sum_count_questions)


def part_2():
    global all_groups_data
    sum_count_questions = 0

    for idx, group in enumerate(all_groups_data):
        all_groups_data[idx]['answers'] = list(map(set, all_groups_data[idx]['answers']))
        all_groups_data[idx]['count_questions'] = len(reduce(lambda x, y: x & y, all_groups_data[idx]['answers']))
        sum_count_questions += all_groups_data[idx]['count_questions']

    print(all_groups_data)
    print(sum_count_questions)

part_2()
