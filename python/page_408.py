# Get pi/4 for x digits

from math import pi

a = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 - 1/15 # ... over time this approximate pi/4?
print(a)

for char in str(pi/4)[2:]:
    print(char)
