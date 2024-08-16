from client import Client
from transaction_class import Transaction  # Assuming Transaction class is imported from transaction_class module

# Create clients
Dinesh = Client()
Ramesh = Client()
Seema = Client()
Vijay = Client()

# Create transactions between clients
t1 = Transaction(Dinesh, Ramesh.identity, 15.0)
t1.sign_transaction()

t2 = Transaction(Dinesh, Seema.identity, 6.0)
t2.sign_transaction()

t3 = Transaction(Ramesh, Vijay.identity, 2.0)
t3.sign_transaction()

t4 = Transaction(Seema, Ramesh.identity, 4.0)
t4.sign_transaction()

# Store transactions in a list
transactions = [t1, t2, t3, t4]

# Display all transactions
for transaction in transactions:
    Transaction.display_transaction(transaction)
    print("--------------")
