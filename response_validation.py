from validator_collection import checkers
email = input("What's your email address? ")

if correct_email := checkers.is_email(email):
    print("Valid")
else:
    print("Invalid")
