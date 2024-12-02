def differ(list):
    sum = 0
    for i in range(len(list)-1):
        diff = abs(list[i] - list[i+1])
        if not(diff > 3 or diff < 1): sum += 1
    if sum == len(list)-1: return True
    else: return False


def checkDecrease(list):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]: return False
    return True

def checkIncrease(list):
    for i in range(len(list) - 1):
        if list[i] < list[i + 1]: return False
    return True

def checkList(list):
        if (checkDecrease(list) or checkIncrease(list)) and differ(list): return True
        else: return False


def main(lists):
    safeListSum = 0
    for list in lists:
        if checkList(list):
            safeListSum += 1

    return safeListSum


with open('input.csv') as f:
    lines = f.readlines()
    lists = [list(map(int, line.split(' '))) for line in lines]
    print(main(lists))


# diff solution
def is_increasing(lst):
    return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))
def is_decreasing(lst):
    return all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))

def check_order(lst):
    return is_increasing(lst) or is_decreasing(lst)

def check_diff(lst):
    return all(abs(lst[i] - lst[i + 1]) in {1, 2, 3} for i in range(len(lst) - 1))

def check_list(lst):
    return check_order(lst) and check_diff(lst)

def main(lists):
    safeListSum = 0
    for lst in lists:
        if check_list(lst):
            safeListSum += 1

    return safeListSum


with open('input.csv') as f:
    lines = f.readlines()
    lists = [list(map(int, line.split(' '))) for line in lines]
    print(main(lists))