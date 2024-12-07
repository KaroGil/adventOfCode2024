def parse(line):
    parts = line.split(': ')
    return int(parts[0]), parts[1]


def checkInput(line):
    total, numbers = parse(line)
    numbers = [int(i) for i in numbers.split(' ')]
    count = 0
    if sum(numbers) == total:
        print('Valid:', line)
        return True

    for number in numbers:
        if number + count <= total:
            count += number
            if count == total:
                print('Valid:', line)
                return True
        else:
            break
    
    print('Invalid:', line)
    return False
    
def checkNumber(total, numbers):
    for i in range(len(numbers)):
        if total % numbers[i] == 0: # The number is a factor of the total
            return True
    return False

with open('test.csv') as f:
    lines = f.read().split('\n')
    print(lines)
    for line in lines:
        print(checkInput(line))