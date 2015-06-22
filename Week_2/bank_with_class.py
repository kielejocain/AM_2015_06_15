class Account(object):
    """Basic account definitions."""

    minimum_balance = 0

    def __init__(self, name, type, balance, apr):
        self.name = name
        self.type = type
        self.balance = balance
        self.apr = apr

    def add_balance(self, amount):
        """Add the requested amount to the balance."""
        self.balance += amount

    def withdrawal(self, amount):
        """Withdraw the requested amount from the account if possible."""
        if self.balance - amount < self.minimum_balance:
            print "This would take you below your minimum balance."
            return
        else:
            self.balance -= amount
            print "Please take your cash."
            print "Your balance is now $%d." % self.balance

class SavingsAccount(Account):
    """A general blueprint for savings accounts."""

    type = 'savings'
    apr = .03
    minimum_balance = 100.0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

class CheckingAccount(Account):
    """A checking account with lower default apr."""

    type = 'checking'
    apr = .01
    minimum_balance = 0.0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def setup_dd(self, company):
        """Offers a savings apr to checking accounts with direct deposit."""
        self.company = company
        self.apr = .03
        self.minimum_balance = 1000.0
