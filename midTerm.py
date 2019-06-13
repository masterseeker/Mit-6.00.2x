#! python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 21:04:58 2019
@author: Tech
Julian Daniel
"""

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    sCopy = s
    multipliers = []
    for elm in L:
        if elm <= s:
            multipliers.append(s//elm)
            s = s - (elm*multipliers[-1])
        else: 
            multipliers.append(0)
    count = 0
    for elm, multi in zip(L, multipliers):
        count += elm*multi
    
    if count == sCopy:
        return sum(multipliers)
    return "no solution"
    

            
            
            
def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """

    ans = None
    for i in range(len(L)):
        for j in range(i, len(L)):
            temp = sum(L[i:j+1])
            if ans == None or ans < temp:
                ans = temp
    return ans

#    maxLPre = max(L)
#    for i in range(1, len(L)):
#        L[i] = L[i] + L[i-1]
#    minL = min(L)
#    maxL = max(L)
#    # if largest continous sequence is smaller than the largest element return element
#    if maxL < maxLPre: 
#        return maxLPre
#    # if first element is smallest contiguos value in sequence 
#    if minL == L[0]:
#        if minL < 0:
#            return maxL - minL
#        else:
#            return maxL
#    #if max contigous value is the first value
#    if maxL == L[0]:
#            return maxL
#    return maxL - minL




def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    i = 0
    while True: 
        if test(i) == True:
            return i 
        elif test(-i) == True:
            return - i
        i+=1
#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

#### This test case prints 0 ####
def f(x):
    return x == 0

print(solveit(f))


#########

import pylab as plt

plt.figure(1)

xValues = [1]
yValues = [1]

for i in range(1, 10):
    yValues.append(i)
    xValues.append(xValues[-1]*2)
    

plt.title("Geometric Sequence G(n) = 1 * (4**(n-1))")
plt.xlabel("Input Values (n)")
plt.ylabel("OutPut Values G(n)")
plt.plot(yValues, xValues)

    






