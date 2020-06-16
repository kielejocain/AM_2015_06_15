from collections import OrderedDict


class Engine(object):
    """Drives the game"""

    def play(self):
        """Builds and runs pet"""
        done = False
        while not done:
            name = raw_input("What would you like to name your pet? > ")
            my_pet = MyPetAlpha(name)
            while my_pet.alive:
                print my_pet
                my_pet.next_move()
                done, evolve = my_pet.check()
                if evolve:
                    self.evolve_pet(my_pet)

    def evolve_pet(self, other):
        """Evolves pet when conditions met"""
        if other.level == "baby":
            name = other.name
            hunger = other.hunger
            boredom = other.boredom
            happiness = other.happiness
            del other
            other = MyPetBeta(name, hunger, boredom, happiness)


class BasePet(object):

    max_hunger = 10
    max_boredom = 10
    max_happiness = 10
    max_strength = 10

    def __init__(self, name):
        self.alive = True
        self.name = name
        self.hunger = 0
        self.boredom = 0
        self.happiness = 10
        self.strength = 0

    def check(self):
        """Checks stats for end_game conditions, evolution."""
        if self.hunger > self.max_hunger:
            return self.game_end("hunger"), False
        elif self.boredom > self.max_boredom:
            return self.game_end("boredom"), False
        elif self.happiness <= 0:
            return self.game_end("happiness"), False
        else:
            return False, self.evolve_check()

    def evolve_check(self):
        return False

    def game_end(self, reason):
        """Ends the game"""
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
            return True
        return False

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
        print "How high can you jump, %s?" % self.name
        self.boredom += 1
        self.happiness -= 2
        self.hunger += 3
        if self.strength < self.max_strength:
            self.strength += 1
        self.check()

    def mine(self):
        print "Mining gold..."
        self.boredom += 2
        self.happiness -= 3
        self.hunger += 4
        if self.strength < self.max_strength - 1:
            self.strength += 2
        else:
            self.strength = self.max_strength
        self.gold += 10
        self.check()


class MyPetAlpha(BasePet):
    """First-level pet"""

    def __init__(self, name):
        self.alive = True
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

    def __str__(self):
        output = "\n%s: %s pet\n" % (self.name, self.level)
        output += "-" * 20 + "\n"
        output += "Hunger: |%s%s|%d\n" % (
            self.hunger * "==",
            (self.max_hunger - self.hunger) * "  ",
            self.hunger
            )
        output += "Boredom: %d / %d\n" % (self.boredom, self.max_boredom)
        output += "Happiness: %d / %d\n" % (self.happiness, self.max_happiness)
        output += "Strength: %d\n" % (self.strength)
        return output

    def evolve_check(self):
        return self.strength >= 10 and self.happiness >= 7


class MyPetBeta(BasePet):
    """First evolution of pet"""

    max_strength = 100

    def __init__(self, name, hunger, boredom, happiness):
        self.alive = True
        self.name = name
        print "(>^v^)>\n<(^v^<)\n" * 4
        print "%s is evolving!" % self.name
        self.level = "teen"
        self.hunger = hunger
        self.boredom = boredom
        self.happiness = happiness
        self.strength = 10
        self.gold = 0
        self.activities = OrderedDict([
            ("Eat", self.feed),
            ("Play", self.play),
            ("Work", self.earn)
            ])

    def __str__(self):
        output = "\n%s: %s pet\n" % (self.name, self.level)
        output += "-" * 20 + "\n"
        output += "Hunger: %d / %d\n" % (self.hunger, self.max_hunger)
        output += "Boredom: %d / %d\n" % (self.boredom, self.max_boredom)
        output += "Happiness: %d / %d\n" % (self.happiness, self.max_happiness)
        output += "Strength: %d\n" % (self.strength)
        output += "Gold: %d" % self.gold
        return output

game = Engine()
game.play()
