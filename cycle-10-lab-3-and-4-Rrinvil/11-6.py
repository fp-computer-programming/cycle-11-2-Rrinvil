sum = 0

while True:
    number = int(input("Enter a number: "))
    if number == -1:
        break
    sum += number

print("The sum of all the numbers entered is:", sum)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 3 == 0:
        print(number)
    continue
