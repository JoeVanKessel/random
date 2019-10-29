
def max_wis(a):
    set = []
    i = len(a)-1
    while i >= 1:
        if a[i] == a[i - 1]:
            i = i - 1
        else:
            set.append(a[i])
            i = i - 2
    return set
