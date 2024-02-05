def name_multiplication(names):
    for name in names:
        string_length = len(name)
        for _ in range(string_length):
            print(name)

# Example usage
names = ["John", "Jane", "Alice", "Bob", "Charlie"]
name_multiplication(names)