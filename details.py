def read_person_details():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender: ")
    email = input("Enter your email: ")

    person = {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Email": email
    }

    return person

# Example usage
person_info = read_person_details()
print("\nPerson Details:")
for key, value in person_info.items():
    print(f"{key}: {value}")
