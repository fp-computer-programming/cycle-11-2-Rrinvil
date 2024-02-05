def is_palindrome(input_string):
    length = len(input_string)
    for i in range(length // 2):
        if input_string[i] != input_string[length - 1 - i]:
                return False
     
    return True

test_string = "ryan"
result = is_palindrome(test_string)

if result:
    print(f"'{test_string}' is a palindrome.")
else:
    print(f"'{test_string}' is not a palindrome.")