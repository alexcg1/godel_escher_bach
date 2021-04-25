
def power_of(number, power, original=None):
    """
    Number - base
    Power - power to raise to
    Original - original number we started with so we don't multiply exponentially
    """
    if not original:
        original = number
    n = number
    p = power
    o = original

    if p == 1:
        return n
    else:
        # print(f"Calculating {n} x {original}")
        n = n*original
        return power_of(n, p-1, original)

def power_of_loop(number, power, original=None):
    if not original:
        original = number
    n = number
    p = power
    o = original

    counter = power
    while counter > 1:
        # print(f"Calculating {n} * {o}")
        n = n*original
        counter = counter -1
    return n


n = 5

def bloop_loop(n):
    output1 = power_of_loop(3, n)
    output2 = power_of_loop(2, output1)
    return output2

def bloop_recursive(n):
    """
    2 to the (3 to the n)
    """

    return power_of(2, power_of(3, n))

print(f"LOOP     : 2 to the power of (3 to the power of {n}) is {bloop_loop(n)}")
print(f"RECURSIVE: 2 to the power of (3 to the power of {n}) is {bloop_recursive(n)}")
