from validator_collection import validators

def main():
    email_address = input("Type your email adress: ")
    try:
        valid_email = validators.email(email_address)
        print("Valid")
    except:
        print("Invalid")

if __name__ == "__main__":
    main()
