
user_input = input().split()
unique_chars = set(user_input)
filtered_chars = [char for char in unique_chars if char.isalpha()]
print(*sorted(filtered_chars))
