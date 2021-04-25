import sys
import random

# number = int(sys.argv[1])
# counter = 0 # Number of steps

def odd_even(number: int, counter):
    counter += 1
    if number == 1:
        print(f"{counter} cycles")
        return counter
    elif number % 2 == 0:
        next_num = int(number/2)
        odd_even(next_num, counter)
    elif number % 2 == 1:
        next_num = (3*number)+1
        odd_even(next_num, counter)

    # print(counter)
    # return counter


attempts = 100

for j in range(attempts):
    counter = 0
    # print(j)
    rand = random.randint(1, 999999999999999999999999999999999999999)
    print(f"\nNumber: {rand}")
    tries = odd_even(rand, counter)
    # print(f"{rand} took {tries} steps")
