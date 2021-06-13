import random


# -1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# Word list to what users can guest
word_list = ["rabbit", "hamster", "betta"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}')

display = []
word_length = len(chosen_word)
for _ in range(word_length): 
    display += "_"
print(display) 

# -2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

# -3 - Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)