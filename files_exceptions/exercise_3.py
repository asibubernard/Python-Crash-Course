# Using While, try/except/else block to create an additin calculator.

print("Give me two numbers and I will add it for you.")

while True:
    first_number = input("First number: ")
    second_number = input("Second number: ")
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Sorry you entered a text instead of an integer.")
    else:
        print(answer)



