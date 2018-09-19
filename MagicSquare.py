We define a magic square to be an  matrix of distinct positive integers from  to  where the sum of any row, column, or diagonal of length  is always equal to the same number: the magic constant.

You will be given a  matrix  of integers in the inclusive range . We can convert any digit  to any other digit  in the range  at cost of . Given , convert it into a magic square at minimal cost. Print this cost on a new line.

from itertools import *

X_Square = []
X_Square.extend(list(map(int,input().split())))
X_Square.extend(list(map(int,input().split())))
X_Square.extend(list(map(int,input().split())))

Ans = 81
for P in permutations(range(1,10)):
    if sum(P[0:3]) == 15 and sum(P[3:6]) == 15 and sum(P[0::3]) == 15 and sum(P[1::3]) == 15 and P[0] + P[4] + P[8] == 15 and (P[2] + P[4] + P[6] == 15):
        Answer = min(Ans, sum(abs(P[i] - X_Square[i]) for i in range(0,9)))
print(Answer)
