# Access Values by Key

# Run: python3 11_dictionaries/2-access-values-by-key.py

# Retrieve dictionary values by using the key name in square brackets or the get() method.

person = {"name": "John", "age": 25, "city": "New York"}
print(person["name"])
print(person.get("age"))
print(person.get("country", "Not found"))
