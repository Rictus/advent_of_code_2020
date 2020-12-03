slope = {
    'right': 7, 'down': 1
}

OPEN_SQUARE = '.'
TREE = '#'
filename = 'input'
grid = map(lambda l: list(l.strip()), tuple(open(filename, 'r')))
tree_count = 0
right_position = 0

skip = False

for idx, line in enumerate(grid):
    if slope['down'] == 2 and idx % 2 == 1:
        continue
    if line[right_position % len(line)] == TREE:
        tree_count += 1
    right_position += slope['right']
print('tree count = ', tree_count)

# Right 1, down 1.: 70
# Right 3, down 1.: 171
# Right 5, down 1.: 48
# Right 7, down 1.: 60
# Right 1, down 2.: 35 trees
print(70 * 171 * 48 * 60 * 35)
