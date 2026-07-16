def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(not c.isalnum() for c in password):
        score += 1

    if score == 5:
        print("Strong Password")
    elif score >= 3:
        print("Medium Password")
    else:
        print("Weak Password")

password = input("Enter a password: ")
check_password_strength(password)
