# Basic Insertion sort algorithm

arr = [2,6,5,1,3,4]

running = True

def insertion_sort(arr):
    #we need an outer loop to iterate through unsorted items
    for i in range(1,len(arr)):
        #runs for indexes 1-5
        j = i
        #starts at index of outer loop, checks if the numbers on the right are in order
        while arr[j-1] > arr[j] and j > 0:
            #swops j-1 and j
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

insertion_sort(arr)
print(arr)
