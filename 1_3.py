user_input = [char for char in input() if char.isalnum()]
if user_input == user_input[::-1]:
    print(True)
else:
    print(False)
