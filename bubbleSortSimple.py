import random


# Bubble Sort Following the Pseudocode on Scholar
def bubble_sort(list):
    n = len(list)
    swapped = True
    while swapped and n >= 0:
        swapped = False
        for i in range(0, n - 1):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp

                swapped = True
        n = n - 1
    print(list)


if __name__ == '__main__':
    bubble_sort([5, 1, 4, 8, 2, 9])
    # bubble_sort([5, 1, 4, 8, 2, 12, 9])
    # bubble_sort([8, 8, 8, 4, 8, 3])
    # bubble_sort([2, 10, 5, 9, 9, 2, 10, 2, 6, 3, 4, 10, 5, 5, 5, 9, 5, 2, 2, 1, 4, 8, 1, 7, 9, 5, 6, 3, 3, 10, 3, 5, 5, 6, 6, 3, 9, 8, 9, 10, 5, 5, 2, 5, 6, 3, 3, 8, 9, 2])
    # bubble_sort([random.randint(1, 10) for x in range(0, 50)])
