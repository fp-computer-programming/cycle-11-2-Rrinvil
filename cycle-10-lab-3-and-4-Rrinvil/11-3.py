import random 
random_integer = random.randint(1, 100)
def number_guess(rnumber):
    user_input = input("Please enter a number: ")
    number = int(user_input)
    while number != rnumber:
        print('wrong, do better')
        user_input = input("Please enter a number: ")
        number = int(user_input)
        
    print("congrats!")

    
        

    
number_guess(random_integer)
