## Animal is-a object
class Animal(object):
	pass
	
## Dog is-a animal 
class Dog(Animal):
	def __init__(self, name):
		## Dog has-a name 
		self.name = name
		
## Cat is-a animal 
class Cat(Animal):
	def __init__(self, name):
		## cat has-a name
		self.name 
		
## person is-a object
class Person(object):

	def __init__(self, name):
		## person has-a name 
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None
	
#Employee is-a person 	
class Employee(Person):

	def __init__(self, name, salary)
		# employee has-a name and a salary 
		super(Employe, self).__init__(name)
		