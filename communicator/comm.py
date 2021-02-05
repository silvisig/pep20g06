from communicator.utils import generate_primes
from random import randint


class Client():
    def __init__(self, base, key):
        self.base = base
        self.key = key

    def _prime(self):
        prime_nr = generate_primes(256)
        my_list = []
        self.prime_nr = [i for i in prime_nr if i >= 129]
        length_prime = len(self.prime_nr)
        random_nr = randint(0, length_prime - 1)
        print(random_nr)
        self.prime = self.prime_nr[random_nr]
        print(self.prime_nr)
        return self.prime

    def select_local_secret(self):
        self.secret = randint(129, self.prime)
    def get_secret(self, secret):
        self.secret1 = ( pow(self.secret,secret) % self.prime)
    def Crypted(self, text_encrypt):
       return crypt_decrypt(text_encyrpt, self.secret)

class Server():
    def __init__(self, base, key):
        self.base = base
        self.key = key

    def _prime(self):
        prime_nr = generate_primes(256)
        self.prime_nr = [i for i in prime_nr if i >= 129]

    def get_prime(self, prime):
        self.prime = prime

    def get_secret(self, secret):
        self.secret1 = (pow(self.secret, secret) % self.prime)

    def select_local_secret(self):
        self.secret = randint(129, self.prime)

    def Decrypted(self, text_to_decrypt):
        return crypt_decrypt(text_to_decrypt, self.secret)
