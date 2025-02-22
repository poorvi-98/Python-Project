# Number Gussing Game using Python

import random
r_num = random.randint(1,100)
while True:
    try:
        u_inp = int(input("Guess the number from 1 between 100 :"))
        if u_inp<r_num:
            print("Please Enter the gretest number :")
        elif u_inp>r_num:
            print("Please Enter the smallest number :")
        else:
            print("Yes this was the correct number.")
            break
    except ValueError:
            print("Please Enter the number not the name.")
        