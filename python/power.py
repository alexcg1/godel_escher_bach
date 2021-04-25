def power_of(n, p):
    return n**p

def power_of_manual(number, power, original=None):
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
        print(f"Calculating {n} x {original}")
        n = n*original
        return power_of_manual(n, p-1, original)

# output = power_of(3, 2)

input1 = 3
input2 = 10

manual = power_of_manual(input1, input2)
print(manual)

auto = power_of(input1, input2)
print(f"Should return {auto}")
