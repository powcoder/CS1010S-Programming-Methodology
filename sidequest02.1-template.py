https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
#
# CS1010S --- Programming Methodology
#
# Mission 2 - Side Quest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import sin, cos, pi

# helper function used by both task 1 and task 2 #
def my_help(n, i, f):

    scaled = f(i)

    if i == 1:

        return scaled
    else:

        return overlay_frac((i-1)/i, my_help(n, i-1, f), scaled)


##########
# Task 1 #
##########


def tree(n, rune):
    # Fill in code here

    def f(i):
        return scale(i/n, rune)

    x =  my_help(n, n, f)

    # print(x)

    return x


# Test
#show(tree(4, circle_bb))

##########
# Task 2 #
##########

# use help(math) to see functions in math module
# e.g to find out value of sin(pi/2), call math.sin(math.pi/2)
#
def helix(rune, n):

    r = 1/2 - 1/n

    t = 2/n

    u = t * pi

    def f(i):

        return translate(r * sin((i-1) * u), r * cos((i-1) * u), scale(t, rune))

    x =  my_help(n, n, f)

    return x

# Test
# show(helix(make_cross(rcross_bb), 9))


# your solution here
def helix(rune, n):

    r = 1/2 - 1/n

    t = 2/n

    u = t * pi

    def f(i):

        return translate(r * sin((i-1) * u), r * cos((i-1) * u), scale(t, rune))

    x = f(1)

    for i in range(2, n+1):

        # x =  overlay((i-1)/i, x), f(i))
        # x =  overlay_frac((i-1)/i, x, f(i))

        x =  overlay( x, f(i))




    return x

show(helix(make_cross(rcross_bb), 9))


# print(tree(4, circle_bb))
print(show(helix(make_cross(rcross_bb), 9)))