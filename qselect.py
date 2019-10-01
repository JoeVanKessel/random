import random
def qselect(k, a):
    if a == []:
        return []
    else:
        pivotindx = random.randint(0, len(a)-1)
        pivot = a[pivotindx]
        left = [x for x in a if x < pivot ]
        right  = [x for x in a if x > pivot ]
        print("pivot: ", pivot)
        print("pivot index", pivotindx)
        print("right: ", right)
        print("left: ", left)
        print("k: ", k)
        a = left + [pivot] + right
        print(a)
        if k == len(left)+1 or len(a) == 1:
            return pivot

        if len(a) == 2 and a[1] == pivot and k != 1:
            return pivot

        elif k < len(left)+1:
            print("left")
            return qselect(k, left)

        elif k >= len(left)+1:
            print("right")
            k = k - 1
            return qselect(k, right)
