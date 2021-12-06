import copy

def sonar_sweeper(depths):
    count = 0
    for i in range(len(depths) - 1):
        if depths[i] < depths[i+1]:
            count += 1
    return count

def sonar_sweeper_advanced(depths):
    count = 0
    B = depths[0] + depths[1] + depths[2]
    for i in range(1, len(depths) - 2):
        A = copy.copy(B)
        B = depths[i] + depths[i+1] + depths[i+2]
        if A < B:
            count += 1
    return count





