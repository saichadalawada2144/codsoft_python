import random as r
import string as s
def Password_verification_and_print():
    try:
        a=int(input("Enter required length of password:"))
        if a<=0:
            print("Length should be a positive integer.")
        else:
            print(f"Requested password from(0-{a}):",''.join
                  (r.choice(s.ascii_letters + s.digits + s.punctuation) for i in range(a)))
    except ValueError:
        print("Invalid please enter valid integer")
Password_verification_and_print()
