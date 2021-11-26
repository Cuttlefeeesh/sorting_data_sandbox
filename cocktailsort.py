
def bubblecompare(t, unsorted:list, i:int):
    # gravity is 1 when increasing and -1 when decreasing

    a = unsorted[i]
    b = unsorted[i+1]
    if a > b:
        unsorted[i] = b
        unsorted[i + 1] = a
        t = 0
    t = t+1
    return t, unsorted

def cocktailsort(unsorted: list):
    step = 0
    history = []
    history.append(unsorted[:])

    done = False
    i=0
    t = 0
    direction = 1
    top_offset = 2
    bottom_offset = 0
    while not done:
        t, unsorted = bubblecompare(t, unsorted, i)
        if t > len(unsorted):
            done = True
        i = i + direction
        if i > len(unsorted)-top_offset: # reverse direction at top of list
            direction = -1
            top_offset = top_offset + 1
            i = i-1
        elif i < bottom_offset: # reverse direction at top of list
            direction = 1
            bottom_offset = bottom_offset + 1
            i = i + 1

        step = step+1
        history.append(unsorted[:])
        #print(history)

    return history