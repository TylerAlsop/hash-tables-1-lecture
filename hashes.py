# Create a funciton that is deterministic (A specified input will always return the same output).

def my_hash(s, limit):
    # Take every character in the string and convert it to a number.
    # Convert each character into UTF-8 numbers.
    string_utf = s.encode()

    total = 0
    for character in string_utf:
        total += character
        total &= 0xffffffff  # Limit total to 32 bits.
    return total % limit

hash_table = [None] * 8 # Make sure that the length is a power of 2.

# Add items to hash_table using the my_hash function.
# Hash the key to get an index.
# Store the value at the generated index.
index = my_hash('Hello', len(hash_table))
hash_table[index] = 'Value for Hello'

index_2 = my_hash('World', len(hash_table))
hash_table[index_2] = 'Value for World'


# Retrieve some items from hash_table.
# Retrieve the value for "Hello"
index = my_hash('Hello', len(hash_table))
print(hash_table[index])
print(hash_table)