
def get_primes_up_to_250():
    primes = []  # List to store prime numbers
    for num in range(2, 251):  # Numbers from 2 to 250
        is_prime = True  # Assume the number is prime
        for divisor in range(2, int(num ** 0.5) + 1):  # Check divisors up to √num
            if num % divisor == 0:  # If divisible, it's not a prime
                is_prime = False
                break
        if is_prime:  # If no divisors were found, it's prime
            primes.append(num)
    return primes



