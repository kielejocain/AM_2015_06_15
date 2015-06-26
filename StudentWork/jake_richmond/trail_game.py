from sys import exit

class Area(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, area_map):
        self.area_map = area_map

    def play(self):
        current_area = self.area_map.opening_area()
        last_area = self.area_map.next_area('finished')

        while current_area != last_area:
            next_area_name = current_area.enter()
            current_area = self.area_map.next_area(next_area_name)

        current_area.enter()    

class Death(Area): 

    def enter(self):
        pass

class MountainTop(Area):

    def enter(self):
        print "You and your wagon train are standing on top of the"
        print "endless mountain top known as Big Mountain Go Boom."
        print "Your leader has died of Typhoid Fever and a nasty case of"
        print "Dysentary. Now the wagon train looks to you as their fearless"
        print "leader. You want to make it to the ocean and board a magnificent"
        print "aircraft carrier that will take you to Paradise."
        print "\n"
        print "You have a couple of choices to decide what is next on your"
        print "journey across the country."
        print "Choice #1 is everyone climbs in the wagon and holds on for"
        print "dear life while screaming 'MURICA!!!!! all the way down the"
        print "mountain sliding to a stop giving everyone high fives." 
        print "Choice #2 is slowly traverse your way safely down"
        print "the mountain and make it to the bottom safely."
        
        choice = raw_input("> ")

        if choice == "1":
            print "Woooooo thats was awesome!!! All the weak people died on"
            print "the way down the mountain and now you have a group of warriors!!"
            return 'river'

        elif choice == "2":
            print "The strong and athletic people starved to death"
            print "during the slow pace waiting for the old geezers"
            print "to come down the mountain."
            return 'river'

        else:
            print "You are an idiot that was not an option! This will self destruct in 5 4 3 2 1 BOOOOOOOOOMMMM"
            return 'death'

class River(Area):

    def enter(self):
        print "You approach raging whitewater filled with guppys. Do you try to cross the raging water?"
        print "While you are standing there and pondering this you see that there is a calmer section down river"
        print "about 2,000 metric yards. You walk down there and take a look and see a giant crocodile swimming"
        print "around with huge, razor sharp, metal teeth chomping at everything around him. What do you do?"
        print "1 walk back and try to cross the raging whitewater or 2 cross where the giant crocodile is?"
        print " You now must choose between 1 or 2!!"

        choice = raw_input("> ")

        if choice == "1":
            print "You slowly approach the raging water... Then you kick the ox in his ass and just go for it!!!!"
            print "All the sudden the ox start making crazy weird noises and the water starts to turn red!"
            print "You start thinking what is going on!? Well dumbass those guppys turned out to be pirahnas!"
            print "Way to kill your people! YOU SUCK"
            return 'death'

        elif choice == "2":
            print "You cautiously approach the water and look for the big scary crocodile. He comes flying out of"
            print "The water and into the air with green and red slimy things hanging out of his mouth!!! You think"
            print "to yourself I think those are intestines or something's stomach! Well it's too late now. Let's do"
            print "this. You slap your ox on the ass and tell him to get on with it. He slowly but surely moves into the"
            print "water one step at a time. All of the sudden the crocodile turns to see what is disrupting the water."
            print "You think to yourself oh shit I am a goner, he is going to eat all of us! The crocodile starts swimming"
            print "towards you faster and faster! Then you hear a huge crunch and open your eyes and can't believe what"
            print "you see!? The damn crocodile is a vegetarian and just bit into some corn you had sitting next to you."
            return 'forest'

        else:
            print "You are an idiot that was not an option! This will self destruct in 5 4 3 2 1 BOOOOOOOOOMMMM"
            return 'death'

class Forest(Area):

    def enter(self):
        print "Wow you made it this far!!! You're wagon people rejoice! After 200 days you know come up to a dense dark"
        print "forest. There is a lot of strange scary noises coming from the trees. OMG!!! What if they are blood thirsty"
        print "Spider Monkeys!!!?? What ever shall we do? Shall you send one of the kids in to scout it out? How about we"
        print "send in one of the donkeys to see if it gets eaten? Make your pick: Choice 1 or Choice 2?"

        choice = raw_input("> ")

        if choice == "1":
            print "What is wrong with you why would you send a poor innocent child into some big scary forest!? I can't"
            print "believe you would do something as atrocious as that!!!! You are a sick human being! But whatever you gotta"
            print "do to survive right? Kids eat a lot of food anyway and aren't good for anything. You probably would have"
            print "eaten him anyways, if worse came to worse."
            return 'ocean'

        elif choice == "2":
            print "Really?! You sent in a damn donkey? What the hell is a donkey going to do? Do you smell that? Something"
            print "is burning... I wonder what it is... You wander towards the smell and see that the donkey laid in a fire pit"
            print "and killed itself. You think to yourself HEY!? That smells good! You take a bite of the donkey and it gives"
            print "Dysentary and you poop yourself to death!!"
            return 'death'

        else:
            print "You are an idiot that was not an option! This will self destruct in 5 4 3 2 1 BOOOOOOOOOMMMM"
            return 'death'



class Ocean(Area):

    def enter(self):
        print "Awesome you made it to the ocean!!! You're almost home free!!! You take a look around and notice that"
        print "there is a bunch of people standing around and taking pictures of the beautiful scenery. Someone walks"
        print "up to you and asks if you want to take a selfie..... You punch them in the face! What is this crazy mad"
        print "magic people are doing with these little square shiny boxes!? You see a boat on the horizon. What do you do?"
        print " 1 do you run to the boat to get away from these demons or 2 do you run back to the mountain?"
 
        choice = raw_input("> ")

        if choice == "1":
            print "You ran like a speeding Gazelle into the ocean and then realized you can't swim! Oh Shit!!!!"
            return 'death'

        elif choice == "2":
            print "You turn and run back into the forest screaming like a wild banshee. You run back through the river"
            print "giving the crocodile a high five while flipping over the river. You reach the bottom of the mountain"
            print "and start your ascent. You sprout wings and fly all the way to the top and land. You walk around feeling"
            print "relieved and then you trip and fall and hit your head and forget everything."
            print "\n"
            print "\n"
            return 'mountain_top'

        else:
            print "You are an idiot that was not an option! This will self destruct in 5 4 3 2 1 BOOOOOOOOOMMMM"
            return 'death'

class Map(object):

    area = {
        'mountain_top': MountainTop(),
        'river': River(),
        'forest': Forest(),
        'ocean': Ocean(),
        'death': Death()




    }
    def __init__(self, start_area):
        self.start_area = start_area

    def next_area(self, area_name):
        val = Map.area.get(area_name)
        return val

    def opening_area(self):
        return self.next_area(self.start_area)


a_map = Map('mountain_top')
a_game = Engine(a_map)
a_game.play()