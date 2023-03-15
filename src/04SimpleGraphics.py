import turtle
"""
Demonstrates using OBJECTS via Turtle Graphics.

Concepts include:
  -- CONSTRUCT an INSTANCE of a CLASS (we call such instances OBJECTS).
  -- Make an object   ** DO **   something by using a METHOD.
  -- Reference an object's   ** DATA **   by using an INSTANCE VARIABLE.

Also:
  -- ASSIGNING a VALUE to a NAME (VARIABLE).

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and PUT_YOUR_NAME_HERE.
"""
###############################################################################
#
# TODO: 1.
#   Yes, that means for YOU to DO things per the following instructions:
#
#   On Line 13 above, replace  PUT_YOUR_NAME_HERE  with your OWN name.
#
#   BTW, the top block of text above forms what is called a DOC-STRING.
#   It documents what this module does, in a way that exterior programs
#   can make sense of.  It has no other effect on this program.
#
###############################################################################

###############################################################################
#
# TODO: 3.
#   Run this module.  A window will pop up and Turtles will move around.
#
#   Then look at the code below. Be sure that you understand the notations for:
#
#     -- ASSIGNING the resulting OBJECT (instance of a class) a NAME, e.g.
#           natasha = turtle
#
#     -- Applying a METHOD to an object to make the object DO something, e.g.
#           natasha.forward(100)
#
#     -- Accessing an INSTANCE VARIABLE of an object, e.g.
#           natasha.speed = 10
#           boris.speed = natasha.speed
#
#   After you are confident that you understand all the code below,
#   change this _TODO_ to DONE and  ** continue to the next _TODO_ (below). **
#
###############################################################################

# -----------------------------------------------------------------------------
# The next few lines show how to:
#   - CONSTRUCT (make and initialize) a window object for animation.
# -----------------------------------------------------------------------------
window = turtle.getscreen()
# -----------------------------------------------------------------------------
# The next few lines show how to:
#   - CONSTRUCT (make) a Turtle object and ASSIGN a NAME to the object.
# -----------------------------------------------------------------------------
ashton = turtle
ashton.shape("turtle")
# -----------------------------------------------------------------------------
# The next few lines show how to:
#   - Ask the Turtle object to do things by applying METHODs to it.
# The numbers in the parentheses are called ARGUMENTS.
# -----------------------------------------------------------------------------
ashton.forward(100)
ashton.left(90)
ashton.forward(200)
# -----------------------------------------------------------------------------
# The next few lines show how to:
#   - Change the pen color
#   - Change the speed
# -----------------------------------------------------------------------------
ashton.pencolor(1, 0, 0) # First 3 are RGB code
ashton.speed = 5  # Bigger means faster, max is usually about 10

ashton.right(90)
ashton.forward(125)

###############################################################################
#
# TODO: 4.
#   Add a few more lines of your own code to make one of the existing
#   Turtles move some more and/or have different characteristics.
#
#      ** Nothing fancy is required. **
#      ** A SUBSEQUENT exercise will let you show your creativity. **
#
#   As always, test by running the module.
#
###############################################################################

# HERE

# -----------------------------------------------------------------------------
# The next line keeps the window open until the user closes it.
# Throughout this exercise, this line should be the LAST line in the file.
# DO NOT ADD CODE BELOW THIS LINE!
# -----------------------------------------------------------------------------
ashton.done()
