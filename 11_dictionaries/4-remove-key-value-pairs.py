# Remove Key-Value Pairs

# Run: python3 11_dictionaries/4-remove-key-value-pairs.py

# Use the del statement or pop() method to remove key-value pairs from a dictionary.

person = {"name": "John", "age": 25, "city": "New York", "country": "USA"}
del person["country"]  # Delete by key
person.pop("age")  # Remove and return value
print(person)
