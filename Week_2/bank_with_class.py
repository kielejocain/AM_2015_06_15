class Account(object):
    """Basic account definitions."""

    minimum_balance = 0

    def __init__(self, name, account_type, balance, apr):
        self.name = name
        self.type = account_type
        self.balance = balance
        self.apr = apr
        self.transactions = []

    def deposit(self, amount):
        """Add the requested amount to the balance."""
        self.balance += amount
        self.transactions.append(("Deposit", amount))
        print "Your new balance is $%d." % self.balance

    def withdrawal(self, amount):
        """Withdraw the requested amount from the account if possible."""
        if self.balance - amount < self.minimum_balance:
            print "This would take you below your minimum balance."
            return
        else:
            self.balance -= amount
            print "Please take your cash."
            print "Your balance is now $%d." % self.balance
            self.transactions.append(("Withdrawal", amount))

class SavingsAccount(Account):
    """A general blueprint for savings accounts."""

    account_type = 'savings'
    apr = .03
    minimum_balance = 100.0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []

class CheckingAccount(Account):
    """A checking account with lower default apr."""

    account_type = 'checking'
    apr = .01
    minimum_balance = 0.0
    transactions = []

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def setup_dd(self, company):
        """Offers a savings apr to checking accounts with direct deposit."""
        self.company = company
        self.apr = .03
        self.minimum_balance = 1000.0
