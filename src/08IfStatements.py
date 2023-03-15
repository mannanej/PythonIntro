########################################################################
# Lets learn about something programmers can't live without; IF Statements!
########################################################################

# An if statement is really a coders bread and butter. Most things can't get done without them. Here is what they will generally look like:
# if (Some Condition):
#     # Do Something

# Simple example:
if (10 < 20):       # If 10 is less than 20
    print("TRUE")

# With an if statement comes whats called an else statement! This is like a "if this do this, if NOT, do this". So:
if (10 > 20):       # If 10 is greater than 20
    print("TRUE")
else:
    print("FALSE")

########################################################################
# Write an if statement that will print TRUE if HOURS is bigger than MINUTES, and print out the value of HOURS if not
########################################################################

# HERE


# IF statements can also be extended as long as you'd like with multiple elif blocks! So:
MILES = 100
FEET = 100000
if (MILES > FEET):
    print("MILES IS BIGGER")
elif (MILES == FEET):
    print("THEY ARE THE SAME")
elif ((MILES + FEET) == 100):
    print("WE GOT SOME BIG NUMBERS")
else:
    print("I GOT CONFUSED")


########################################################################
# Play around with the block above. See if you can add more statements!
########################################################################


# You can also do whats called a "Nested If Statement" where you stack conditions on top of each other. For example:
LEFT = 5
RIGHT = 10
if (RIGHT > LEFT):
    if (RIGHT == 10):
        if (LEFT == 5):
            if ((RIGHT + LEFT) == 15):
                print("That was a LOT of nested ifs! Usually, you don't want to nest them that many times!")

# Of course, each nested if can have its own set of elif and elses, and it can get REALLY messy!

########################################################################
# Play around with the block above. See if you can add more statements to the nested ifs!
########################################################################

# WONDERFUL! As far as I can tell, you now have most of the basics. There is still a lot to learn and I may add more in the future, but for now, keep learning on your own!
# Or, just as well, ask questions!!!