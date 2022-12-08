import random
lives = 9
words = ["amaze","fairy","diary","Eevee","sorry"]
secret_word = random.choice(words)
clue = list("?????")
heart_symbol = u'\u2764'
guess_word_currectly = False
def update_clue(guess_letter,secret_word,clue):
    index = 0
    while index < len(secret_word) :
        if guess_letter == secret_word[index]:
            clue[index] = guess_letter
        index = index+1


while lives > 0 :
    print(clue)
    print("Your LEFT lives:" + heart_symbol * lives)
    guess = input("Press a letter or the whole word: ")
    if guess == secret_word:
        guess_word_currectly = True
        break
    if guess in secret_word :
        update_clue(guess, secret_word, clue)
    else:
        print("Incorrect,you left a life.Please try again")
        lives = lives - 1
if guess_word_currectly:
    print("You won!")
else:
    print('You lost!')
print("The word is " + secret_word)
if secret_word == "Eevee" :
    print("I like Eevee")



































        











