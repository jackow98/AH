import random


# Bubble Sort Following the Pseudocode on Scholar
def bubble_sort(list):
    total_swaps = 0
    list_to_sort_length = len(list)
    swapped = True

    print("BUBBLE START: Sorting the list", list)

    # The outer while loop will repeat if there has been a swap and there is more than one item in our list to sort
    # Each iteration of the while loop will bubble up the largest number which is closest to the start of the list?
    # - If there have been no swaps, then the list is sorted, and we won't repeat
    # - If there has been a swap, then the list is not sorted, and we must repeat the process for the rest of the list
    # - If there is no items left to sort then we won't repeat
    while swapped and list_to_sort_length >= 0:
        print("\tWHILE START: Swapped is " + str(swapped) + " and list_to_sort_length is " + str(
            list_to_sort_length) + " so repeating while loop")
        swapped = False

        # This will bubble up the largest number which is closest to the start of the list?
        for i in range(0, list_to_sort_length - 1):
            print("\t\tFOR Iteration " + str(i))
            print("\t\t\tComparing index " + str(i) + " with " + str(i + 1))

            # If value in position i bigger than the one in position i+1, swap them
            if list[i] > list[i + 1]:
                print("\t\t\t" + str(list[i]) + " is greater than " + str(list[i + 1]) + " so swapping")
                print("\t\t\t" + str(list))

                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
                total_swaps = total_swaps + 1

                unswapped_lower = str(list[0:i] if len(list[0:i]) > 0 else "") + " "
                swapped = "\033[1m" + str(list[i + 1]) + " <-> " + str(list[i]) + ", " + "\033[0m"
                unswapped_higher = str(list[i + 2:] if len(list[i + 2:]) > 0 else "") + " "

                print("\t\t\t" + unswapped_lower + swapped + unswapped_higher)
                print("\t\t\t" + str(list))
                swapped = True
            else:
                print("\t\t\tNo Swap")

        # The value at the top of the list is now the biggest so we reduce the size of our list to sort by 1
        list_to_sort_length = list_to_sort_length - 1
        print("\tWHILE END: Swapped is " + str(swapped) + ", list_to_sort_length is " + str(
            list_to_sort_length) + ", and list is", list)

    print("BUBBLE END: Sorted list is ", list)
    print("Total swaps is ", total_swaps)


if __name__ == '__main__':
    # bubble_sort([5, 1, 4, 8, 2, 9])
    # bubble_sort([5, 1, 4, 8, 2, 12, 9])
    # bubble_sort([8, 8, 8, 4, 8, 3])
    bubble_sort([2, 10, 5, 9, 9, 2, 10, 2, 6, 3, 4, 10, 5, 5, 5, 9, 5, 2, 2, 1, 4, 8, 1, 7, 9, 5, 6, 3, 3, 10, 3, 5, 5, 6, 6, 3, 9, 8, 9, 10, 5, 5, 2, 5, 6, 3, 3, 8, 9, 2])
    # bubble_sort([random.randint(1, 10) for x in range(0, 50)])
