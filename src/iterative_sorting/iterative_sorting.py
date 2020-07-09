# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    # -1 because we dont compare the last value in the list to anything
    for i in range(0, len(arr) - 1):
        #declare your starting point / smallest number
        cur_index = i #starting default
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        #For every element to the right of our default
        for j in range(i+1, len(arr)):
            #if the value were comparing is smaller than our current smallest number
            if arr[j] < arr[smallest_index]:
                # j becomes our new smallest number
                smallest_index = j


        # TO-DO: swap
        # Your code here

        #If we found an item smaller than our current smallest
        if smallest_index != i:
            #Smallest index now refers to j not i
            #So we swap the positions of j and i when j is smaller than i
            arr[smallest_index], arr[i] = arr[i], arr[smallest_index]


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    #length of array - 1 because there will never be anything to the right of the 
    # end of the array to compare to
    index_length = len(arr)-1 

    #Create a variable that will be used to get us out of our loop
    sorted = False

    #Create our loop
    while not sorted:
        #Loop will break when it has gone through all the values
        sorted = True

        #For every value in the list
        for i in range(0, index_length):
            #if value were comparing is greater than the value to the right
            if arr[i] > arr[i + 1]:
                #Sorting is not complete
                sorted = False
                #Switch the values being compared
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
