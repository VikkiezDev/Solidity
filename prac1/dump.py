import datetime
import hashlib

# Create a class for blocks in the blockchain
class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now(datetime.timezone.utc)  # Current timestamp in UTC
        self.data = data  # Data stored in the block
        self.previous_hash = previous_hash  # Hash of the previous block
        self.hash = self.calc_hash()  # Hash of the current block
    
    def calc_hash(self):
        """
        Calculate the SHA-256 hash of the block's data.
        
        Returns:
        - Hexadecimal string representation of the hash digest.
        """
        sha = hashlib.sha256()
        hash_str = self.data.encode("utf-8")  # Encode data as UTF-8 bytes
        sha.update(hash_str)  # Update the hash object with the encoded data
        return sha.hexdigest()  # Return the hexadecimal representation of the hash

# Instantiate the blockchain with initial blocks
blockchain = [Block("First block", "0")]  # Genesis block with previous hash "0"
blockchain.append(Block("Second block", blockchain[0].hash))  # Second block with hash of first block
blockchain.append(Block("Third block", blockchain[1].hash))  # Third block with hash of second block

# Dumping the blockchain: Display details of each block
for block in blockchain:
    print(
        f"Timestamp: {block.timestamp}\nData: {block.data}\nPrevious Hash: "
        f"{block.previous_hash}\nHash: {block.hash}\n"
    )
