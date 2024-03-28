import math

# Calculate the factorial of 25
factorial_25 = math.factorial(25)

# Calculate the number of symmetries
symmetries = 25 * 2 * 4  # 25 digraph swaps * 2 (since reversing the order of the swap doesn't change the key) * 4 (rotations: 0, 90, 180, 270 degrees)

# Calculate the number of effectively unique keys
effectively_unique_keys = factorial_25 // symmetries

# Convert the number of effectively unique keys to the approximate power of 2
approx_power_of_2 = math.log2(effectively_unique_keys)

print("Approximate power of 2 for effectively unique keys:", approx_power_of_2)
