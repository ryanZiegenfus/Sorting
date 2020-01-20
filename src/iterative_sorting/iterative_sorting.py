# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        smallest_value = arr[i]
        print(f'This index at i is: {i}')
        print(f'This value at i is: {arr[i]}')
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            print(f'The index at j is: {j}')
            print(f'The value at j is: {arr[j]}')
            if arr[j] < smallest_value:
                print(f'{arr[j]} is less than {smallest_value}')
                smallest_value = arr[j]
                smallest_index = j
                print(f'The new smallest value is: {smallest_value}')

            print('************')
        
        if smallest_value != arr[i]:
            print(f'{arr[i]} becomes {smallest_value}')
            print(f'{arr[smallest_index]} becomes {arr[i]}')

            arr[i], arr[smallest_index] = smallest_value, arr[i]
        print(f'This is the updated array: {arr}')   
        # TO-DO: swap



    print(arr)
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


selection_sort([3,5,1,2,3])