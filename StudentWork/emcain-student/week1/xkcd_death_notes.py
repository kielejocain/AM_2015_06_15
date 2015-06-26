# from https://web.archive.org/web/20121220025758/http://xkcd.com/actuary.py.txt

# script written by Randall Munroe. Most comments by Emily Cain (although there were a few brief ones explaining how the program worked before I looked at it)

# Summary of program (by Emily):

# this program takes inputs of current ages and genders to calculate the probability any or all of those people will die in a certain time period. 

# if you input a year (after the current year) or a number of years (less than the current year) the program will calculate the probability that anyone or everyone will die in that time period. Either way, the program also determines the number of years for certain probabilities of anyone or everyone dying. 

# The program outputs these calculations in an easily readable form. 


#!/usr/bin/python
import sys
import datetime

# The following description was written by Randall (the programmer). 

# Calculates death probabilities based on Social Security
# actuarial tables for a given group of people.

# Run with a list of ages/genders and an optional timespan (or year in the future):

# python actuary.py 63m 80m 75f 73m 10

# or:

# python actuary.py 63m 80m 75f 73m 2022

# This will give statistics for that group, including
# various probabilities over 10 years. Years can be
# ommitted and it will still give some statistics.
# If "Years" exceeds the current calendar year, it will be interpreted as a date.


#this is a list of lists. The outer list contains two inner lists, each of which is an actuarial table--one for men and one for women
bothtables=[[0.00756, 0.00052, 0.00035, 0.00025, 0.00020, 0.00018, 0.00017, 0.00016, 0.00014, 0.00011, 0.00009, 0.00010, 0.00015, 0.00027, 0.00043, 0.00061, 0.00078, 0.00094, 0.00107, 0.00119, 0.00131, 0.00142, 0.00149, 0.00151, 0.00148, 0.00143, 0.00140, 0.00138, 0.00137, 0.00139, 0.00141, 0.00143, 0.00147, 0.00152, 0.00158, 0.00165, 0.00174, 0.00186, 0.00202, 0.00221, 0.00243, 0.00267, 0.00291, 0.00317, 0.00344, 0.00373, 0.00405, 0.00441, 0.00480, 0.00524, 0.00573, 0.00623, 0.00671, 0.00714, 0.00756, 0.00800, 0.00853, 0.00917, 0.00995, 0.01086, 0.01190, 0.01301, 0.01413, 0.01522, 0.01635, 0.01760, 0.01906, 0.02073, 0.02265, 0.02482, 0.02729, 0.03001, 0.03289, 0.03592, 0.03918, 0.04292, 0.04715, 0.05173, 0.05665, 0.06206, 0.06821, 0.07522, 0.08302, 0.09163, 0.10119, 0.11183, 0.12367, 0.13679, 0.15124, 0.16702, 0.18414, 0.20255, 0.22224, 0.24314, 0.26520, 0.28709, 0.30846, 0.32891, 0.34803, 0.36544, 0.38371, 0.40289, 0.42304, 0.44419, 0.46640, 0.48972, 0.51421, 0.53992, 0.56691, 0.59526, 0.62502, 0.65628, 0.68909, 0.72354, 0.75972, 0.79771, 0.83759, 0.87947, 0.92345, 0.96962], [0.00615, 0.00041, 0.00025, 0.00018, 0.00015, 0.00014, 0.00014, 0.00013, 0.00012, 0.00011, 0.00010, 0.00010, 0.00012, 0.00016, 0.00021, 0.00028, 0.00034, 0.00039, 0.00042, 0.00043, 0.00045, 0.00047, 0.00048, 0.00049, 0.00050, 0.00051, 0.00052, 0.00053, 0.00056, 0.00059, 0.00063, 0.00068, 0.00073, 0.00078, 0.00084, 0.00091, 0.00098, 0.00108, 0.00118, 0.00130, 0.00144, 0.00158, 0.00173, 0.00189, 0.00206, 0.00225, 0.00244, 0.00264, 0.00285, 0.00306, 0.00329, 0.00355, 0.00382, 0.00409, 0.00437, 0.00468, 0.00505, 0.00549, 0.00603, 0.00665, 0.00736, 0.00813, 0.00890, 0.00967, 0.01047, 0.01136, 0.01239, 0.01357, 0.01491, 0.01641, 0.01816, 0.02008, 0.02210, 0.02418, 0.02641, 0.02902, 0.03206, 0.03538, 0.03899, 0.04301, 0.04766, 0.05307, 0.05922, 0.06618, 0.07403, 0.08285, 0.09270, 0.10365, 0.11574, 0.12899, 0.14343, 0.15907, 0.17591, 0.19393, 0.21312, 0.23254, 0.25193, 0.27097, 0.28933, 0.30670, 0.32510, 0.34460, 0.36528, 0.38720, 0.41043, 0.43505, 0.46116, 0.48883, 0.51816, 0.54925, 0.58220, 0.61714, 0.65416, 0.69341, 0.73502, 0.77912, 0.82587, 0.87542, 0.92345, 0.96962]]

