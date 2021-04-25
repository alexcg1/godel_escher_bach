# Test if number is prime

def is_prime(n):
    divisor = n-1
    while divisor > 1:
        output = n % divisor
        if output == 0:
            print(f"{n} is not prime")
            return False
        divisor -= 1
    print(f"{n} is     prime")
    return True


for i in range(0,35):
    is_prime(i)
