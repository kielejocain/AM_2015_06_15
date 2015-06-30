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
		self.hand = hand # string
		self.cards = hand.split(' ')
		self.values = self.values() # list of cards in high-->low order

		self.straight = self.straight() # boolean
		self.flush = self.flush() # boolean
		self.high = self.high_card() # list high-->low

		self.card_order = ["2", "3", "4", "5", "6", "7",
			"8", "9", "T", "J", "Q", "K", "A"]
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

	def values(self):
		"""returns list of card values high --> low"""
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


	def of_a_kind(self):
		"""Returns # of occurrences of each value in a dict"""
		# list?
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

        for i in range(len(how_many)):
            if how_many[i] != 0:
                ordered_values.append(self.card_order[i])
                ordered_index.append(i)
        score["high card"] = ordered_values[::-1]
        # print ordered_values

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



