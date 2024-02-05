def length_multiples(lst):
    return [value * index for index, value in enumerate(lst)]

# Test cases
print(length_multiples([1, 2, 3, 4, 5]))  # Test case with only integers
print(length_multiples([1.5, 2.5, 3.5, 4.5, 5.5]))  # Test case with integers and float values
print(length_multiples(["a", "bb", "ccc", "dddd"]))  # Test case with only strings