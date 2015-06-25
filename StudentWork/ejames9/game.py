""" You awaken in your bed, which is currently functioning as a raft, and you are swiftly floating downstream. You navigate the river as best you can, trying to avoid
waterfalls and other dangers. If you successfully navigate through all Forks of the river, you will enter the Ocean of Enlightenment. If you fail any of the tests, or choose
your path unwisely, you will awaken in a pool of your own sweat. """

from random import randint
from sys import exit
import death

class Fork(object):

    def enter(self):
        print "Not yet config'd."
        exit(1)



class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_fork = self.scene_map.awake()
        last_fork = self.scene_map.next_fork('Last Fork')

        while current_fork != last_fork:
            next_fork_name = current_fork.enter()
            current_fork = self.scene_map.next_fork(next_fork_name)


class LastFork(Fork):

    def enter(self):
        print "'Well, Well, Well!' Says, the voice in your head. 'What a pleasant"
        print "surprise! It looks as though I may have underestimated you! Either"
        print "that, or you\'re just incredibly lucky! Be as it may, you\'d be"
        print "better off with luck on your side, for your final test!' As he"
        print "spoke these words, I entered a dense fog. Up ahead, I could see"
        print "That the river forked again, this time, with 3 options. Unfortunately,"
        print "though, the fog was too dense to see beyond that. The voice spoke again,"
        print "'You must choose your path wisely. Two of the three forks lead to very"
        print "steep falls. The third will lead to the Ocean of Enlightenment!"
        print "Good luck! And may the force be with you. You must choose the left, right"
        print "or middle path.'"
        fog = {'left': 1, 'right': 2, 'middle': 3}
        ooe = randint(1, 3)
        ooe = fog[ooe]
        choice = raw_input(">> ")
            if choice == ooe









class Death(Fork):

    def enter(self):
        death.death()


class ThirdFork(Fork):

    def enter(self):
        print "'I bet you are pretty pleased with yourself!', Says the voice in your head. 'Don\'t get cocky, your next test won\'t be so easy!'"
        print "You travel along the river for what seems like an eternity, when you come to another fork. On the left, There seems to be another"
        print "waterfall. On the right, there is a family of large Trolls bathing in the river. By now, you've learned to avoid waterfalls, so you"
        print "approach the Trolls. The largest, meanest and ugliest one stops you. 'Hold on there!', He grumbles. No one passes without playing a"
        print "little game first. If you win, you may pass. If you lose, we'll send you over the Falls!, He says. Heads or Tails?! He asks, pulling"
        print "out a strange, but 2 sided coin. 'We are playing best 2 of 3', he informs me."

        game = {'heads': 1, 'tails': 2, 'wins': 0, 'loss': 0}
        wins = game['wins']
        losses = game['loss']

        while wins < 2 and losses < 2:
            answer = randint(1, 2)
            choice = raw_input("heads/tails?\n>> ")
            choice = game[choice]
            if choice == answer:
                wins += 1
                print "'Wow you\'re lucky! That\'s %d wins, and %d losses, %d to go!'" % (wins, losses, (2 - wins))
            else:
                losses += 1
                print "'You are not such a lucky fellow! That's %d for me, and %d for you!'" % (losses, wins)
        if wins == 2:
            print "'Wow! you are extremely lucky! I don\'t normally do this, but since you are such a nice, lucky fellow,"
            print "We\'ll let you pass.' And with those words, and a crooked smile, He waved me on. The trolls stared"
            print "blankly at me as I passed."
            return 'Last Fork'
        else:
            print "You are truly, very unlucky! We will not be letting you pass today, I\'m afraid."
            print "And as the river does not travel backward, I had no choice but to take the other fork. 'Tough luck!'"
            print "said the voice in my head."
            return 'Death'

class SecondFork(Fork):

    def enter(self):
        print "As your bed slowly approaches the lock, Rufus the knight addresses you. 'You have chosen wisely' He states, monotonously."
        print "'Now, if you'd like to proceed beyond this lock, you must answer this riddle correctly.', He asserts."
        print "'I Run, though I have no legs. I may possess no heat, yet I have steam. I have no mouth to speak of, but from far away you can still hear me roar.'"
        print "'What am I?'"
        guess = 1
        while guess < 3:
            answer = raw_input(">> ")
            if answer == 'a waterfall' or answer == 'waterfall':
                print "That's right! Well done! You may Pass!"
                return 'Third Fork'
            else:
                print "Nope. Try again."
                guess += 1
        print "You fail! You have no choice now but to take the other fork in the river. He says with a sinister grin."
        print "Reluctantly, you set off toward the falls."
        return 'Death'



class FirstFork(Fork):

    def enter(self):
        choice = '0'
        print "'You are very brave!', the voice continues. With that, you come to a fork in the river with 2 choices. On the right,"
        print "you see that the river leads directly to a deadly waterfall. On the left, the river comes to a lock that is controlled"
        print "by a Knight. Would you like to go right or left?"
        while choice != 'r' or choice != 'l':
            choice = raw_input("'l' or 'r'>> ")
            if choice == 'r':
                return 'Death'
            elif choice == 'l':
                return 'Second Fork'
            else:
                print "You may be too stupid to play this game."


class Awake(Fork):

    def enter(self):
        print "Suddenly feeling cold and wet, You awaken in your bed, which is floating rapidly down a swiftly moving river. A voice in your mind speaks to"
        print "you, saying, 'Pass 3 tests, and you will reach the Ocean of Enlightenment, where you will atain omnipotence!  Will you try?'"
        choice = raw_input("Y/N\n>> ")
        if choice == 'y':
            return 'First Fork'
        elif choice == 'n':
            print "'You are quite lame!' The voice in your head informs you. 'Goodbye.', He says. Before you've heard the last echoe of his voice,"
            print "you awake in your bed, back in your bedroom, soaked in sweat and feeling quite lame."
            exit(1)
        else:
            print "I couldn't understand your response, please try again."
            return 'Awake'


class Map(object):

    forks = {'Awake': Awake(), 'First Fork': FirstFork(), 'Death': Death(), 'Second Fork': SecondFork(), 'Third Fork': ThirdFork()}

    def __init__(self, enter_fork):
        self.enter_fork = enter_fork

    def next_fork(self, fork_name):
        key = Map.forks.get(fork_name)
        return key

    def awake(self):
        return self.next_fork(self.enter_fork)


map = Map('Awake')
game = Engine(map)
game.play()
