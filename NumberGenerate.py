import random

top_of_range = input("Enter a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number greater than 0 ')
        quit()

else:
    print('Please enter a number and Try next time')
    quit()

randomNumber = random.randint(0, top_of_range) #if random.randint(0,11) then 11 is also show 
#if random.randrange(0,11) then 11 is not shown 
print(randomNumber)
guesses = 0;

while True:
    guesses +=1
    user_guess = input("Make a Guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please enter a number and Try next time')
        continue

    if user_guess == randomNumber:
        print("You got it! ")
        break
    elif user_guess > randomNumber:
        print("you were above the number")
    else:
        print("you were below a number")

 #print("you got it:", guesses, "guesses") and print("you got it:" + str(guesses) + " guesses") same 
   # print("you got it in", guesses, "guesses")  convert integer guesses  ot string guesses
print("you got it: " + str(guesses) + " guesses")