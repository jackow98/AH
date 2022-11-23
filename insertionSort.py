# Insertion Sort Following the Pseudocode on Scholar
def insertion_sort(my_list: list):
    total_swaps = 0
    value = 0
    index = 0

    print("INSERTION START: Sorting the list", my_list)
    for i in range(1, len(my_list)):
        print("\n\tFOR START: Iteration "+str(i)+" value is " + str(value) + " and index is " + str(index) + " and list is " + str(my_list))
        value = my_list[i]
        index = i

        while index > 0 and value < my_list[index - 1]:
            print("\t\tWHILE START: Index is " + str(index) + " and value is " + str(
                value) + " which is less than " + str(my_list[index - 1]) + " so swapping")
            print("\t\t\t" + str(my_list))

            my_list[index] = my_list[index - 1]
            index = index - 1

            unswapped_lower = str(my_list[0:index + 1]) if len(my_list[0:index + 1]) > 0 and index >= 0 else "" + ""
            unswapped_higher = str(my_list[index + 2:] if len(my_list[index + 2:]) > 0 else "") + " "
            swapped = "\033[1m" + str(my_list[index]) + " <-> " + str(value) + ", " + "\033[0m"

            print("\t\t\t" + unswapped_lower + "\033[1m i \033[0m" + unswapped_higher)
            print("\t\t\t" + swapped)

        my_list[index] = value
        total_swaps = total_swaps + 1
        print("\tFOR END: sorted list is " + str(my_list))

    print("INSERTION END: Sorted list is ", my_list)
    print("Total swaps is ", total_swaps)


if __name__ == '__main__':
    insertion_sort([5, 1, 4, 8, 2, 9])
    # insertion_sort([5, 1, 4, 8, 2, 12, 9])
    # insertion_sort([8, 8, 8, 4, 8, 3])
    # insertion_sort([2, 10, 5, 9, 9, 2, 10, 2, 6, 3, 4, 10, 5, 5, 5, 9, 5, 2, 2, 1, 4, 8, 1, 7, 9, 5, 6, 3, 3, 10, 3, 5, 5, 6, 6, 3, 9, 8, 9, 10, 5, 5, 2, 5, 6, 3, 3, 8, 9, 2])
    # insertion_sort([random.randint(1, 10) for x in range(0, 6)])
