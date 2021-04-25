# How calculate m - n, using only addition

def subtract(m, n):
    original_n = n
    assert(m >= n)
    counter = 0
    while m > n:
        n += 1
        counter +=1
    return counter

def if_subtract(m, n):
    original_n = n
    assert(m >= n)
    counter = 0
    for i in range(0, m):
        if n == m:
            return counter
            print("Done")
        else:
            n = n+1
            counter +=1

m = 7
n = 1

print(f"IF:   {m} - {n} = {subtract(m, n)}")
print(f"LOOP: {m} - {n} = {if_subtract(m, n)}")

