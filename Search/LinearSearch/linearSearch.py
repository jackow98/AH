def linear_search(list, item_to_find):
    found = False
    array_size = len(list) - 1
    counter = 0

    while counter <= array_size and not found:
        print("WHILE START: Iteration " + str(counter))
        print("\tChecking at index " + str(counter))

        found = list[counter] == item_to_find
        lower_search = str(list[0:counter]) if len(list[0:counter]) > 0 else ""
        mid_item = "\033[1m" + str(list[counter]) + "\033[0m"
        upper_search = str(list[counter + 1:]) if len(list[counter + 1:]) > 0 else ""
        counter = counter + 1
        print("\t" + lower_search + " " + mid_item + " " + upper_search)

    print("WHILE END")

    if found:
        print("\033[1mFound at position " + str(counter - 1) + "\033[0m")
    else:
        print("Item not found")

    print("\nSearched " + str(counter + 1) + " elements")


if __name__ == '__main__':
    linear_search([2, 5, 8, 12, 16, 27, 38, 58, 81, 91], 27)
    linear_search(
        [1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 8, 8,
         8, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10], 8)
    # linear_search([2, 5, 8, 12, 16, 27, 38, 58, 81, 91], 91)
    # linear_search([2, 5, 8, 12, 16, 27, 38, 58, 81, 91], 2)
