#Question 3



###Objective: The aim of this assignment is to explore the random package in Python and understand how it can be used with loops to introduce randomness into your programs.

#Task 1

####Random Choice Game Create a game where a player has a list of items. They have to guess which item in the list was selected. Use random.choice() to select the item and take the user's guess via input. Provide feedback on whether they guessed correctly or not keep them playing until they guess correctly.


print("="*60)

import random ##import random module

our_list = ["football","basketball", "baseball"] ##original List
our_choice = random.choice(our_list) ###list being randomize

print(our_list) ###print out original list
while True:
    my_choice = input("Please pick a sport from the list above ") ###propompt user to guess.

    print("Random sport selected was", our_choice) ##to provide a sense of transparency, show the system random choice.

    if my_choice == our_choice: ###evaluating if your choice and system are the same.
        print("Congrats, you selected the correct sports") ###if so, print the following message.
        break ###loop is broken and program is terminated.
    else: ### if your choice and system are not the same.
        print("Incorrect selection. Please try again") ###then print the following message

