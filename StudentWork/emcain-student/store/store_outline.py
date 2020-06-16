class Store:

class Product:
	# has cost (wholesale), price (retail), inventory
	# has physical attributes like color, weight
	# has various attributes based on subtype
	
	def __init__(self, name, cost, price):
		self.name = name
		self.cost = cost
		self.price = price
		self.inventory = 0
	
	def set_inventory(self, number):
		self.inventory = number
	
class Shirt(Product):
	# has size, color, decoration
	
class Book(Product):
	# has title, author, isbn, hard/softcover

class Cart(Order):
	# inherits Order's methods, attributes
	# has methods to add, remove and modify 
	def add_line_item(self, product, number):
		line_items.append(LineItem(product, number)
		for li in line_items:
			self.total += li.charge	
			
	def confirm_order(self):
		ord = Order()
		ord.line_items = self.line_items
		ord.total = self.total 
		return ord 

class Order:
	# has LineItems, Customer 
	# has Total Cost
	# has customer
	def __init__(self)
		self.line_items = [] 
		self.total = 0.0

class LineItem:
	# has Product, number --> calculate cost 
	def __init__(self, product, number):
		self.product = product
		self.number = number
		self.charge = product.price*number
		

class Customer:
	# has name, login, password, email
	# has default PaymentMethod
	# has default shipping and billing addresses
	# can shop, have a cart, modify cart, place orders
	
	def __init__(self, name, password, email):
		self.name = name
		self.password = password
		self.email = email 
		self.cart = Cart(None, self)
		self.orders = []
		self.balance = 0.0
	
	def add_to_cart(self, product, number)
		self.cart.add_line_item(product, number)
	
	def place_order(self):
		order = Order(self.cart.confirm_order())
		self.cart = Cart(None, self) 
		

class Payment: 

class PaymentMethod:
	# abstract class?

class CreditCard(PaymentMethod):

class StoreCredit(PaymentMethod):