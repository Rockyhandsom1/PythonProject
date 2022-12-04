
playing = input("do you want to play?")
print("playing")

if playing.lower() !="yes":  
    # (if no then quit otherwise output this below result)
    # (playing.lower means convert to lower case when user type even a upper letter)
    #  (playing.upper means convert to upper case when user type even a lower leter)
        quit()
print("okay! lets play :)")
Score = 0;

answer = input("what does CPU stand for?")
if answer.lower() == "central processing unit":
    print('correct!')
    Score += 1; # or Score = Score + 1 is same
else:
     print('please input correct answer! This is wrong!')

answer = input("what does MU stand for?")
if answer.lower() == "memory unit":
    print('correct!')
    Score += 1; # or Score = Score + 1 is same
else:
     print('please input correct answer! This is wrong!')

answer = input("what does CU stand for?")
if answer.lower() == "control unit":
    print('correct!')
    Score += 1; # or Score = Score + 1 is same
else:
     print('please input correct answer! This is wrong!')

answer = input("what does RU stand fro?")
if answer.lower() == "register unit":
    print('correct!')
    Score += 1; # or Score = Score + 1 is same
else:
     print('please input correct answer! This is wrong!')

answer = input("what does BIOS stand for?")
if answer.lower() == "basic input output":
    print('correct!')
    Score += 1; # or Score = Score + 1 is same

else:
     print('please input correct answer! This is wrong!')

     print("You Got " + str(Score) + " Questions Correct!")
     print("You Got " +  str((Score / 5) * 100) + "%")