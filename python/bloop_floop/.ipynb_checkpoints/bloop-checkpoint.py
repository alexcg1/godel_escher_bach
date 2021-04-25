# Page 410
def wrong_two_three_n(n):
    output = 2
    counter = 1
    while counter < 3: # Power of 3
        counter += 1
        output = 2*output

    print(f"2 to power 3 is {output}")

    counter = 1
    while counter < n: # Power of n
        counter += 1
        output = output*n

    print(output)

def two_three_n(n):
    # First work out 3 to n
    power = n
    total = 3
    counter = 1
    while counter < n:
        counter += 1
        total = total*power

    print(f"- 3 to power of {n} is {total}")

    print(f"Now computing 2 to power of {total}")
    n = total
    power = n
    counter = 1
    base = 2
    output = base
    while counter < n:
        counter + 1
        output = output*power

    print(f"- 2 to power of 3 to power of {n} is {output}")

two_three_n(1)

