def cheese_and_crackers(cheese_count, boxes_of_crackers) :
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# My own function. Run it ten different ways.
def kittens_to_wash(total_kittens, dirty_kittens) :
	clean_kittens = total_kittens - dirty_kittens
	print "There are %s clean kittens." % clean_kittens
	print "Please wash %s dirty kittens right away!" % dirty_kittens


