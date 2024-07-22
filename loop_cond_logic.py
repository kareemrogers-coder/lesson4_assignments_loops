###Question 2


#Task 1: Loop Condition Exploration Write a while loop with a condition that will never be true (an infinite loop). Ask the user a question until their answer triggers a break statement (hint: use an if statement to evaluate their answer).


print("=="*60)

math = True ###have math while loop be True
while math: ##execute loop.
    user = input("What is 5 X 5 ? ") ###create a user input.
    if user == "25": ###create the answer
        math = False ###is answer is typed/entered, math while loop turns into False, terminating the loop.
        print("That is correct") ###along with the following message.
    else: ###else the loop will continue until correct answer is selected.
        print("Please try again")

print("=="*60)
print("=="*60)

#Task 2: Conditional Exit. Create a while loop that will terminate after 5 iterations, and each iteration you print which iteration it is on. (use a control variable)


###the following is a car search code block that cancel after 5 attempts of searching

attempts = 1

while True: ##create while to be True. this enable the input function to repeat it itself if the incorrect input is enter on the code line below.
    car_search = input("Type the word Begin to start search for vehicle ") # Create an input function, the word "Begin" must be type/entered.
    if car_search == "Begin": ##verify the correct entry is enter in the correct format.
        while attempts <= 5: ###putting a constraint on the amount of loops. 
            print("Searching for vehicle.", "Attempt # ", attempts, "...........") ###create a print function to keep track of the number of loops, or in this case attempts.
            attempts += 1 ###for eacj attempt/loop add 1 until it reachs the max constraints.
        
        print("Max attempts of 5 has been executed. Please try a different location for vehicle search") ###Once max number is reached, print the following.
        break ##then break the loop

    else: ####if incorrect entry is typed or entered. print the message below.
        print("Incorrect entry, try again... Please type the word Begin")


print("=="*60)
print("=="*60)