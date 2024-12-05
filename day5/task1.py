def checkCorrectness(update, rule_dict, rule_dict_before):
    count = 0
    update = [int(i) for i in update.split(',')]
    print("update", update)
    for i in range(len(update)):
        print(update[i])
        intenal_count = 0
        if update[i] in rule_dict:
            for j in range(i+1,len(update)):
                if update[j] in rule_dict[update[i]]:
                    intenal_count += 1
                else:
                    break
        if update[i] in rule_dict_before:
            for j in range(i-1,-1,-1):
                if update[j] in rule_dict_before[update[i]]:
                    intenal_count += 1
                else:
                    break
        if intenal_count == len(update) - 1:
            count += 1
    print("count", count)
    print("update", len(update))
    if count == len(update) : 
        return update
    return 0

def getMiddleNumber(updated_pages):
    return updated_pages[len(updated_pages) // 2]

def makeDict(rules):
    rules_dict = {}
    for rule in rules:
        rule = rule.split('|')
        X = int(rule[0])
        if X not in rules_dict:
            rules_dict[X] = []
        rules_dict[X].append(int(rule[1]))
    return rules_dict

def makeDictBefore(rules):
    rules_dict = {}
    for rule in rules:
        rule = rule.split('|')
        X = int(rule[1])
        if X not in rules_dict:
            rules_dict[X] = []
        rules_dict[X].append(int(rule[0]))
    return rules_dict

with open('input.csv', 'r') as file:
    data = file.read().split('\n\n')
    total = 0
    correctUpdates = []
    rules = data[0].split('\n')
    updates = data[1].split('\n')
    print(makeDict(rules))
    for update in updates:
        correctUpdates.append(checkCorrectness(update, makeDict(rules), makeDictBefore(rules)))
    
    correctUpdates = list(filter(lambda x: x != 0, correctUpdates))
    print(correctUpdates)

    for correctUpdate in correctUpdates:
        total += getMiddleNumber(correctUpdate)

    print(total)