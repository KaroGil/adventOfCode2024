from functools import lru_cache

def parse(data):
    # Split the data by spaces and convert each number to an integer
    return [int(number) for number in data.split(' ')]

def evenLength(number):
    # Split the number in half
    strNumber = str(number)
    half_l = len(strNumber) // 2
    left = strNumber[:half_l]
    right = strNumber[half_l:]
    return int(left), int(right)

@lru_cache(None) # Cache results for memoization
def blink(number, iterations):
    if iterations == 0: # Base case
        return 1

    if number == 0: # If number is 0, return 1
        return blink(1, iterations - 1)

    strNumber = str(number)
    if len(strNumber) % 2 == 0: # If number has even length, split it
        return blink(evenLength(strNumber)[0], iterations - 1) + blink(evenLength(strNumber)[1], iterations - 1)

    # Else multiply it by 2024
    return blink(number * 2024, iterations - 1)


with open('input.csv', 'r') as file:
    data = file.read()
    numbers = parse(data)
    print(numbers)
    total_count = 0
    for number in numbers: # For each number, calculate the number of stones
        total_count += blink(number, 75)
    
    print(f'Final number of stones: {total_count}')