import random


def bubblesort(unsorted: list):
    step = 0
    history = []
    history.append(unsorted[:])

    done = False
    i=0
    t = 0
    while not done:
        a = unsorted[i]
        b = unsorted[i + 1]
        if a > b:
            unsorted[i] = b
            unsorted[i + 1] = a
            t = 0
        if t > 1.5 * len(unsorted):
            done = True
        i = i + 1
        if i > len(unsorted)-2:
            i=0
        t = t + 1
        step = step+1
        history.append(unsorted[:])
        #print(history)

    return history


def randomize_list(n):  # todo remove
    data = list(range(n))
    random.shuffle(data)
    return data


if __name__ == "__main__":
    unsorted = randomize_list(10)
    print(bubblesort(unsorted))
