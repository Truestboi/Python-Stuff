word = input("Type a word for someone to guess: ")

# Converts the word to lowercase
word = word.lower()

blanks = []
for i in range(len(word)):
	blanks.append('_')
print(' '.join(blanks))

# Checks if only letters are present
if(word.isalpha() == False):
	print("That's not a word!")
	word = input("Type a word for someone to guess: ")
# Some useful variables
guesses = []
maxfails = 7

#If guess matches a letter in the word, fill in that word
while maxfails > 0:
	guess = input("Guess a letter: ")
	if guess in word:
		for i in range(len(word)):
			if guess == word[i]:
				blanks[i] = guess
			if guess == word:
				print("You guessed the word: %s!" %(word))
				exit()
		print(' '.join(blanks))
		if blanks[i] != '_':
			print("You guessed the word: %s!" %(word))
			exit()
	else:
		maxfails -= 1
		print("Sorry, that's not right. %s tries remaining!" %(maxfails))
		print(' '.join(blanks))
else:
	print("You lose! The word was %s" %(word))
if blanks[i] != '_':
	print("You guessed the word: %s!" %(word))
if guess == word:
	print("You guessed the word: %s!" %(word))
