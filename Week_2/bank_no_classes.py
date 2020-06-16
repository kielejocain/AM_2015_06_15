accounts = {}

# add an account manually
accounts['Kyle Joecken'] = {'type': 'checking', 'balance': 10.25, 'apr': .01}

# define a function for it
def make_account(name, type, balance, apr):
    """Takes basic account info and adds account to list."""
    if name in accounts:
        print "That person already has an account!"
        return
    else:
        accounts[name] = {'type': type, 'balance': balance, 'apr': apr}

make_account('Kevin Long', 'savings', 1200.0, .03)

# add money to an account manually (I got paid!)
accounts['Kyle Joecken']['balance'] += 100.0

# define a function for it
def add_balance(name, amount):
    """Adds the requested amount to the named account if possible."""
    if name not in accounts:
        print "No account under that name."
    else:
        accounts[name]['balance'] += amount
        print "Your new balance is: $%d" % accounts[name]['balance']

add_balance('Kevin Long', 500.0)

# get money out.  Gotta check the balance!
print "Your balance is $%d." % accounts['Kyle Joecken']['balance']
accounts['Kyle Joecken']['balance'] -= 50.0

#define a function
def withdrawal(name, amount):
    """Withdraws the requested amount from the named account if possible."""
    if name not in accounts:
        print "No account under that name."
    elif accounts[name]['balance'] < amount:
        print "Insufficient funds."
    else:
        accounts[name]['balance'] -= amount
        print "Here is your $%d." % amount
        print "Your balance is now $%d." % accounts[name]['balance']

withdrawal('Kevin Long', 200.0)
