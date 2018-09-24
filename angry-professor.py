@Angry profesor 

# A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, he decides to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time () to arrived late ().
# Given the arrival time of each student and a threshhold number of attendees, determine if the class is canceled.

#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    
    
    a = map(int,raw_input().strip().split(' '))
    
    
    
    s = 0
    
    
    
    for i in a:
        if i <= 0:
            s += 1
    if s >= k:
        print "NO"
    else:
        print "YES"
