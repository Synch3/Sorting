# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        if i < smallest_index:
            smallest_index = i



        # TO-DO: swap
            arr.insert(i, arr.pop(smallest_index))  
            


    print(arr)
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

arr2 = []

arr3 = [0, 1, 2, 3, 4, 5]

        
selection_sort(arr1) #, [0,1,2,3,4,5,6,7,8,9])
selection_sort(arr2) # , [])
selection_sort(arr3) # , [0,1,2,3,4,5])

    #    selection_sort(arr4) // , sorted(arr4))