__author__ = 'Brandon'


class Customer(object):
    """ A customer of ABC Bank w/checking account. Customers have the following properties:
            Attributes:
                Name: A string representing the customers name.
                Balance: A float tracking the current balance of the customers account.
    """

    def __init__(self, name, balance = 0.0):
        """ Return a customer object whos name is *name*
            and string balance is *balance*
        """
        self.name = name
        self.balance = balance

    def withdraw (self, amount):
        """ Return the balance remaining after withdrawing *amount* dollars
        """
        if amount > self.balance:
            raise RuntimeError

        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """ Return the balance remaining after depositing *amount* dollars
        """
        self.balance += amount
        return self.balance

Jeff = Customer('Jeff Knupp', 1000)
Barry = Customer('Barry Smith', 10000)
Pablo = Customer('Pablo Escobar', 1000000)

print Pablo.deposit(1.00)
print Pablo.withdraw(.75)
print Pablo.balance
