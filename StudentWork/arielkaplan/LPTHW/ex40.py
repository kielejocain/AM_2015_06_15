class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

	def __repr__():
		"""If you ask for the object, it'll just say what class it is,
		and where it is in memory. This tells the object how to represent
		itself."""
		pass

happy_bday = Song(["Happy birthday to you",
				   "I don't want to get sued",
				   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"])

marys_lamb = Song(["Mary had a little lamb",
				   "(Little lamb, little lamb)",
				   "Mary had a little lamb",
				   "Its fleece was white as snow."])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

marys_lamb.sing_me_a_song()