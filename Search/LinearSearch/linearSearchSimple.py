def linear_search(list, item_to_find):
    found = False
    array_size = len(list)-1
    counter = 0

    while counter <= array_size and not found:
        found = list[counter] == item_to_find
        counter = counter + 1

    if found:
        print(str(item_to_find) + " found at position " + str(counter - 1))
    else:
        print("Item not found")


if __name__ == '__main__':
    # linear_search([2, 5, 8, 12, 16, 27, 38, 58, 81, 91], 27)
    # linear_search([2, 5, 8, 12, 16, 27, 38, 58, 81, 91], 91)
    linear_search([2, 5, 8, 12, 16, 27, 38, 58, 81, 91], 2)
