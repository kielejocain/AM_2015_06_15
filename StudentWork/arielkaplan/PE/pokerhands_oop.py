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

        self.card_order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        self.hand = hand # string
        self.cards = hand.split(' ')
        self.values = self.values() # list of cards in high-->low order

        self.straight = self.straight() # boolean
        self.flush = self.flush() # boolean
        self.high = self.high_card() # list high-->low

        self.score = {
            # [0] is if hand is present
            # [1] and optional [2] is value of cards
            "royal flush": [False, None],
            "straight flush": [False, None], # high card of straight
            "four of a kind": [False, None],
            "full house": [False, None, None], # 3x value, 2x value
            "flush": [False, None],
            "straight": [False, None], # high card of straight
            "three of a kind": [False, None],
            "two pairs": [False, None, None], # value of each pair
            "one pair": [False, None],
            "high card": []
        }

    def __repr__(self):
        return str(self.cards)

    def straight(self):
        """Are card values consecutive? Returns boolean."""

        # consecutive = True
        # i = 0
        # while (i < 4) and (consecutive == True):
        # 	# check if difference between indices is 1
        # 	if ordered_index[i] == (ordered_index[i + 1] - 1):
        # 		i += 1
        # 	else:
        # 		consecutive = False
        # 		break
        pass


    def flush(self):
        """Are all cards same suit? Returns boolean."""
        suits = [
            self.hand.count("S"),
            self.hand.count("H"),
            self.hand.count("D"),
            self.hand.count("C")
        ]
        if max(suits) == 5:
            return True
        else:
            return False


    def values(self):
        """returns list of card values high --> low"""
        how_many = {
            "2": self.cards.count("2"),
            "3": self.cards.count("3"),
            "4": self.cards.count("4"),
            "5": self.cards.count("5"),
            "6": self.cards.count("6"),
            "7": self.cards.count("7"),
            "8": self.cards.count("8"),
            "9": self.cards.count("9"),
            "T": self.cards.count("T"),
            "J": self.cards.count("J"),
            "Q": self.cards.count("Q"),
            "K": self.cards.count("K"),
            "A": self.cards.count("A"),
        }
        ordered_values = []
        ordered_index = []

        for i in self.card_order:
            print i
            while how_many[i] != 0:
                print how_many[i]
                ordered_values.insert(0, card_order[i])
                ordered_index.append(i)
                how_many[i] -= 1
        return ordered_values

    def high_card(self):
        """Returns list of cards from high to low"""
        # Remove those already used???
        pass

    def calculate(self):
        """Returns dict score: """
        # needs more arguments, probably
        pass


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

# score1 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
# score2 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]

# compare(score1, score2)
# print "Player 1 should win.\n"

# score1 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 974]
# score2 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 976]

# compare(score1, score2)
# print "Player 2 should win.\n"

test_hand1 = Hand('5H 5C 6S 7S KD')
test_hand2 = Hand('2C 3S 8S 8D TD')

print test_hand1.hand
print test_hand1.cards
print test_hand1.values
print test_hand1.straight
print test_hand1.flush
print test_hand1.high

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