def deathprob(age, years):  # a formula to determine the probability a given person will die, with a number of years as input 
    #negative ages = female (this is Randall's comment)
    act=[] #this is a list that will hold the relevant actuarial tables, male or female 
    if age<0: # if age is a negative number the person is female 
        act=bothtables[1] # use the second table (females)
        age=-1*age # multiply age by -1 to make it positive
    else:
        act=bothtables[0] # use the first table (males)
    while(len(act)<int(age+years+2)): # slower/bloaiter but keeps things clean (Randall's comment)
        act.append(act[-1]**0.5) # I'm not sure what this does 
    liveprob=1 
    i=0
    iage=int(age) # age as integer 
    fage=age%1 # fraction after age if it's a mixed number? maybe? 
    while i<=years-1: #advance through this formula for each year between now and the date in question 
        thisyear=(1-fage)*act[iage+i]+fage*act[iage+i+1] #the probability they will die this year is equal to this formula
        liveprob*=1-thisyear # multiply the overall probability they will survive by the probability they will survive this year 
        i+=1
    if years%1: # Amortizes risk of dying over a partial year, which is (Randall's comment)
                # 1-P(living last full year)^(year fraction) (Randall's comment)
        lastyear=(1-fage)*act[iage+i]+fage*act[iage+i+1] 
        lastyearlive=1-lastyear
        lastyearlive=lastyearlive**((years%1))
        liveprob*=lastyearlive
    return 1-liveprob # return the probability they will die i.e. 1 - the probability they wil live 

def proballdie(ages, years): # probability everyone in the list will die by a certain year, given the list "ages" and the number of years  
    probsliving=[]
    for i in ages:
        probsliving.append(1-deathprob(i, years))
    prod=1
    for i in probsliving:
        prod*=(1-i)
    return prod

def probanydie(ages, years): #returns the probability that  anyone in the list dies
    probsliving=[]
    for i in ages: 
        probsliving.append(1-deathprob(i, years))
    prod=1
    for i in probsliving:
        prod*=i
    return 1-prod

def calcexp(ages, prob, flag): #calculates life expectancy based on the ages list, the probability of dying (5, 50, 95%), and whether or not it is "flagged" as calculating the probability that all or any die 
    i=0
    for interval in (10, 1, 0.1, 0.01): #loops through the numbers at left
        probs=0
        while(probs<prob): #while the variable "probs" is less than the input probability
            i+=interval #increase i by 10, 1, .1 or .01
            if flag==0: #if we want to know the probability that the entire group will die  
                probs=proballdie(ages, i)
            else:
                probs=probanydie(ages, i) #if we want to know the probability that any member of the group will die
        i-=interval #subtract the current interval from i before returning to start the for loop again with the subtracted i 
    return i #returns a float 

ages=[] # creates an empty list that will hold the ages of  everyone you want to know about
# print sys.argv[1:]
for arg in sys.argv[1:]: #for each argument you have entered except the first one (which is the script name)
    gender=1
    years=1.0
    if arg[-1]=='m' or arg[-1]=='M': #If the last character of the argument is M or m, then the person is male and we will use their age as a positive number
        try:
            ages.append(1*float(arg[:-1])) #try adding all but the last character of the argument to the ages table. The last character indicates gender, preceding characters indicate age. 
        except:
            print "Error parsing argument", arg
    elif arg[-1]=='f' or arg[-1]=='F': #if the last character of the argument is F or f, then the person is female and we will use their age as a negative number 
        try:
            ages.append(-1*float(arg[:-1])) #try adding all but the last character of the argument, times -1 because female, to the ages table. The last character indicates gender, preceding characters indicate age. 
        except:
            print "Error parsing argument", arg
    else: #if the input appears to be neither a male or female person with the age, it is probably the time period we want to know about
        try:
            years=float(arg)
            break
        except:
            print "Error parsing argument", arg

