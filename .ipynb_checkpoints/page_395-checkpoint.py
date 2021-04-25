import itertools


def is_prime(n):
    if n == 1:
        return False
    # if divisible only by itself and one return True
    countdown = n

    for divisor in range(1, n):
        blacklist = [1, n]
        if countdown not in blacklist:
            remainder = n % countdown
            if remainder == 0:
                return False

        countdown -= 1
    return True


def is_in_prime_pair(n):
    assert is_prime(n)
    higher = n + 2
    lower = n - 2
    if is_prime(higher) or is_prime(lower):
        return True
    else:
        return False


def get_primes(limit):
    primes = []
    while limit > 0:
        if is_prime(limit):
            primes.append(limit)
        limit -= 1
    primes.reverse()
    return primes


def is_goldbach(n):
    # Is even number a difference of two primes?
    # i.e. does it have goldbach property
    # results = []
    list1 = get_primes(n * 2)
    list2 = list1.copy()
    if n % 2 == 0:
        for i in list1:
            for j in list2:
                if i > j:
                    if i - j == n:
                        return True
    return False


def get_goldbachs(limit):
    output = []
    for i in range(1, limit + 1):
        if is_goldbach(i):
            output.append(i)
    return output


def is_tortoise(n):
    # Is even number a sum of 2 primes?
    if n % 2 == 0:
        list1 = get_primes(n)
        list2 = list1.copy()
        for i in list1:
            for j in list2:
                if i + j == n:
                    return True
    return False


def is_achilles(n):
    if not is_tortoise(n):
        return True
    return False
