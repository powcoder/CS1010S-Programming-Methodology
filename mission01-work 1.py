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
# Mission 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


##########
# Task 1 #
##########

def mosaic(a,b,c,d):
    # Fill in code here
    return stack(beside (d,a), beside (c,b))


# Test
#show(mosaic(rcross_bb, sail_bb, corner_bb, nova_bb))
#show(mosaic(heart_bb, pentagram_bb, circle_bb, ribbon_bb))


##########
# Task 2 #
##########

def simple_fractal(pic):
    # Fill in code here
    return beside(pic, stack(pic,pic))

# Test
#show(simple_fractal(make_cross(rcross_bb)))
#show(simple_fractal(heart_bb))
