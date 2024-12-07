def find_expression(total, numbers, current_expression=[], current_value=0):
    if not numbers:
        if current_value == total:
            return current_expression
        return False

    # Recursive case
    next_number = numbers[0]
    remaining_numbers = numbers[1:]

    # Addition
    result_addition = find_expression(
        total,
        remaining_numbers,
        current_expression + [f"+{next_number}"],
        current_value + next_number
    )
    if result_addition:
        return result_addition

    # Multiplication
    result_multiplication = find_expression(
        total,
        remaining_numbers,
        current_expression + [f"*{next_number}"],
        current_value * next_number if current_value != 0 else next_number 
    )
    if result_multiplication:
        return result_multiplication

    return False


def solve(total, numbers):
    solution = find_expression(total, numbers)
    if solution:
        return total
    return False


def parse(line):
    parts = line.split(': ')
    return int(parts[0]), parts[1]

with open('input.csv') as f:
    lines = f.read().split('\n')
    count = 0
    for line in lines:
        total, numbers = parse(line)

        numbers = [int(i) for i in numbers.split(' ')]
        correct = solve(total, numbers)
        if correct:
            print('Valid:', total)
            count += total

    print(count)