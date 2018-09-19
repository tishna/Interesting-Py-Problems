#!/bin/python

#The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.
#Laura plants a Utopian Tree sapling with a height of 1 meter at the onset of spring. How tall will her tree be after  growth cycles?

import sys


temp = int(raw_input().strip())



for item in xrange(temp):
    cyc = 1
    num = int(raw_input().strip())
    height = 1
        
    for i in range(num):
        if cyc == 1:
            height = height * 2
        else:
            height = height + 1
        cyc *= -1
    print height
