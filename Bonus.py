# Bonus
# Write a function that when given two numbers, finds their greatest common divisor.
def gcd(x,y):
  if y == 0:
    return x
  else:
    return gcd(y, x % y)

print("gcd of 15 and 10:",gcd(15,10))
print("gcd of 46 and 12:",gcd(46,12))


# The greatest common divisor of two integers is the largest positive integer that divides both of the integers. For example, look at the numbers 10 and 15: 10 can be divided by 1, 5, and 10, 15 can be divided by 1, 3, 5, and 15.
# When we say 'can be divided' here we mean divided evenly, so in other words there is no remainder. For example when 15 is divided by 6, there is a remainder of 3 because 15=6(2)+3 so 6 is not a divisor of 15.
# The greatest common divisor of 15 and 10 is 5 since both numbers can be divided by 5.
# Here is more information on greatest common divisors. https://en.wikipedia.org/wiki/Greatest_common_divisor


# Extra Bonus
# Try solving the algorithms using an iterative approach and compare your code.

# You can read more about recursion here. https://en.wikipedia.org/wiki/Recursion_(computer_science)