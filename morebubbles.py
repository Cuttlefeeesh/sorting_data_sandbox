from cocktailsort import bubblecompare

def bublystep(i,len, dir):
    stepsize = 2
    topindex = len-2

    nextstep = i + dir * stepsize
    if nextstep > topindex: # above max
        if len%stepsize==0:
            nextstep = topindex -1
        else:
            nextstep = topindex
        dir = -1
    elif nextstep <= 0: # below min
        nextstep = 0
        dir = 1
    print(nextstep)
    return nextstep, dir

def bubblysort(unsorted: list):
    unsorted = list(unsorted)
    history = []
    history.append(list(unsorted))
    sortedcheck = list(unsorted)
    sortedcheck.sort()
    listlength = len(sortedcheck)

    done = False
    i = 0
    t = 0
    stepsize = 3
    direction = 1
    top_offset = 1+stepsize
    bottom_offset = stepsize-1

    while not done:
        t, unsorted = bubblecompare(t, unsorted, i)
        i, direction = bublystep(i, listlength, direction)
        """
        if i > len(unsorted)-top_offset: # reverse direction at top of list
            direction = -1
            top_offset = top_offset + 1
            i = i + direction * stepsize + 1
        elif i < bottom_offset: # reverse direction at top of list
            direction = 1
            bottom_offset = bottom_offset + 1
            i = i + direction * stepsize
        """
        history.append(list(unsorted))
        if unsorted[:] == sortedcheck:
            done = True

    return history