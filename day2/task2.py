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

def check_modify(lst):
    if check_list(lst): return True

    for i in range(len(lst)):
        if check_list(lst[:i] + lst[i+1:]): return True

    return False

def main(lists):
    safeListSum = 0
    for lst in lists:
        if check_modify(lst):
            safeListSum += 1
    return safeListSum


with open('input.csv') as f:
    lines = f.readlines()
    lists = [list(map(int, line.split(' '))) for line in lines]
    print(main(lists))


