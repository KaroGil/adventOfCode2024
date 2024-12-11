def bitChange(number):
    if number == 0:
        return 1
    
def evenLength(number):
    if len(number) % 2 == 0:
        left = number[:len(number) // 2]
        right = number[len(number) // 2:]
        return int(left), int(right)
def rest(number):
    return number * 2024

def blink(numbers):
    result = []
    for number in numbers:
        if number == 0:
            result.append(bitChange(number))
        elif len(str(number)) % 2 == 0:
            result.append(evenLength(str(number))[0])
            result.append(evenLength(str(number))[1])
        else:
            result.append(rest(number))

    return result

with open('input.csv', 'r') as file:
    data = file.read().split(' ')
    numbers = [int(number) for number in data]
    print(numbers)
    for i in range(25):
        numbers = blink(numbers)
        print(f'Blink {i + 1}')
print(f'Final number of stones: {len(numbers)}')