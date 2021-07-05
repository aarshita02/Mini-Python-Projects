# The strip function will remove any trailing spaces on both the sides
email = input("Enter your e-mail: ").strip()
username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

# f-string is an alternative to format function
print(f"Your username is {username} & domain is {domain}")
