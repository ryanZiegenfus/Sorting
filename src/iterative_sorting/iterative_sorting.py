# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        smallest_value = arr[i]
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < smallest_value:
                smallest_value = arr[j]
                smallest_index = j
        
        if smallest_value != arr[i]:
            arr[i], arr[smallest_index] = smallest_value, arr[i]
        # TO-DO: swap

    print(arr)
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for _ in range(0, len(arr) - 1):
        j = len(arr) - 1
        for k in range(0, j):
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
        j = j - 1
    print(arr)
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

selection_sort([5,2,8,9,6,4,3,6,7,234,567,8])
bubble_sort([3, 5, 1,8,3,7,8,9,6,4,5,3,5,6,898,5])