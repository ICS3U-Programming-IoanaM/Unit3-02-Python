#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu
#
# Date: Oct. 5, 2022
# programs that lets you guess the randomly generated number


import random


def main():
    # variables
    user_num = int(input("Enter your guess: "))
    rand_num = random.randint(0, 9)

    # checks if user's number is the same as the random number
    if user_num == rand_num:
        print("You guessed the right number!")
    else:
        print("you guessed the wrong number :(")


if __name__ == "__main__":
    main()
