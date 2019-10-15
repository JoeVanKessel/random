def find(unsorted, near, amount):
    nearest = [amount]
    i = 0
    while i < len(unsorted):
        if i == 0:
            nearest[i] = unsorted[i]

    return nearest
