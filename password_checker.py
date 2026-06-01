password = input("Enter a password: ")

length = len(password)
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_symbol = any(not char.isalnum() for char in password)

if length >= 8 and has_upper and has_lower and has_digit and has_symbol:
    print("Password Strength: Strong")

elif length >= 6 and ((has_upper and has_digit) or (has_lower and has_digit)):
    print("Password Strength: Medium")

else:
    print("Password Strength: Weak")