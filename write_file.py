"""
This script will ask user for name, favorite color, pets name, 
mother's maiden name, and elementary school
"""

# Function to collect user information
def collect_user_data():
    print("Please answer the following questions")
    name = input("What is your name: ")
    favorite_color = input("What is your favorite color?: ")
    first_pet = input("What is your first pet's name?: ")
    mothers_maiden_name = input("What is your mother's maiden name?: ")
    elementary_school = input("What elementary school did you attend?: ")

    # Return collected info as a dictionary
    return {
        "Name":name,
        "Favorite Color":favorite_color,
        "First Pet":first_pet,
        "Mothers miaden name":mothers_maiden_name,
        "Elementary School":elementary_school,

    }


#Function to save information to a file
def save_to_file(data, filename="hackme.txt"):
     with open(filename, "w") as file:
         for key, value in data.items():
                file.write(f"{key}: {value}\n")
                print(f"Information has been saved to {filename}.")

# Collect and save user information
save_to_file(collect_user_data())

