def insertion_sort(my_list: list):
    value = 0
    index = 0
    for i in range(1, len(my_list)):
        value = my_list[i]
        index = i
        while index > 0 and value < my_list[index - 1]:
            my_list[index] = my_list[index - 1]
            index = index - 1
        my_list[index] = value
    print(my_list)


if __name__ == '__main__':
    insertion_sort([5, 1, 4, 8, 2, 9])
    insertion_sort(["B224", "F127", "F411", "B432", "H121"])
    # insertion_sort([5, 1, 4, 8, 2, 12, 9])
    # insertion_sort([8, 8, 8, 4, 8, 3])
    # insertion_sort([2, 10, 5, 9, 9, 2, 10, 2, 6, 3, 4, 10, 5, 5, 5, 9, 5, 2, 2, 1, 4, 8, 1, 7, 9, 5, 6, 3, 3, 10, 3, 5, 5, 6, 6, 3, 9, 8, 9, 10, 5, 5, 2, 5, 6, 3, 3, 8, 9, 2])
    # insertion_sort([random.randint(1, 10) for x in range(0, 6)])
