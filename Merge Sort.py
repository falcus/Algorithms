# Sorts an array by dividing it into arrays of single elements and then merging those into a single array (sorted)
# Uses recursion and pointers

def mergeSort(arr):
    if len(arr) > 1:

        #create sub-arrays 1 and 2 
        # sub-array1 from 1 -> midpoint and sub-array2 from midpt -> end
        midpt = len(arr)//2
        sub_array1 = arr[1:midpt]
        sub_array2 = arr[midpt:]

        #here we're doing the same process for each sub array
        mergeSort(sub_array1)
        mergeSort(sub_array2)

        #initial values for pointers that we'll use to keep track of where we are in an array
        i = j = k = 0

        #Until we reach the end 

        while i < len(sub_array1) and j < len(sub_array2):
            if subarray1


