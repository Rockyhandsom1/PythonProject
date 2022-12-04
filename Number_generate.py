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
