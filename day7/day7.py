
card_strength = dict([(str(i), i) for i in range(2,10)])
card_strength['T'] = 10
card_strength['J'] = 11
card_strength['Q'] = 12
card_strength['K'] = 13
card_strength['A'] = 14
from enum import Enum
from functools import total_ordering
class HandType(Enum):
    HIGHCARD = 1
    ONEPAIR = 2
    TWOPAIR = 3
    THREEOFAKIND = 4
    FULLHOUSE = 5
    FOUROFAKIND = 6
    FIVEOFAKIND = 7
@total_ordering
class Hand():
    def __init__(self, hand, bid):
        self._unsorted = hand
        self._sorted = ''.join(sorted(hand, key=lambda x: card_strength[x]))
        self.bid = int(bid)
        card_count = {}
        for c in self._sorted:
            card_count[c] = self._sorted.count(c)
        vals = [int(count) for count in sorted(''.join([str(v) for v in card_count.values()]), reverse = True)]
        if vals[0] == 5:
            print(f'{self._unsorted} is a 5 of a kind')
            self.type = HandType.FIVEOFAKIND
        elif vals[0] == 4:
            print(f'{self._unsorted} is a 4 of a kind')
            self.type = HandType.FOUROFAKIND
        elif vals[0] == 3 and vals[1] == 2:
            print(f'{self._unsorted} is a full house')
            self.type = HandType.FULLHOUSE
        elif vals[0] ==  3:
            print(f'{self._unsorted} is a 3 of a kind')
            self.type = HandType.THREEOFAKIND
        elif vals[0] == 2 and vals[1] == 2:
            print(f'{self._unsorted} is a 2 pair')
            self.type = HandType.TWOPAIR
        elif vals[0] == 2:
            print(f'{self._unsorted} is a pair')
            self.type = HandType.ONEPAIR
        else:
            print(f'{self._unsorted} is a high card')
            self.type = HandType.HIGHCARD
    def __eq__(self, other):
        return self._unsorted == other._unsorted
    def __lt__(self, other):
        if self._unsorted == other._unsorted:
            return True
        if self.type != other.type:
            return self.type.value < other.type.value
        idx = 0
        while self._unsorted[idx] == other._unsorted[idx]:
            idx += 1
        return card_strength[self._unsorted[idx]] < card_strength[other._unsorted[idx]]
    def __repr__(self):
        return f'{self._unsorted} {self.type.name}'

hands = []
with open('day7/day7.txt') as f:
    for line in f:
        hand, bid = line.strip().split(' ')
        hands.append(Hand(hand, bid))
hands = sorted(hands)
total_winnings = sum([(rank+1)*hand.bid for rank, hand in enumerate(hands)])
print(f'{total_winnings=}')
# test = Hand('25TAQ')
# print(test._unsorted)
# print(test._sorted)
# test = Hand('KKQKK')