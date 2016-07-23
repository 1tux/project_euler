import random
def roll():
    a = random.randrange(1,7)
    b = random.randrange(1,7)
    if a == b:
        doubles = True
    else:
        doubles = False
    return (a+b, doubles)


def chance_next_rail(pos):
    while not pos in [5, 15, 25, 35]:
        pos += 1
        if pos == 40:
            pos = 0
    return pos


def chance_next_utility(pos):
    if pos in range(0,12) + range(28,40):
        return 12
    if pos in range(12,28):
        return 28


def chance_back_three(pos):
    new = pos - 3
    if new < 0:
        return 40+new
    else:
        return new


def chance(card, pos):
    if card == 1:
        return 0
    elif card == 2:
        return 10
    elif card == 3:
        return 11
    elif card == 4:
        return 24
    elif card == 5:
        return 39
    elif card == 6:
        return 5
    elif card == 7 or card == 8:
        return chance_next_rail(pos)
    elif card == 9:
        return chance_next_utility(pos)
    elif card == 10:
        return chance_back_three(pos)
    else:
        return pos


def cc(card, pos):
    if card == 1:
        return 0
    elif card == 2:
        return 10
    else:
        return pos



def shuffle_cc():
    deck = range(1,17)
    random.shuffle(deck)
    return deck


def shuffle_chance():
    deck = range(1,17)
    random.shuffle(deck)
    return deck


def main():
    print 'Simulating some rolls of monopoly:\n\n\n'
    output_text = ''
    records = [0]*40
    chancedeck = shuffle_chance()
    ccdeck = shuffle_cc()
    pos = 0  #0 is Go
    x = 0
    doubles_count = 0
    while x < 10 ** 6:
        if x % 1000000 == 0:
            print x # for monitoring progress
        x+=1
        dice_roll = roll()
        if dice_roll[1]==True:
            doubles_count+=1
        else:
            doubles_count = 0
        if doubles_count == 3:
            pos = 10
            doubles_count = 0
        else:
            pos += dice_roll[0]
            if pos > 39:
                pos = pos-40
            if pos == 2 or pos == 17 or pos == 33:
                temp = ccdeck.pop()
                ccdeck.insert(0,temp)
                pos = cc(temp, pos)
            if pos == 7 or pos == 22 or pos == 36:
                temp2 = chancedeck.pop()
                chancedeck.insert(0,temp2)
                pos = chance(temp2, pos)
            if pos == 30:
                pos = 10
        records[pos]+= 1
    second = list(records)
    #output_text += str(records)
    #output_text += '\n\n\n'
    for x in range(0,40):
        output_text += str((records.index(max(records)), (max(records)+0.0)/10000000))
        records[records.index(max(records))] = 0
    a =  second.index(max(second))
    second.pop(a)
    b = second.index(max(second))
    second.pop(b)
    print a, b, second.index(max(second))
    print "end of text"
    return second

main()