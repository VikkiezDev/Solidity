import binascii
import collections
import datetime
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
from client import Client  # Assuming Client class is imported from client module

class Transaction:
    def __init__(self, sender, recipient, value):
        self.sender = sender  # Sender (an instance of Client class)
        self.recipient = recipient  # Recipient's public key (identity)
        self.value = value  # Value of the transaction
        self.time = datetime.datetime.now()  # Timestamp of the transaction creation

    def to_dict(self):
        # Convert transaction details to an ordered dictionary
        sender_identity = "Genesis" if self.sender == "Genesis" else self.sender.identity
        return collections.OrderedDict({
            "sender": sender_identity,
            "recipient": self.recipient,
            "value": self.value,
            "time": self.time,
        })

    def sign_transaction(self):
        # Sign the transaction using the sender's private key
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        # Hash the transaction details
        h = SHA.new(str(self.to_dict()).encode("utf8"))
        # Return the signature in hexadecimal format
        return binascii.hexlify(signer.sign(h)).decode("ascii")
    
    @staticmethod
    def display_transaction(transaction):
        sender_identity = transaction.sender.identity if transaction.sender != "Genesis" else "Genesis"
        print(f"Sender: {sender_identity}")
        print(f"Recipient: {transaction.recipient}")
        print(f"Value: {transaction.value}")
        print(f"Time: {transaction.time}")


# Test the Transaction class
zainab = Client()
zeenat = Client()
t = Transaction(zainab, zeenat.identity, 5.0)

print("\nTransaction Recipient:\n", t.recipient)
print("\nTransaction Value:\n", t.value)

signature = t.sign_transaction()
print("\nSignature:\n", signature)

