#assignment 1
import random

str=input("enter a string")
digit=letter=0
for ch in str:
    if ch.isdigit():
        digit+=1
    elif ch.isalpha():
        letter+=1
    else:
       continue
print("letter:",letter)
print("digit:",digit)


#assignment2
number=random.randrange(1,10)
player_name = input("Hello, What's your name?")
number_of_guesses = 0
print('okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))


