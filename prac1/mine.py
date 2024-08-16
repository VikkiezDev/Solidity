import hashlib

def sha256(message):
    """ 
    Calculates the SHA-256 hash of a message.
    
    Args:
    - message: The input message to be hashed (in ASCII format).
    
    Returns:
    - Hexadecimal string representation of the hash digest.
    """
    return hashlib.sha256(message.encode("ascii")).hexdigest()

def mine(message, difficulty=1):
    """
    Mines a block to find a nonce (proof of work) that satisfies a given difficulty level.

    Args:
    - message: The message to be mined (typically the block data).
    - difficulty: The number of leading zeros the hash digest must have (default is 1).

    Raises:
    - AssertionError: If difficulty is not an integer or is less than 1.
    """
    assert isinstance(difficulty, int) and difficulty >= 1, "Difficulty must be an integer >= 1"
    
    prefix = "0" * difficulty  # Create a prefix of zeros as per the difficulty
    
    for i in range(1000):
        digest = sha256(str(hash(message)) + str(i))  # Combine message and nonce, then hash it
        
        if digest.startswith(prefix):
            print(f"After {i} iterations, found nonce: {digest}")
            return digest  # Return the found nonce
        
    print(f"No nonce found with difficulty {difficulty}")

# Example usage
if __name__ == "__main__":
    mine("test message", 2)  # Test mining with a test message and difficulty level of 2



#whole code without comments
"""
import hashlib

def sha256(message):
    return hashlib.sha256(message.encode("ascii")).hexdigest()

def mine(message, difficulty=1):
    assert isinstance(difficulty, int) and difficulty >= 1, "Difficulty must be an integer >= 1"
    
    prefix = "0" * difficulty
    
    for i in range(1000):
        digest = sha256(str(hash(message)) + str(i))
        
        if digest.startswith(prefix):
            print(f"After {i} iterations, found nonce: {digest}")
            return digest

"""

