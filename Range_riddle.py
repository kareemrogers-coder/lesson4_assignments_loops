### Question 1


#Task 1: Every Other Day Write a program that prints each day of the week, but only if that day is on an even index.

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#print(len(days_of_week)) # the len gives you the the lenth of the list. in this case seven.

print('='*60)
print('='*60)


print("Original index list: ")

for index in range(len(days_of_week)): 
        
        print(index,days_of_week[index])

print('='*60)


for index in range(len(days_of_week)): ###created and index variable, that using the range function with a constriants length end point base on the lenght of days_or_weeks.
    if index % 2 == 0: # if the index falls on a number that have no remainder, print this results and display section of the list that correspond with that index number.
        print("The following index ", index,"which is linked to ", days_of_week[index], "falls on a even number index")

