import math
import sys

def smallestDifference(arr1,arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)


    i1 = i2 = 0
    smallest = math.inf
    while i1 < len(arr1) and  i1 < len(arr2):
        if arr1[i1] <= arr2[i2]:
            if arr2[i2] - arr1[i1] < smallest:
                smallest = arr2[i2] - arr1[i1]
            i1+=1
        else:
            if arr1[i1] - arr2[i2] < smallest:
                smallest = arr1[i1] - arr2[i2]
            i2+=1
    return smallest


    if __name__ == "__main__":
        arr1 = [int(a) for a in sys.argv[1].split(',')]
        arr2 = [int(a) for a in sys.argv[2].split(',')]
        print(smallestDifference(arr1,arr2))

