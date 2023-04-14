def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def binarysearchFunc():
    arr = [10, 20, 23, 26, 29, 30, 45, 90, 102] # Numbers must be in order and can use the bubblesort to rearrange into proper numbers
    target = 10 # Input any value to search
    binsearch_Index = binary_search(arr, target)
    if binsearch_Index != -1:
        print(target, "is present in the array at index", binsearch_Index)
    else:
        print(target, "is not in the array.")

def bubblesortFunc():
    arr = [11, 6, 35, 44, 32, 61, 63, 55, 23]
    bubblesort_Arr = bubble_sort(arr)
    print("Sorted array is:", bubblesort_Arr)

def main():
    binarysearchFunc()
    print("\n")
    bubblesortFunc()

main()
