class Song(object):

    def __init__(self, lyrics):
	    self.lyrics = lyrics
		
    def sing_me_a_song(self):
	    for line in self.lyrics:
		    print line
			
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
				   "So I'll stop right there"])
				   
bulls_on_parade = Song(["They rally round the family",
                        "With pockets full of shells"])
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

new_lyrics = """I broke my promise on a very sharp rock
And I was possessed by something quite unfriendly
I was haunted by a demon in my sleep
That's how I learned how to survive."""
				
survival = Song([new_lyrics])

survival.sing_me_a_song()