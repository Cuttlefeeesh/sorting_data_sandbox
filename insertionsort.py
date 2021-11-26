from collections import deque
def insertionsort(unsorted:deque):
    history = [list(unsorted)]
    ordered = deque([unsorted.popleft()])
    while unsorted:
        x = unsorted.popleft()
        center = deque([])
        placed = False
        while not placed:
            y = ordered.pop()
            if x < y:
                center.appendleft(y)
                histline = list(ordered) + [x] + list(center) + list(unsorted)
                history.append(histline)
            elif x > y:
                ordered.append(y)
                ordered.append(x)
                ordered.extend(center)
                center.clear()
                histline = list(ordered) + list(unsorted)
                history.append(histline)
                placed = True
            if not ordered: # we've run out of ordered numbers, x is lowest
                ordered.append(x)
                ordered.extend(center)
                center.clear()
                placed = True



    return history
