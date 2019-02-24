########Basic Number Guessing Game#######
#       1st and 2nd week knowledge      #
#########################################

import random
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second

my_num = random.randint(1,99)
user_num = int(input("Enter a whole number from 1 to 99:"))
tries = 1

while user_num != "my_num" :
    if user_num<my_num:
        print("No, that's too low")
        user_num = int(input("Try a different number \n \n"))
        tries +=1
    elif user_num>my_num:
        print("No, that's too high!")
        user_num = int(input("Try a different number \n \n"))
        tries +=1
    else:   
        winsound.Beep(1567,100)
        winsound.Beep(1760,100)
        winsound.Beep(1975,100)
        winsound.Beep(1760,100)
        winsound.Beep(1567,100)
        for i in range(3):
            print("###################            #################")
        print("######    That's it, you got it! My number was",my_num)
        print("######    That was fun. It only took you",tries,"tries.  Reset to play again.")
        for i in range(2):
            print("###################            #################")
        break

