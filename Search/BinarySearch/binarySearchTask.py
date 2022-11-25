def binary_search(list, target):
    low = 0
    high = len(list)
    mid = 0
    found = False
    elements_searched = 0

    """
    Implement while loop here
    """

    if not found:
        print("Target not found")

    print("Searched " + str(elements_searched) + " elements")
    return {"found": found, "elements_searched": elements_searched, "position": mid}


if __name__ == '__main__':
    binary_search([2, 5, 8, 12, 16, 27, 38, 58, 81, 91], 27)
