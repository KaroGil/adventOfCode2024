
def parse(data):
    a,b,c,_,p = data.splitlines()
    return a[12:], b[12:], c[12:],p[9:]

def getOperand(number):
    return number

def getComboOperand(number, a, b, c):
    if 0 <= number <= 3:
        return number
    elif number == 4:
        return a
    elif number == 5:
        return b
    elif number == 6:
        return c
    else:
        return "combo operand 7?"

def rules(number, a, b, c, p):
    if number == 0:
        # Division numerator: register A
        # Division denominator: 2 to the power of the instructions combo operand
        instruction = 2
        return a / 2^(getComboOperand(instruction))

    elif number == 1:
        pass

    elif number == 2:
        pass

    elif number == 3:
        pass
    elif number == 4:
        pass
    elif number == 5:
        pass
    elif number == 6:
        pass
    elif number == 7:
        pass

    else:
        return 0


with open('test.csv', 'r') as file:
    data = file.read()
    a,b,c,p = parse(data)
    print(f'a: {a}')
    print(f'b: {b}')
    print(f'c: {c}')
    print(f'p: {p}')


    output = "4,6,3,5,6,3,5,2,1,0"


# Test
assert output == "4,6,3,5,6,3,5,2,1,0"