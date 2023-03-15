########################################################################
# First we learned For loops, now lets talk about While loops!
########################################################################

# A while loop is much like a for loop, just with some extra tweaks that can be handy for some things and annoying for others. They will generally look like this:
# while (True):
#     # Do something

# This says that, while true, run the code inside like you would a for loop. This is really handy because, with a while true loop, it will run until the program is killed.
# So, if you have something that you would want to run FOREVER, it is easier to do with a while loop than a for loop!
# You can also use it like a for loop, but I don't think it looks quite as clean:

number = 0                  # Start a variable at 0
while (number != 5):        # If the variable IS NOT EQUAL to 5, run another loop
    print("I love Python")
    number = number + 1     # Increase the variable by one. This is what a for loop does, we are just doing it manually
print("END LOOP")

# So it can be used just like a for loop, but instead of running X amount of times, it runs until a condition is met. For example:
# while (0 == 1):
#     # Do Something

# This is based on a condition that will NEVER BE MET, so it will run forever.

########################################################################
# Write your own while loop that counts all the way to 10
########################################################################

# HERE

########################################################################
# Write your own for loop that runs forever and see what happens!
# HINT: If it is running forever, the best way to stop it is to click in the terminal window and press CTRL+C (which is the shortcut for copy) and it will kill the program.
########################################################################

# HERE

# Great! You now know the basics behind while loops! Although, in there I started talking about conditions, which may not have made a ton on sense. Lets talk about those next!