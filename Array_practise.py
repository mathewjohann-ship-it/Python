import numpy as np
from colorama import Fore, Style


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Finds what index the thing your finding is at.
find = np.where(a == 1)
print(Fore.GREEN + f"{find}\n")


# Reshapes the array
print(f"{a.reshape(3, 1)} \n")
# Finds out what shape it is
print(f"{a.shape} \n")


# Iterates each element in the array
for i in a:
    print(i)

# Joins the two array together
print(f"{np.concatenate((a, b))}\n")

# adds the two arrays
print(f"{np.add(a, b)}\n")

# Substracts the two arrays
print(f"{np.subtract(a, b)}\n")

# Multiplies the two arrays
print(f"{np.multiply(a, b)}\n")

# divedes the two arrays
print(f"{np.divide(a, b)}\n")