# shows user how to enter input correctly if they do it wrong
if not sys.argv[1:]:
    print "The format is 'actuary.py 15m 80f 23', with a list of ages and a number of years to run the projections."
    raise SystemExit
if not ages:
    print "No ages specified.  Format is 12m, 17f, etc."
    raise SystemExit

# print "Ages:", ages
# print "Years:", years

(datetime.date.today()+datetime.timedelta(days=365.242191*1)).year #adding date object to a timedelta object to get a date object. finds its year.  does ??? with it 
someone_years=[calcexp(ages, 0.05, 1), # this returns a list of floats, probably. Or strings???? used as strings below
               calcexp(ages, 0.5, 1),
               calcexp(ages, 0.95, 1)]
someone_dates=[(datetime.date.today()+datetime.timedelta(days=365.242191*someone_years[0])).year, # takes the above numbers and uses them to calculate a date based on today's date + total time. 
               (datetime.date.today()+datetime.timedelta(days=365.242191*someone_years[1])).year,
               (datetime.date.today()+datetime.timedelta(days=365.242191*someone_years[2])).year]
print "There is a 5%  chance of someone dying within", someone_years[0], "years (by", str(someone_dates[0])+")." #concatenates to avoid automatic space; must convert to string first. 
print "There is a 50% chance of someone dying within", someone_years[1], "years (by", str(someone_dates[1])+")."
print "There is a 95% chance of someone dying within", someone_years[2], "years (by", str(someone_dates[2])+")."
print ""

if len(ages)>1: #only makes sense to do an everyone statement if there are multiple people. 
    everyone_years=[calcexp(ages, 0.05, 0),
                   calcexp(ages, 0.5, 0),
                   calcexp(ages, 0.95, 0)]
    everyone_dates=[(datetime.date.today()+datetime.timedelta(days=365.242191*everyone_years[0])).year,
                   (datetime.date.today()+datetime.timedelta(days=365.242191*everyone_years[1])).year,
                   (datetime.date.today()+datetime.timedelta(days=365.242191*everyone_years[2])).year]
    print "There is a 5%  chance of everyone dying within", everyone_years[0], "years (by", str(everyone_dates[0])+")."
    print "There is a 50% chance of everyone dying within", everyone_years[1], "years (by", str(everyone_dates[1])+")."
    print "There is a 95% chance of everyone dying within", everyone_years[2], "years (by", str(everyone_dates[2])+")."


if years: # if the user has input year 
    yearword="years" 
    if years==1: # changes from plural to singular if "years" is 1, so it says "1 year" instead of "1 years"
        yearword="year"

    print ""
    if years>datetime.date.today().year: # Program assumes years under current year are a number of years, and years over current year refer to the date. If input years is greater than the current year...
        years=years-datetime.date.today().year #...recalculate the "years" variable to be the number of years in the future that year is
    if len(ages)>1: #if there is more than one person being analyzed, we will look at the probability of everyone dying 
        p=100*proballdie(ages, years) # converts probability into a percentage by multiplying by 100 
        printable="" # the percentage we will print out 
        if p<0.001: # if the percentage is really low/almost impossible 
            printable="<0.001"
        elif p>99.99: # if the percentage is really high/almost guaranteed 
            printable=">99.99" 
        else:
            printable=str(p)[:5] # if the percentage is not at one of the above extremes we want to see the actual percentage in our output
        print "Probability of all dying in", years, yearword+":  ", printable+"%" #outputs the info in an easily readable format
    p=100*probanydie(ages, years) #regardless of how many people there are we will want to know the probability anyone dies 
    printable="" # the percentage we will print out 
    if p<0.001:
        printable="<0.001" # if the percentage is really low/almost impossible
    elif p>99.99:
        printable=">99.99" # if the percentage is really high/almost guaranteed 
        print p # I don't know why he is choosing to do this, it seems odd/inconsistent with rest of program 
    else:
        printable=str(p)[:5] # convert p to a string and assign the first 5 characters to printable 
    print "Probability of a death within", years, yearword+":", printable+"%"  #outputs the info in an easily readable format
raise SystemExit #leaves the program 

