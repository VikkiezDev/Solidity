# pip install pycryptodome

import binascii
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
import Crypto.Random

class Client:
    def __init__(self):
        # Generate a new RSA key pair with 1024-bit key length
        random_generator = Crypto.Random.new().read
        self._private_key = RSA.generate(1024, random_generator)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)
    
    @property
    def identity(self):
        # Return the public key in hexadecimal format
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

# Example usage:
if __name__ == '__main__':
    # Create a new client instance
    dinesh = Client()
    
    # Print the public key of the client
    print("Public Key:", dinesh.identity)
