######Basic Number Guessing Game######
#     1st and 2nd week knowledge     #
######################################

import random
my_num = random.randint(1,99)
user_num = int(input("Enter a whole number from 1 to 99:"))

while user_num != my_num :
    print
    if user_num<my_num:
        print("No, that's too low")
        user_num = int(input("Try a different number"))
    elif user_num>my_num:
        print("No, that's too high!")
        user_num = int(input("Try a different number"))
    else:
        print("That's it, you got it! My number was",my_num)
        print("That was fun.  Reset to play again.")

