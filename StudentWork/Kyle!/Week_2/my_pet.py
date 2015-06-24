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
                done = my_pet.check()
                if my_pet.evolve_check():
                    my_pet = self.evolve_pet(my_pet)

    def evolve_pet(self, other):
        """Evolves pet when conditions met"""
        if other.level == "baby":
            name = other.name
            hunger = other.stats['Hunger'][0]
            boredom = other.stats['Boredom'][0]
            happiness = other.stats['Happiness'][0]
            return MyPetBeta(name, hunger, boredom, happiness)


class BasePet(object):

    def __init__(self, name):
        self.alive = True
        self.name = name

    def __str__(self):
        output = "\n%s: %s pet" % (self.name, self.level)
        if self.level != 'baby':
            output += (58 - len(output)) * " " + "Gold:"
            output += (5 - len(str(self.gold))) * " " + str(self.gold)
        output += "\n" + "-" * 68 + "\n"
        for stat in self.stats:
            output += self.make_bar(stat)
        return output

    def make_bar(self, stat):
        curr, max = self.stats[stat]
        percent = 50 * curr / max
        return "%s:|%s%s|%s\n" % (
            stat + (10 - len(stat)) * " ",
            "=" * percent,
            " " * (50 - percent),
            (4 - len(str(curr))) * " " + str(curr)
            )

    def check(self):
        """Checks stats for end_game conditions, evolution."""
        if self.stats['Hunger'][0] > self.stats['Hunger'][1]:
            return self.game_end("hunger")
        elif self.stats['Boredom'][0] > self.stats['Boredom'][1]:
            return self.game_end("boredom")
        elif self.stats['Happiness'][0] <= 0:
            return self.game_end("happiness")
        else:
            return False

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
        self.alive = False
        if raw_input("> ").lower() not in ['y', 'yes']:
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
        self.stats['Hunger'][0] = 0
        if self.stats['Happiness'][0] < self.stats['Happiness'][1] - 2:
            self.stats['Happiness'][0] += 2
        else:
            self.stats['Happiness'][0] = self.stats['Happiness'][1]

    def play(self):
        print "Tag, you're it!"
        self.stats['Boredom'][0] = 0
        if self.stats['Happiness'][0] < self.stats['Happiness'][1]:
            self.stats['Happiness'][0] += 1
        self.stats['Hunger'][0] += 2

    def lift(self):
        print "How high can you jump, %s?" % self.name
        self.stats['Hunger'][0] += 3
        self.stats['Boredom'][0] += 1
        self.stats['Happiness'][0] -= 2
        if self.stats['Strength'][0] < self.stats['Strength'][1]:
            self.stats['Strength'][0] += 1

    def mine(self):
        print "Mining gold..."
        self.stats['Hunger'][0] += 4
        self.stats['Boredom'][0] += 2
        self.stats['Happiness'][0] -= 3
        if self.stats['Strength'][0] < self.stats['Strength'][1] - 1:
            self.stats['Strength'][0] += 2
        else:
            self.stats['Strength'][0] = self.stats['Strength'][1]
        self.gold += 10


class MyPetAlpha(BasePet):
    """First-level pet"""

    def __init__(self, name):
        self.alive = True
        self.level = "baby"
        self.name = name
        print "%s is hatching!" % self.name
        self.stats = OrderedDict([
            ("Hunger", [9, 10]),
            ("Boredom", [0, 10]),
            ("Happiness", [10, 10]),
            ("Strength", [0, 10])
        ])
        self.activities = OrderedDict([
            ("Eat", self.feed),
            ("Play", self.play),
            ("Exercise", self.lift)
            ])

    def evolve_check(self):
        return self.stats['Strength'][0] == 10 and self.stats['Happiness'][0] >= 7


class MyPetBeta(BasePet):
    """First evolution of pet"""

    max_strength = 100

    def __init__(self, name, hunger, boredom, happiness):
        self.alive = True
        self.name = name
        print "(>^v^)>\n<(^v^<)\n" * 4
        print "%s is evolving!" % self.name
        self.level = "teen"
        self.stats = OrderedDict([
            ("Hunger", [hunger, 10]),
            ("Boredom", [boredom, 10]),
            ("Happiness", [happiness, 10]),
            ("Strength", [10, 100])
        ])
        self.gold = 0
        self.activities = OrderedDict([
            ("Eat", self.feed),
            ("Play", self.play),
            ("Work", self.mine)
            ])

game = Engine()
game.play()
