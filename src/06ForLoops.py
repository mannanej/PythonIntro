########################################################################
# We saw in a previous section what a for loop is, but now lets talk 
# about how they work!
########################################################################

# To write a simple for loop, it would look like this:
#   for i in range(10):
#       # Do Something
# So, it is saying "Do every indented line below me 10 times, one after another"

# For examnple, if I wanted to print "I love Python" 3 times, I would put:
for i in range(3):
    print("I love Python")
print("END LOOP")

# Another important tool with a for loop is that it keeps track of the number of loops it has done with the variable i. So
# it will make i=0, run the code, then i=1 and run the code, then i=2 run the code and so on.
for i in range(5):
    print("This is loop number: ", i)
print("END LOOP")
# IMPORTANT: Most coding languages, when doing a for loop or something similar, will start counting at 0 NOT AT 1. Since it does this, it will never reach
# the actual final number you put in the range. This can be tricky for first timers.

########################################################################
# Write your own for loop that counts all the way to 13
########################################################################

# HERE

########################################################################
# We can, however, edit where a for loop starts in a very simple way:
for i in range(3, 5):
    print("This is loop number: ", i)
print("END LOOP")

# We can also edit variables inside a for loop, and they will stay edited through each iteration. For example:
number = 2
for i in range(5):
    number = number * 2 # This says that, each time we loop, number will be changed to whatever its current value is times 2
    print(number)
print("END LOOP")

# Or, we can multiply a variable by whatever number loop we are on:
number = 2
for i in range(5):
    number = number * i
    print(number)
print("END LOOP")

# Wait, why is it all zeros? Well, the loop starts counting from zero! So, we get a zero on our first multiply, then each time we loop we are multiplying by zero again.

########################################################################
# Write your own for loop that multiplies a variable by the number of the current loop, but make sure the loop doesn't start at 0
########################################################################

# HERE

# Fantastic! For loops are now pretty well understood! They can obviously get much more complex than we have seen here, but now you know the basics and can
# mess around with them for yourself!