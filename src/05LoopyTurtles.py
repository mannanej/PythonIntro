import turtle

###############################################################################
# This code has multiple purposes, but the most important is to show how to do a for loop.
# These are REQUIRED for most programs in some way.
###############################################################################

###############################################################################
# One window
###############################################################################

window = turtle.getscreen()

###############################################################################
# Example 1.
###############################################################################
jakob = turtle
jakob.shape("turtle")
jakob.pencolor(0, 0, 1) # Blue
jakob.speed = 20  # Fast

distance = 200

# Do the indented code 6 times.  Each time draws a square.
for k in range(6):

    # Put the pen down, then draw a square of the given size:
    jakob.forward(distance)
    jakob.left(90) # Turn left 90 degrees
    jakob.forward(distance)
    jakob.left(90) # Turn left 90 degrees
    jakob.forward(distance)
    jakob.left(90) # Turn left 90 degrees
    jakob.forward(distance)
    jakob.left(90) # Turn left 90 degrees

    # Move a little below and to the right of where the previous
    # square started.  Do this with the pen up (so nothing is drawn).
    jakob.penup()
    jakob.right(45)
    jakob.forward(10)
    jakob.left(45)

    # Put the pen down again (so drawing resumes).
    # Make the size for the NEXT square be 10 pixels smaller.
    jakob.pendown()
    distance = distance - 25

turtle.done()
