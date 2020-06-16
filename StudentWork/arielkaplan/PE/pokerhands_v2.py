f = open("poker.txt")
all_hands = f.read()
f.close()

class Player(object):

    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.hands = []


class Round(object):
    """Compares two hands"""

    def __init__(self, hand1, hand2):
        self.hand1 = hand1
        self.hand2 = hand2
        self.winner = self.compare()

    def compare(hand1, hand2):
        """takes two strings, returns [0, 1] or [1, 0]"""
        pass



class Hand(object):
    """
    One five-card hand as a string with spaces between,
    ex. '6S QH 6D 6H QD'
    """
    # consecutive?
    # how many suits?
    # list of high->low unused cards
    # how many of each value
    # score dict:

    def __init__(self, hand):

        self.HAND_LENGTH = 5
        self.card_order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        self.score_order = [
            "royal flush",
            "straight flush",
            "four of a kind",
            "full house",
            "flush",
            "straight",
            "three of a kind",
            "two pairs",
            "one pair",
            "high card"
        ]

        self.hand = hand # string
        self.cards = hand.split(' ')
        self.values = self.values() # list of cards in low-->high order
        self.how_many = self.how_many()  # {'card': frequency}

        self.straight = self.straight() # boolean
        self.flush = self.flush() # boolean
        self.high_cards = self.high_card() # unused card list low-->high

        self.score = {}
        # e.g. "straight flush": [high card value, []]
        # e.g. "full house": [pair value, three of a kind value, []]
        # e.g. "three of a kind": [three of a kind value, [A, 4] <-- unused cards

    def __repr__(self):
        return str(self.hand)

    def straight(self):
        """Are card values consecutive? Returns boolean."""
        LOW_HAND_VALUE = 0
        card_order_start = 0

        # find lowest card matched to card order
        while self.values[LOW_HAND_VALUE] != self.card_order[card_order_start]:
            card_order_start += 1

        # see if next card == next in card order
        for i in range(self.HAND_LENGTH):
            current_value = self.values[i]
            compare_value = self.card_order[card_order_start]
            if current_value != compare_value:
                return False
                break
            i += 1
            card_order_start += 1
        return True

    def flush(self):
        """Are all cards same suit? Returns boolean."""
        SUIT_INDEX = 1
        for i in range(self.HAND_LENGTH):
            current_suit = self.cards[i][SUIT_INDEX]
            prev_suit = self.cards[i - 1][SUIT_INDEX]
            if current_suit != prev_suit:
                return False
        return True

    def how_many(self):
        of_a_kind = {}
        for value in self.values:
            if value not in of_a_kind.keys():
                of_a_kind[value] = 0
            of_a_kind[value] += 1
        return of_a_kind

    def values(self):
        """returns list of card values low-->high"""
        VALUE_INDEX = 0
        values = []
        for card in self.cards:
            values.append(card[VALUE_INDEX])

        ordered_values = []
        for i in self.card_order:
            for j in values:
                if i == j:
                    ordered_values.append(i)
        return ordered_values

    def high_card(self):
        """Returns list of unused cards from low-->high"""
        high_cards = []
        if self.straight:
            return []
        else:
            for card in self.card_order:
                if card in self.how_many.keys() and self.how_many[card] == 1:
                    high_cards.append(card)
            return high_cards

    def calc_flush(self):
        HIGHEST_CARD_INDEX = -1
        highest_card = self.values[HIGHEST_CARD_INDEX]
        if self.flush and self.straight and (highest_card == "A"):
            self.score["royal flush"] = [highest_card, self.high_cards]
        elif self.flush and self.straight:
            self.score["straight flush"] = [highest_card, self.high_cards]
        elif self.flush:
            self.score["flush"] = [highest_card, self.high_cards]
        else:
            pass

    def calc_multiples(self):
        three = None
        pairs = []

        for card, count in self.how_many.items():
            if count == 4:
                four_of_value = card
                self.score["four of a kind"] = [four_of_value, self.high_cards]
            elif count == 3:
                three = card
                self.score["three of a kind"] = [three, self.high_cards]
            elif count == 2:
                # TODO: Order pairs high-->low
                pairs.append(card)
            else:
                pass
        self.calc_full_house(three, pairs)

    def calc_full_house (self, three, pairs):
        """Takes a two lists of values; may be empty"""
        if (three != None) and (len(pairs) == 1):
            self.score["full house"] = [three, pairs[0], self.high_cards]
            del(self.score["three of a kind"])
        elif len(pairs) == 2:
            self.score["two pairs"] = [pairs[1], pairs[0], self.high_cards] # higher value first
        elif len(pairs) == 1:
            self.score["one pair"] = [pairs[0], self.high_cards]
        else:
            print "Not a full house"

    def calculate(self):
        """Returns dict score: """
        # needs more arguments, probably
        self.calc_flush()
        self.calc_multiples()
        if self.score == {}:
            self.score["high card"] = self.high_cards

