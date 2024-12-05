def checkCorrectness(update, rule_dict, rule_dict_before):
    update = [int(i) for i in update.split(',')]
    if len(update) <= 2: 
        return update 
    
    for i in range(len(update)-1):
        if update[i] in rule_dict:
             if update[i + 1] not in rule_dict.get(update[i], []):
                return update
    if update[-1] in rule_dict_before:
        if update[-2] not in rule_dict_before.get(update[-1], []):
            return update
    return 0

def fixIncorrectUpdates(incorrectUpdates, rule_dict):
    if len(incorrectUpdates) <= 2: 
        return update 
    fixed = False
    while not fixed:
        fixed = True
        for i in range(len(incorrectUpdates) - 1):
            if incorrectUpdates[i + 1] not in rule_dict.get(incorrectUpdates[i], []):
                # Swap elements and mark as not fixed
                incorrectUpdates[i], incorrectUpdates[i + 1] = incorrectUpdates[i + 1], incorrectUpdates[i]
                fixed = False
    return incorrectUpdates

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
    incorrectUpdates = []
    fixed = []
    rules = data[0].split('\n')
    updates = data[1].split('\n')
    rule_dict = makeDict(rules)
    rule_dict_before = makeDictBefore(rules)
    for update in updates:
        incorrectUpdates.append(checkCorrectness(update, rule_dict, rule_dict_before))
    
    incorrectUpdates = list(filter(lambda x: x != 0, incorrectUpdates))
    print(incorrectUpdates)
    for update in incorrectUpdates:
        fixed.append(fixIncorrectUpdates(update, makeDict(rules)))
    
    print(fixed)

    for update in fixed:
        total += getMiddleNumber(update)

    print(total)