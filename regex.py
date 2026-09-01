import re
while True:
    try:
        email = input("Enter email: ").strip()
        pattern = r"^[a-z0-9A-Z.]+@alustudent\.com$"
        if re.match(pattern, email):
            print("Valid EMAil")
            break   
    except Exception as e:
        print(f"ERROR: {e}")
