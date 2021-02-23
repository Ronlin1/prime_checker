# Prime Number Checker

def prime_checker(n):
    """
    This function checks if a number is a prime number and returns a boolean expression for it.
    It can also be tweaked to return a list or a certain range of prime numbers.
    """

    # These If statements here are for excluding the first numbers not involved in the while loop
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n == 5 or n == 7:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # If you know prime Nos: U well know that apart from 5, no other multiple of 5 is a prime number
    # So lets initialize our i from 5 --> Prime Nos = 1*2, 1*3, 1*5, 1,7 --and so on --->
    i = 5
    while i * 1 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
        # print(i) #Debugger
        return True  # This returns True  for numbers that are prime


# Let's Generate a list
my_list = [i for i in range(100)]
# print(my_list) # For Debugging
x = []

# Using Enumerate function to append a boolean expression on the first 100 numbers
for k, j in enumerate(range(len(my_list))):
    if prime_checker(my_list[j]):
        print(k, "--> true")
        if k:
            x.append(k)
    else:
        print(k, "--> false")
print(x)

# If you don't understand a thing, kindly feel free to hit on me for clarification and teaching
