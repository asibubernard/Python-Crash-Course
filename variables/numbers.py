# Avoiding Type error with the str() Function/method

# age = 23
# message = "Happy " + age + "rd Birthday!"

# print(message)

# str() converts integers to strings
age = 23
message = "Happy " + str(age) + "rd Birthday!"

print(message)