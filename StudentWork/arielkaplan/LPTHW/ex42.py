## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Class Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## ??
		self.name = name

## Cat is-a Animal
class Cat(Animal)

	def __init__(self, name):
		## ??
		self.name = name

## Person is-a object with attributes name and pet
class Person(object):

	def __init__(self, name):
		## Person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		## Employee has-a name; calls init of superclass Person
		super(Employee, self).__init__(name)
		## Employee has-a salary (added to imported init)
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Dog
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## Mary has-a pet set equal to instance satan
mary.pet = satan

## frank is-a Employee and has-a name and salary
frank = Employee("Frank", 120000)

## frank has-a pet set equal to instance rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()