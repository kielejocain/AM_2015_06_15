f = open("poker.txt")
all_hands = f.read()
f.close()

# split hands so a list of player 1 hands 
# and a list of player 2 hands (2 lists of lists)

# make a dictionary of scoring:
# starting with best score, check what each hand has
# "high card" is decending list of values

# evaluate first list in each list:
# check suits: # of same:
#	- all same suit == flush
#		- check #: consecutive?
# 			- straight flush
# 				- royal flush
# check numbers: # of same:
# 	- 4 is four of a kind
# 	- 3 is three of a kind
# 		- remaining cards are a pair == full house
# 	- 2 is a pair
# 		- 2 more is 2 pairs

player1 = []
p1_wins = 0

player2 = []
p2_wins = 0

who_wins = [p1_wins, p2_wins]

card_order = ["2", "3", "4", "5", "6", "7", 
	"8", "9", "T", "J", "Q", "K", "A"]
# card_order.index("T") >> 8

hands = all_hands.split("\n")

# split rounds into player 1 and player 2 hands
for hand in hands:
	p1_hand = hand[:14]
	p2_hand = hand[15:]
	player1.append(p1_hand)
	player2.append(p2_hand)
	# print player1
	# print player2
	# test with just one round
	break

# find score of a hand:
def find_score(hand):
	"""Takes a string of 2-char cards. Returns dict score."""
	print hand
	cards = hand.split(' ')
	# print cards

	score = {
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

	# How many of each value in the hand
	how_many = [
		hand.count("2"),
		hand.count("3"),
		hand.count("4"),
		hand.count("5"),
		hand.count("6"),
		hand.count("7"),
		hand.count("8"),
		hand.count("9"),
		hand.count("T"),
		hand.count("J"),
		hand.count("Q"),
		hand.count("K"),
		hand.count("A"),
	]

	how_many = {
		"2": hand.count("2"),
		"3": hand.count("3"),
		"4": hand.count("4"),
		"5": hand.count("5"),
		"6": hand.count("6"),
		"7": hand.count("7"),
		"8": hand.count("8"),
		"9": hand.count("9"),
		"T": hand.count("T"),
		"J": hand.count("J"),
		"Q": hand.count("Q"),
		"K": hand.count("K"),
		"A": hand.count("A"),
	}


	# How many of each suit in the hand
	suits = [hand.count("S"), hand.count("H"), hand.count("D"),
		hand.count("C")]

	# High cards
	ordered_values = []
	ordered_index = []

	for i in range(len(how_many)):
		if how_many[i] != 0:
			ordered_values.append(card_order[i])
			ordered_index.append(i)
	score["high card"] = ordered_values[::-1]
	# print ordered_values


	# Are cards consecutive?
	consecutive = True
	i = 0
	while (i < 4) and (consecutive == True):
		# check if difference between indices is 1
		if ordered_index[i] == (ordered_index[i + 1] - 1):
			i += 1
		else:
			consecutive = False
			break

	# of-a-kind
	if max(how_many) == 4:

		# find value of four-of-a-kind
		collection_value = card_order[how_many.index(4)]
		score["four of a kind"] = [True, collection_value]
		# remove claimed cards from high card list
		score["four of a kind"].remove(collection_value)
		print "four of a kind"

	elif (max(how_many) == 3) and (2 in how_many):

		collection_value_high = card_order[how_many.index(3)]
		collection_value_low = card_order[how_many.index(2)]
		score["full house"] = [True, collection_value_high, 
			collection_value_low]
		# remove claimed cards from high card list
		score["full house"].remove(collection_value_high)
		score["full house"].remove(collection_value_low)
		print "full house"

	elif max(how_many) == 3:

		collection_value = card_order[how_many.index(3)]
		score["three of a kind"] = [True, collection_value]
		# remove claimed cards from high card list
		score["three of a kind"].remove(collection_value)
		print "Three of a kind"

	elif how_many.count(2) == 2:

		collection_value1 = card_order[how_many.index(2)]

		score["two pair"] = [True, collection_value]
		# remove claimed cards from high card list
		score["two pair"].remove(collection_value)
		print "Two pair"
	elif how_many.count(2) == 1:
		score["one pair"] = True
		print "One pair"

	# Flush
	elif (max(suits) == 5) and (consecutive == True):
		# Check if straight flush is a royal flush
		if ordered_index[-1] == 12:
			score["royal flush"] = True
			print "Woo, royal flush!"
		else: 
			score["straight flush"] = True
			print "Straight flush"

	# Straight
	elif consecutive == True:
		# Already checked for flushes; not same suit
		score["straight"] = True
		print "Straight, no flush"

	# Got nothing but high card	
	else:
		print "Nothing interesting in hand."
		# find highest non-zero number in how_many.
		# match that index to card_order
		print "Highest card is: %s" % score["high card"][0]

	print score
	return score


def compare(score1, score2):
	"""Compares the score of two hands. Increases win tally."""
	"""Currently broken. :( """
	p1 = 0
	p2 = 0

	# because score is now a dictionary, make list of order 
	# to check:
	high_to_low = [
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

	# for i in score1:
	# 	if i > score2[i]:
	# 		print i
	# 		print score2[i]
	# 		print "Player 1 wins!"
	# 		p1 += 1
	# 		break
	# 	elif i < score2[i]:
	# 		print i
	# 		print score2[i]
	# 		print "Player 2 wins!"
	# 		p2 += 1
	# 		break
	# 	else: 
	# 		print "They're equal, try the next one!"
	wins = [p1, p2]

#############

# score1 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
# score2 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]

# compare(score1, score2)
# print "Player 1 should win.\n"

# score1 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 974]
# score2 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 976]

# compare(score1, score2)
# print "Player 2 should win.\n"

# test_hand1 = '5H 5C 6S 7S KD'
# test_hand2 = '2C 3S 8S 8D TD'

# find_score(test_hand1) # should be one pair
# find_score(test_hand2) # should be one pair

test_hand4 = '6S QH 6D 6H QD'
find_score(test_hand4) 
print "^^ should be full house"

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

test_hand10 = '8S 8H 8D 8C JC'
find_score(test_hand10)
print "^^ should be four of a kind"