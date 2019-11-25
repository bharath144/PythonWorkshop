import random
import time

input_a = [x for x in range(0, 1000)]
input_b = random.sample(input_a, 10)
input_c = input_b.copy()

def iterative_sort(unsorted_list):
    print(unsorted_list)
    for i in range(0, len(unsorted_list)):
        # Improved exit condition, if there are no swaps, all numbers are sorted
        swapped = False
        for j in range(0, len(unsorted_list) - i - 1):
            if unsorted_list[j] > unsorted_list[j+1]:
                # The actual in-place swap, a semantic that's unique to Python.
                # This is similar to temp = x, x = y, y = temp
                unsorted_list[j], unsorted_list[j+1] = \
                    unsorted_list[j+1], unsorted_list[j]
                print("   " + str(unsorted_list))

                # Indicates if we swapped something
                swapped = True
        print(unsorted_list)
        if not swapped:
            break

def recurseive_sort(unsorted_list):
    print(unsorted_list)
    for i, num in enumerate(unsorted_list):
        try:
            if unsorted_list[i + 1] < num:
                # Swap
                unsorted_list[i] = unsorted_list[i + 1]
                unsorted_list[i + 1] = num
                print("   " + str(unsorted_list))
                recurseive_sort(unsorted_list)
        except IndexError:
            print(unsorted_list)
            pass

    return unsorted_list

recurseive_sort(input_b)
print("")
print("")
print("")
print("")
iterative_sort(input_c)
