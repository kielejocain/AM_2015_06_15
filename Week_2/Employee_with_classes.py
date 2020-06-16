class Employee:
	"Common base class for all employees"
	empcount = 0 # Employee Count

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.emp_count += 1

	def display_count(self):
		print "Total Employee %d" % Employee.em_count

	def display_employee(self):
		print "Name : ", self.name, "Salary: ", self.salary

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
print "Total Employee %d" % Employee.emp_count