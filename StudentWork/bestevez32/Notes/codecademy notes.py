#Codecademy Notes

#Functions: EXAMPLE #1

# First "def"ine a function called "cube" that takes the argument "number"
# Make the function "return" the cube of that number 
def cube(number):
    return number ** 3
        
# "def"ine a second function called "by_three" that takes argument "number"
#if that number is divisible by 3 should call cube(number)
def by_three(number):
    if number % 3 == 0:
        return cube(number)
# "else", by_three should return "False"        
    else:   
        return False
		
# Functions: EXAMPLE #2
# def a function shut_down that takes an argument s.
def shut_down(s):
# if shut_down receives an s equal to "yes" return Shutting down   
    if s == "yes":
        return "Shutting down"
#else if s == "no" return "Shutdown aborted"  
    elif s == "no": 
        return "Shutdown aborted"
#else return "Sorry"    
    else:
     return "Sorry" 
	 
#FUNCTIONS: EXAMPLE # 3

#def function called diatance_from_zero with an argument
def distance_from_zero(n):

#if the type is int or float return abs of function input
    if type(n) == int or type(n) == float:
        return abs(n)
 # else return nope  
    else:
        return "Nope"

#TAKING A VACATION SCRIPT:
		
def hotel_cost(nights):
    return 140 * nights
    
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    if city == "Tampa":
        return 220
    if city == "Pittsburgh":
        return 222
    if city == "Los Angeles":
        return 475
        
def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        return cost - 50
    elif days >= 3 and days <= 6: 
        return cost - 20
       
    return cost
    
def trip_cost(city, days, spending_money): 
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money
    
print trip_cost("Los Angeles", 5, 600)
    

# FOR LOOPS:

my_list = [1,9,3,8,5,7]

# variable follows "for"
for number in my_list:
    print 2 * number
	
	