p1 = Player("Player 1")
p2 = Player("Player 2")

two_hands = all_hands.split("\n")

# split rounds into player 1 and player 2 hands
for hand in two_hands:

    hand1 = Hand(hand[:14])
    p1.hands.append(hand1)

    hand2 = Hand(hand[15:])
    p2.hands.append(hand2)

    print p1.hands
    print p2.hands
    # test with just one round
    break


#############

def test_hand_values(hand, outcome):
    test_hand = Hand(hand)
    test_hand.calculate()
    print "hand: " + str(test_hand.hand) + " = " + str(outcome)
    # print "cards: " + str(test_hand.cards)
    print "values: " + str(test_hand.values)
    print "straight: " + str(test_hand.straight)
    print "flush: " + str(test_hand.flush)
    print "high: " + str(test_hand.high_cards)
    print "Score: "
    for key, value in test_hand.score.items():
        print str(key) + ": " + str(value)
    print "-" * 10

test_hand_values('5H 5C 6S 7S KD', 'one pair, K high') # one pair, K high
test_hand_values('2C 3S 8S 8D TD', 'one pair, T high') # one pair, T high
test_hand_values('6S 7S 8S 9S TS', 'straight flush ') # straight flush
test_hand_values('6S QH 6D 6H QD', 'full house')
test_hand_values('AH 7S AS 9D 9H', 'two pair, A & 9')
test_hand_values('6S 7S 8S 9D TH', 'straight')
test_hand_values('8S 8H 8D 8C JC', 'four of a kind')
test_hand_values('TS JS QS KS AS', 'royal flush')
test_hand_values('6S KS 2S 9D TH', 'nothing')
test_hand_values('6D KH 8S 9C TD', 'nothing')



# score1 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
# score2 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]

# compare(score1, score2)
# print "Player 1 should win.\n"

# score1 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 974]
# score2 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 976]

# compare(score1, score2)
# print "Player 2 should win.\n"

# test_hand1 = Hand('5H 5C 6S 7S KD')
# test_hand2 = Hand('2C 3S 8S 8D TD')

# find_score(test_hand1) # should be one pair
# find_score(test_hand2) # should be one pair

# test_hand4 = '6S QH 6D 6H QD'
# find_score(test_hand4)
# print "^^ should be full house"

# test_hand5 = 'AH 7S AS 9D 9H'
# find_score(test_hand5)
# print "^^ should be two pair"

# test_hand6 = '6S KS 2S 9D TH'
# find_score(test_hand6)
# print "^^ should be nothing. High card only. Should lose to next hand."

# test_hand7 = '6D KH 8S 9C TD'
# find_score(test_hand7)
# print "^^ should be nothing. High card only. Should win over previous hand."

# test_hand3 = '6S 7S 8S 9D TH'
# find_score(test_hand3)
# print "^^ should be straight"

# test_hand8 = '6S 7S 8S 9S TS'
# find_score(test_hand8)
# print "^^ should be straight flush"

# test_hand9 = 'TS JS QS KS AS'
# find_score(test_hand9)
# print "^^ should be royal flush"
#
# test_hand10 = '8S 8H 8D 8C JC'
# find_score(test_hand10)
# print "^^ should be four of a kind"
#