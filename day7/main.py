def parse_containing_bag(_str):
    count = int(_str[0])
    if _str[-1] == 's':
        _str = _str[:-1]  # remove plurial
    _str = _str.strip()[2:-4]  # remove the beginning integer and the end " bag"
    return count, _str


def get_rules():
    _rules = {}

    for line in tuple(open('input', 'r')):
        color, contain = line.split(' bags contain ')
        if contain[:2] == 'no':
            containing_bags = []
        else:
            containing_bags = contain.strip()[:-1].split(', ')
            containing_bags = list(map(parse_containing_bag, containing_bags))
        _rules[color] = containing_bags

    return _rules


def get_bags_containing(bags, my_bag):
    bags_containing_my_bag = set()
    # How many bags can directly contain my_bag ?
    for r in bags:
        containing_bags = bags[r]
        if any(b == my_bag for a, b in containing_bags):
            bags_containing_my_bag.add(r)
    return bags_containing_my_bag


MY_BAG = 'shiny gold'
rules = get_rules()


def first_part_of_problem():
    # = Bags directly containing MY_BAG
    contain = get_bags_containing(rules, MY_BAG)
    answer_bags = set(contain)

    for _ in range(10):
        # Which bags contain one of {contain} ?
        intermediate_results = set()
        for bag_name in contain:
            intermediate_results |= get_bags_containing(rules, bag_name)
        answer_bags |= intermediate_results
        contain = intermediate_results
    print(answer_bags)
    print(len(answer_bags))


def count_bag(key):
    global rules
    if len(rules[key]) == 0:
        return 0

    global_count = 0
    for bag in rules[key]:
        count, name = bag
        child_count = count_bag(name) + 1
        global_count += (count * child_count)
    return global_count


def second_part_of_problem():
    print(count_bag(MY_BAG))


second_part_of_problem()
