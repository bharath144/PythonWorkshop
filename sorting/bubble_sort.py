import random
import time

input_a = [x for x in range(0, 15)]
input_b = random.sample(input_a, 10)
print(input_b)

for i in range(0, len(input_b)):
    # Improved exit condition, if there are no swaps, all numbers are sorted
    swapped = False
    for j in range(0, len(input_b) - i - 1):
        if input_b[j] > input_b[j+1]:
            # The actual in-place swap, a semantic that's unique to Python.
            # This is similar to temp = x, x = y, y = temp
            input_b[j], input_b[j+1] = input_b[j+1], input_b[j]
            print("   " + str(input_b))

            # Indicates if we swapped something
            swapped = True
            time.sleep(1)
    print(input_b)
    if not swapped:
        break
