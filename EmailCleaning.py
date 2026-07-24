def write_log(message):
    with open(r"C:\Users\dell\OneDrive\Desktop\program.app", "a") as file:
        file.write(message + "\n")

def email_validation(email):
    return "@" in email and "." in email

def clean_email(email):
    cleaning = email.lower().strip()
    return cleaning

write_log("App started")
email = input("Enter your email:")
email_validation(email)
if not email_validation(email):
    write_log(f"Email is not valid : {email}")
else:
    clean = clean_email(email)
    write_log(f"Processed email : {clean}" )
write_log("App ended")
