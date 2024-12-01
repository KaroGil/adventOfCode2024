
def distance(dist1, dist2):
    return abs(abs(dist1) - abs(dist2))

def findSmallest(list):
    smallest = min(list)
    list.remove(smallest)
    return smallest

def main(list1, list2):
    totalDistance = 0
    for i in range(max(len(list1), len(list2))):
        # Find smallest in both list
        smallest1 = findSmallest(list1)
        smallest2 = findSmallest(list2)
        # Find the distance
        totalDistance += distance(smallest1, smallest2)

    return totalDistance

#print(main([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])) # 0

with open('./input.csv', 'r') as f:
    data = f.read().splitlines()
    l = [i.split("  ") for i in data]

    list1 = [int(i[0]) for i in l]
    list2 = [int(i[1]) for i in l]
    print(main(list1, list2))

    