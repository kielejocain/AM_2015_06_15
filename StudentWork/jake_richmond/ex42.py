## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	"""docstring for Animal"""
	pass

#"""class ClassName(object):
	#"""docstring for ClassName"""
	#def __init__(self, arg):
		#super(ClassName, self).__init__()
		#self.arg = arg"""
		
	##?? has-a
class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self, name):
		##??
		self.name = name

# has-a 
class Cat(Animal):
	"""docstring for Cat"""
	def __init__(self, name):
		self.name = name
		
class Person(object):
	"""docstring for Person"""
	def __init__(self, name):
		super(Person, self).__init__()
		self.name = name

		## Person has-a pet of some kind
		self.pet = none

## ?? 
class Employee(Person):
	"""docstring for Employee"""
	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## ??
		self.salary = salary

## ??
class Fish(object):
	"""docstring for Fish"""
	pass

class Salmon(Fish):
	pass

class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")


		


