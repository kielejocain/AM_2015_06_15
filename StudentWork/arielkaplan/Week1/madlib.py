# Madlibs created with article at http://www.npr.org/sections/thetwo-way/2015/06/15/414568713/texas-braces-for-heavy-rain-as-tropical-wave-gathers-steam-in-gulf

article = ""

place1 = raw_input("Give the name of a place. >> ")
verb1 = raw_input("Give a verb. >> ")
noun1 = raw_input("Give a plural noun. >> ")
authority = raw_input("Give an authority figure. >> ")
noun2 = raw_input("Give a noun. >> ")
place2 = raw_input("Give another place. >> ")
verb2 = raw_input("Give another verb. >> ")
noun3 = raw_input("Give another noun. >> ")

article += "Parts of " + place1 
article += " have barely had time to " + verb1
article += " from the last round of flooding " + noun1
article += " but " + authority + " is predicting that there's more to come this week."
article += " " + authority
article += " says a tropical " + noun2
article += " that is gathering steam in " + place2
article += " will " + verb2
article += " anywhere from 5 to 10 inches of " + noun3 + "."

print article
