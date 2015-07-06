__author__ = 'Brandon'



class Vehicle(object):
    """ Attributes:
            Wheels: An integer representing the number of wheels a vehicle has.
            Miles: Integral number of miles driven on a vehicle.
            Make: The name of the vehicle as a string.
            Model: The model of the vehicle as a string.
            Year: The integral year the vehicle was built.
            Sold_On: The date the vehicle was sold on.
    """

    def __init__(self, wheels, miles, sold_on):
        self.wheels = wheels
        self.miles = miles
        self.sold_on = sold_on

    def sale_price(self):
        """ Sale price is based on # of wheels x 5,000 - miles(5%)
        """

        if self.sold_on is None:
            return 0.0
        else:
            return 5000.0 * self.wheels - (0.05 * self.miles)

    def purchase_price(self):
        """ Purchase price is based on # of wheels x 2,500 - miles(10%)
        """

        if self.sold_on is None:
            return 0.0
        else:
            return self.wheels * 2500.0 - (0.10 * self.miles)

car = Vehicle(4.0, 20000, 2010)
motorcycle = Vehicle(2.0, 3000, 2014)
mac_truck = Vehicle(18.0, 40000, 2009)

print car.sale_price()
print car.purchase_price()
print motorcycle.sale_price()
print motorcycle.purchase_price()
print mac_truck.sale_price()
print mac_truck.purchase_price()







