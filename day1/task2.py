example1 = [3,4,2,1,3,3]
example2 = [4,3,5,3,9,3]

def score(number, list):
    return list.count(number)

def main(list1,list2):
    finalScore = 0
    for i in list1:
        finalScore += (score(i, list2) * i)
    return finalScore

with open('./input.csv', 'r') as f:
    data = f.read().splitlines()
    l = [i.split("  ") for i in data]

    list1 = [int(i[0]) for i in l]
    list2 = [int(i[1]) for i in l]
    print(main(list1, list2))

print(main(example1, example2)) 