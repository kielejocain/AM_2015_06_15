"""Application solves for V, R or I in Ohm's Law equation."""

def solve_for_i():
	volt = "s"
	while not volt.isdigit():
		volt = raw_input("What is the voltage, in volts, of the circuit? \n>")
		if volt.isdigit():
			volt = int(volt)
			resist = raw_input("Great. What is the current, in amperes, of the circuit? \n>")
			if resist.isdigit():
				resist = int(resist)
				current = volt / resist
				print "In accorance with Ohm's Law, the current on this circuit must be: %d amperes." % current
				break
			else:
				print "Really? Let's start over."
				volt = "s"
		else:
			print "Really?"


def solve_for_r():
	volt = "s"
	while not volt.isdigit():
		volt = raw_input("What is the voltage, in volts, of the circuit? \n>")
		if volt.isdigit():
			volt = int(volt)
			current = raw_input("Great. What is the current, in amperes, of the circuit? \n>")
			if current.isdigit():
				current = int(current)
				resist = volt / current
				print "In accorance with Ohm's Law, the resistance on this circuit must be: %d ohms." % resist
				break
			else:
				print "Really? Let's start over."
				volt = "s"
		else:
			print "Really?"


def solve_for_v():
	current = "s"
	while not current.isdigit():
		current = raw_input("What is the current, in amperes, of the circuit? \n>")
		if current.isdigit():
			current = float(current)
			resist = raw_input("Great. What is the resistance, in ohms, of the circuit? \n>")
			if resist.isfloat():
				resist = float(resist)
				volt = current * resist
				print "In accorance with Ohm's Law, the voltage on this circuit must be: %d volts." % volt
				break
			else:
				print "Really? Let's start over."
				current = "s"
		else:
			print "Really?"
			

def begin():
	print "Welcome to the Ohm's Law Calculator!"
	choice = raw_input("Would you like to Solve for V (Voltage), I (Current) or R (Resistance)?")
	if choice == "V" or choice == "v":
		solve_for_v()
	elif choice == "I" or choice == "i":
		solve_for_i()
	elif choice == "R" or choice == "r":
		solve_for_r()
	else:
		choice2 = "0"
		while choice2 != "Y" or choice2 != "y" or choice2 != "N" or choice2 != "n": 
			choice2 = raw_input("That was not a valid choice. Would you like to try again? Y/N?")
			if choice2 == "Y" or choice2 == "y":
				begin()
			elif choice2 == "N" or choice2 == "n":
				print "Goodbye."
			else:
				print "Really?"
				
				
begin()