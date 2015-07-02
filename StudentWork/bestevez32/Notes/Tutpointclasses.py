# CREATING CLASSES

class Employee:
	'Common basic class for all employees'
	empCount = 0 # This is a variable whose value is shared among all 
				# instance of this class. 
	
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount +=1
		
	def displayCount(self):
		print "Total Employee %d" % Employee.empCount
		
	def displayEmployee(self):
		print "Name: ", self.name, ", Salary: ", self.salary 
		
# CREATING INSTANCE OBJECTS

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of EMployee class"
emp2 = Employee("Manni", 5000)

#Accessing Attributes"

emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount




