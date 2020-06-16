
    # Every if-statement must have an else.
    # If this else should never run because it doesn't make sense, then you must use a die function in the else that prints out an error message and dies, just like we did in the last exercise. This will find many errors.
    # Never nest if-statements more than two deep and always try to do them one deep.
    # Treat if-statements like paragraphs, where each if-elif-else grouping is like a set of sentences. Put blank lines before and after.
    # Your boolean tests should be simple. If they are complex, move their calculations to variables earlier in your function and use a good name for the variable.

	
	# If you follow these simple rules, you will start writing better code than most programmers. Go back to the last exercise and see if I followed all of these rules. If not, fix my mistakes.
	
	from sys import exit

def gold_room():
    print "This room is full of gold.  How much do you take?"

    choice = int(raw_input("> "))
	
    if isinstance(choice, int):
        how_much = int(choice)
    else:
		print("this should not happen...")
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()