def is_prime(number):
    for i in range(2, number // 2 + 2):
        if not number % i:
            return False
    return True
def generate_primes(limit):
    result = []
    for i in range(limit):
        if is_prime(i):
            result.append(i)
    return result
