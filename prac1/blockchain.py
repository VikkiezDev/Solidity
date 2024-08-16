from client import Client
from transaction_class import Transaction  # Assuming Transaction class is imported from transaction_class module

class Block:
    def __init__(self, client):
        self.verified_transactions = []  # List to store verified transactions in the block
        self.previous_block_hash = ""  # Hash of the previous block in the blockchain
        self.Nonce = ""  # Nonce (number used once) for proof of work (not implemented here)
        self.client = client  # Client associated with this block

def dump_blockchain(blocks):
    print(f"\nNumber of blocks in the chain: {len(blocks)}")
    for i, block in enumerate(blocks):
        print(f"Block # {i}")
        for transaction in block.verified_transactions:
            Transaction.display_transaction(transaction)
        print("--------------")
    print("=====================================")

if __name__ == '__main__':
    # Create a client instance
    Dinesh = Client()
    
    # Create a genesis transaction
    t0 = Transaction("Genesis", Dinesh.identity, 500.0)  # Corrected line
    
    # Create a genesis block
    block0 = Block(Dinesh)
    block0.previous_block_hash = ""
    block0.Nonce = None  # Placeholder for proof of work nonce (not implemented)
    block0.verified_transactions.append(t0)
    
    # Hash the genesis block (not implemented in this snippet)
    digest = hash(block0)
    last_block_hash = digest
    
    # List to store blockchain blocks (currently only the genesis block)
    TPCoins = [block0]
    
    # Dump blockchain to display all blocks and their transactions
    dump_blockchain(TPCoins)
