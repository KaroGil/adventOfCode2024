def checkCorrectness(update, rule_dict, rule_dict_before):
    update = [int(i) for i in update.split(',')]
    if len(update) <= 2: 
        return update 
    
    for i in range(len(update)-1):
        if update[i] in rule_dict:
             if update[i + 1] not in rule_dict.get(update[i], []):
                return 0
    if update[-1] in rule_dict_before:
        if update[-2] not in rule_dict_before.get(update[-1], []):
            return 0
    return update

def getMiddleNumber(updated_pages):
    return updated_pages[len(updated_pages) // 2]

def makeDict(rules):
    rules_dict = {}
    rules_dict_before = {}
    for rule in rules:
        rule = rule.split('|')
        X = int(rule[0])
        Y = int(rule[1])
        if X not in rules_dict:
            rules_dict[X] = []
        rules_dict[X].append(int(rule[1]))
        if Y not in rules_dict_before:
            rules_dict_before[Y] = []
        rules_dict_before[Y].append(int(rule[0]))
    return rules_dict, rules_dict_before

with open('test.csv', 'r') as file:
    data = file.read().split('\n\n')
    total = 0
    correctUpdates = []
    rules, updates = data[0].split('\n'),  data[1].split('\n')

    rules, rulesBefore = makeDict(rules)
    for update in updates:
        correctUpdates.append(checkCorrectness(update, rules, rulesBefore))

    correctUpdates = [x for x in correctUpdates if x !=0]

    for correctUpdate in correctUpdates:
        total += getMiddleNumber(correctUpdate)

    print(total)