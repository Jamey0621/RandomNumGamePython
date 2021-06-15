#This is a number guessing game
import random
#After import lets set up something to keep trck of the guesses made
guessesTaken = 0
# lets get the players info
print('Why hi there my name is Jamey and your playing a guess that number game! Whats you Name??')
PlayerName = input()
#lets set the random number between 1 and 100 at random
number = random.randint(1, 100)

#nice now lets start the game with getting the users guesse
print('Well,' + PlayerName + ' I am thinking of a number between 1 and 100 lets see if you can get it?')
#lets get some ruels going the player has 6 trys to guess the number
for guessesTaken in range(6):
    #get the users guess
    print('Take a guess')
     #store the guess so we can compair it to the number
    guess = input()
    guess = int(guess)
#lets get some logic for the guess could of used a switch statment but this will work
    if guess < number:
        print('Your to low bud!')

    if guess > number:
        print('Your number is to high bud!')

    if guess == number:
        break
#lets get the number of times the user had guessed and display
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Great Job' + PlayerName + 'You guesses my number in ' + guessesTaken + 'guesses!')


if guess != number:
    print('Wow ' + PlayerName + 'you need some help the number i was thinking of was ' +number+'!')

#yay for programming 