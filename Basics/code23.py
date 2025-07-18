# Code #23: Find Prime numbers from a list
# Tier: Intermediate
# Goal: Extract prime numbers 

nums = [7, 10, 13, 15, 17, 21]
primes = []

for num in nums:
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)  # 👈 Now only runs if loop didn't break

print("Prime numbers:", primes)
