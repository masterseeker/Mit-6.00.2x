#! python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:43:26 2019
@author: Tech
Julian Daniel
"""
import random
import pylab as plt

plt.hist()

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float("NaN")
    
    total = 0
    mean = sum([len(t) for t in L])/len(L)
    
    for t in L:
        total += (len(t) - mean) ** 2
        
    deviation = (total / len(L)) ** 0.5
    return deviation

def stdDevOfInts(L):
    if len(L) == 0:
        return float("NaN")
    total = 0
    mean = sum(L) / len(L)
    
    for elm in L:
        total += (elm - mean) ** 2
    
    deviation = (total / len(L)) ** 0.5 
    return (deviation , mean)

def longestRun(numFlips):
    count = 0
    longestRun = 0
    for i in range(numFlips):
        if random.randint(1,2) == 1:
            count += 1
            if count > longestRun:
                longestRun = count
        else:
            count = 0
    return longestRun


import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    count = 0
    for trial in range(numTrials):
        if runMonoTrial():
            count += 1
    return count / numTrials
    
    count = sum([1 if runMonoTrial() else 0 for t in range(numTrials)])
    return count / numTrials 
    
#def runMonoTrial():
#    """
#    if all balls drawn are of the same color returns True else False
#    """
#    bucket = ["r", "b"] *3
#    random.shuffle(bucket)
#    selection = []
#    for i in range(3):
#        index = random.randint(0, len(bucket) -1)
#        selection.append(bucket.pop(index))
#    return len(set(selection)) == 1 
        
def runMonoTrial():
    """
    if all balls drawn are of the same color returns True else False
    """
    bucket = ["r", "b"] *3
    random.shuffle(bucket)
    selection = random.sample(bucket, 3)
    return len(set(selection)) == 1
        

            

            