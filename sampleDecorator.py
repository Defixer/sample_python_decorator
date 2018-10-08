
def talk(func):
	def shout(wordy):
		print("HOY" + func(wordy))
	return shout

@talk
def your_name(wordy):
	word = " {}".format(wordy).upper() + "!"
	return word

your_name("kups")