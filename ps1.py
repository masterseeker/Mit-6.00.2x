###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # Create a sorted cows List by wieght in descending order
    cowsSorted = [(cow, cows[cow]) for cow in cows]
    cowsSorted.sort(key= lambda x: x[1], reverse = True)
    cowTrips = [] 
    # While cows are still present on earth 
    while len(cowsSorted) > 0:
        currTrip = []
        availWeight = limit
        lightestCow = cowsSorted[-1][1]
        for cow in cowsSorted:
            if cow[1] <= availWeight:
                currTrip.append(cow)
                availWeight -= cow[1]
            if availWeight < lightestCow or availWeight == 0:
                break
        # remove taking cows from the cowsSorted List
        for cow in currTrip:
            index = cowsSorted.index(cow)
            cowsSorted.pop(index)
        # add current Trip to cowTrips
        cowTrips.append([cow[0] for cow in currTrip])
    
    return cowTrips
    
    


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # worst possible solution
    leastTrips = [[cow] for cow in cows]
    for partition in get_partitions(cows):
         # if solutuion is not optimal continue to next partition
        if len(partition) >= len(leastTrips):
            continue
        obeysWeightLimit = True
        # if solutuion is not possible break early
        for trip in partition:
            currTripWeight = [cows.get(name) for name in trip]
            if sum(currTripWeight) > limit:
                obeysWeightLimit = False
                break
        # if obeys weight limit == True update current answer
        if obeysWeightLimit:
            leastTrips = partition
    return leastTrips

# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data.txt")
    # greedy run time 
    start = time.time()
    greedyCow = greedy_cow_transport(cows)
    end = time.time()
    print("Greedy Solution Time: {}".format(end-start))
    print(len(greedyCow))
    print()
    # Brute force run time
    start = time.time()
    bruteForceCow = brute_force_cow_transport(cows)
    end = time.time()
    print("BruteForce Solution Time: {}".format(end-start))
    print(len(bruteForceCow))

"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

#cows = load_cows("ps1_cow_data.txt")
#limit=10
#print(cows) 
#
#print(greedy_cow_transport(cows, limit))
#print()
#print(brute_force_cow_transport(cows, limit))

compare_cow_transport_algorithms()

