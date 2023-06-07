"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""


class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """
        * Input a string that's stored in the table.
            - First check if the index in the hash table is empty and put the value there if it is.
            - If it is not empty, check if the string appears in the index:
                ### In the case of key, value pairs:
                - if present, update the value
                - if not just add it.
                ### In the case of just an array of values:
                - just append it.
        """

        index = self.calculate_hash_value(string)
        if self.table[index] == None:
            self.table[index] = [string]
        elif self.table[index]:
            self.table[index].append(string)

    def lookup(self, string):
        """
        *Return the hash value if the string is already in the table. Return -1 otherwise.
            - Get the hash value.
            - If the table at that index is None, return -1.
            - If there the table at that index is not empty:
                loop through each element of the array at that point and check for the string.
        """
        index = self.calculate_hash_value(string)
        if self.table[index] == None:
            return -1
        elif self.table[index]:
            for item in self.table[index]:
                if item == string:
                    return index
            return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        hash_value = int(str(ord(string[0])) + str(ord(string[1])))
        return hash_value


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))
