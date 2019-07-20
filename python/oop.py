# First oop example from LPTHW
class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy bday to you",
		   "I don't wanna get sued",
		   "So I'll stop right there"])

happy_bday.sing_me_a_song()

