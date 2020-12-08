from copy import deepcopy



def read_file():
    _instructions = []
    for idx, line in enumerate(open('input')):
        instruction, value = line.strip().split(' ')

        value = int(value[1:]) if value[0] == '+' else -int(value[1:])
        _instructions.append({'line_number': idx, 'instruction': instruction, 'value': value, 'read': False})
    return _instructions


def run_instructions(instructions):
    ACCUMULATOR = 0
    terminates_correctly = True  # meaning without infinite loops
    current_instruction_index = 0
    while current_instruction_index < len(instructions):
        inst = instructions[current_instruction_index]
        instruction = inst['instruction']
        value = inst['value']

        if inst['read']:
            terminates_correctly = False
            break
        else:
            instructions[current_instruction_index]['read'] = True

        if instruction == 'nop':
            current_instruction_index += 1
        elif instruction == 'acc':
            ACCUMULATOR += value
            current_instruction_index += 1
        elif instruction == 'jmp':
            current_instruction_index += value
        else:
            raise ValueError(f'Unknown instruction "{instruction}" with value "{value}".')
    return ACCUMULATOR, terminates_correctly


def fix_and_run():
    instructions = read_file()
    for idx, inst in enumerate(instructions):
        copied_instructions = deepcopy(instructions)
        if inst['instruction'] == 'nop':
            copied_instructions[idx]['instruction'] = 'jmp'
        else:
            copied_instructions[idx]['instruction'] = 'nop'
        accumulator, terminated_correctly = run_instructions(copied_instructions)
        if terminated_correctly:
            print('Updated following instructrion')
            print(inst)
            print(accumulator)


fix_and_run()
