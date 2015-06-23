from collections import OrderedDict

class MyPet(object):

    max_hunger = 10
    max_strength = 10
    max_boredom = 10
    max_happiness = 10

    def __init__(self, name):
        self.level = "baby"
        self.name = name
        print "%s is hatching!" % self.name
        self.hunger = 9
        self.strength = 0
        self.boredom = 0
        self.happiness = 10
        self.activities = OrderedDict([
            ("Eat", self.feed),
            ("Play", self.play),
            ("Exercise", self.lift)
            ])
        self.check()

    def __str__(self):
        output = "\n%s: %s pet\n" % (self.name, self.level)
        output += "-" * 20 + "\n"
        output += "Hunger: %d / %d\n" % (self.hunger, self.max_hunger)
        output += "Boredom: %d / %d\n" % (self.boredom, self.max_boredom)
        output += "Happiness: %d / %d\n" % (self.happiness, self.max_happiness)
        output += "Strength: %d\n" % (self.strength)
        return output

    def check(self):
        """Checks stats for end_game conditions, evolution."""
        if self.hunger > self.max_hunger:
            self.game_end("hunger")
        elif self.boredom > self.max_boredom:
            self.game_end("boredom")
        elif self.happiness <= 0:
            self.game_end("happiness")
        elif self.strength >= self.max_strength and self.happiness > 7:
            self.evolve()
        else:
            print self
            self.next_move()

    def game_end(self, reason):
        """Ends the game"""
        global exit
        if reason == "hunger":
            print "%s got hungry and left in search of food." % self.name
        elif reason == "boredom":
            print "%s got bored and wandered off to play." % self.name
        elif reason == "happiness":
            print "%s was so sad that they left to live on their own." % self.name
        print "Sadly, they did not return."
        print "Thanks for playing!"
        print "Try again?"
        if raw_input("> ").lower not in ['y', 'yes']:
            exit = True

    def next_move(self):
        """Decide your next move"""
        print "What would you and %s like to do?" % self.name
        for i, activity in enumerate(self.activities):
            print "%d. %s"% (i + 1, activity)
        while True:
            response = raw_input("Please enter an activity. > ")
            if response in [str(i) for i in range(1, len(self.activities)+1)]:
                self.activities[self.activities.keys()[int(response) - 1]]()
                break
            else:
                try:
                    self.activities[response.title()]()
                    break
                except KeyError:
                    print "Not a valid choice."

    def feed(self):
        print "Let's eat!"
        self.hunger = 0
        self.boredom += 1
        if self.happiness < self.max_happiness - 2:
            self.happiness += 2
        else:
            self.happiness = self.max_happiness
        self.check()

    def play(self):
        print "Tag, you're it!"
        self.boredom = 0
        if self.happiness < self.max_happiness:
            self.happiness += 1
        self.hunger += 2
        self.check()

    def lift(self):
        print "Throw the ball!"
        self.boredom += 1
        self.happiness -= 2
        self.hunger += 3
        self.strength += 1
        self.check()

    def evolve(self):
        if self.level == "baby":
            self = MyPetAlpha(self.name)


exit = False
while not exit:
    name = raw_input("What would you like to name your pet? > ")
    my_pet = MyPet(name)
