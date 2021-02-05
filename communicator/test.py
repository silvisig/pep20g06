from communicator.comm import Client,Server

client = Client('1','2')
prime_nr= client._prime()
client.select_local_secret() #pe ob client apelam metoda select_local-secret
print(client.prime_nr)
print('client',client.secret)
print(client.secret1)

server=Server('verde','albastru')
server.get_prime(prime_nr)
print(server.prime)
print(server.secret1)
server.select_local_secret()
print('server',server.secret)


print(server.prime)
initial_string = 'Text to send to server'
enc = crypt_decrypt(initial_string, client.secret)
print(enc)
dec = crypt_decrypt(enc, server.secret)
print(dec)
encrypted_text=client.encrypt(initial_string)
print(encrypted_text)
decrypted_text=server.decrypt(dencrypted_text)
