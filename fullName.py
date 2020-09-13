# fullName.py - Lab2
# Author: Daeshaun Morrison
# Date: 9/1/2020

# If "continueNaming" = true, it keeps asking user to input their name.
# If false, program stops

continueNaming = True
# While continueNaming is true...ran the program
while continueNaming :
    #User inputs their first & last name
    firstName = input("What's your first name?")
    lastName = input("What's your last name(s)?")
    # logs it
    print(f"{lastName}, {firstName}")
    
    # Ask if they want to continue
    noOrYes = input(f"Do you want to continue? (Y/N)")
    
    # If yes or any other programmed equivalent, "continueNaming = True",
    # which contines the program
    if noOrYes.lower().startswith('y'):
        continueNaming = True
        
    # If no or any other programmed equivalent, "continueNaming = false",
    # ending the program   
    elif noOrYes.lower().startswith('n'):
        continueNaming = False
        
    elif noOrYes != "Y" or "N":
        noOrYes = input(f"That's not an answer, do you want to continue? (Y/N)")
    #else: noOrYes = input(f"That's not answer, do you want to continue? (Y/N)")
