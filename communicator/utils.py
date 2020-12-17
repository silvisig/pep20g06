def function(string,key):
    list1 = []
    for i in string:
        list1.append (chr(ord(i).__xor__(key)))
    return ''.join(list1)
encrypted= function('hello world', 140)
print(encrypted)
decrypted =function(encrypted,140)
print(decrypted)
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