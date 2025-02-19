import random
import string
import subprocess



# Function to generate random passwords based on user data
def generate_passwords(user_data):
    # Extract the user data
    name, age, likes, dog_name, color, birthplace, movie, memorable_year = user_data

    # Passwords with combinations of weak structures
    weak_passwords = [
        name.lower() + str(age) if name else str(age),
        dog_name.lower() + str(age) if dog_name else str(age),
        likes.lower() + "123" if likes else "123",
        name.lower() + "2025" if name else "2025",
        color.lower() + str(age) if color else "color123",
        birthplace.lower() + str(age) if birthplace else "city123",
        movie.lower() + "2025" if movie else "movie123",
        memorable_year if memorable_year else "2025"
    ]
    
    # Medium strength passwords, combining different user data
    medium_passwords = [
        name.lower() + dog_name.capitalize() if name and dog_name else "default123",
        likes.capitalize() + str(age) if likes else "default" + str(age),
        name.capitalize() + likes.capitalize() if name and likes else "default",
        name + dog_name + str(random.randint(100, 999)) if name and dog_name else "default" + str(random.randint(100, 999)),
        color.capitalize() + memorable_year if color and memorable_year else "color2025",
        birthplace.capitalize() + movie.capitalize() if birthplace and movie else "cityMovie123",
        name.capitalize() + memorable_year if name and memorable_year else "default2025",
        random.choice(string.ascii_uppercase) + dog_name.capitalize() + str(random.randint(1000, 9999)) if dog_name else "random2025",
        name.capitalize() + str(random.randint(1000, 9999)) + random.choice(string.punctuation)
    ]
    
    # Strong passwords with a lot more randomness, longer length
    strong_passwords = [
        ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12)),
        name.capitalize() + str(random.randint(1000, 9999)) + dog_name.capitalize() + random.choice(string.punctuation) if name and dog_name else ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=16)),
        ''.join(random.choices(string.ascii_uppercase + string.digits + string.punctuation, k=16)),
        random.choice(string.ascii_uppercase) + dog_name.lower() + str(random.randint(100, 999)) + random.choice(string.punctuation) if dog_name else ''.join(random.choices(string.ascii_uppercase + string.digits + string.punctuation, k=16)),
        ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=20)),
        random.choice(string.ascii_uppercase) + birthplace.lower() + memorable_year + random.choice(string.punctuation) if birthplace and memorable_year else ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=18)),
        ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k=24)),
        name.capitalize() + memorable_year + dog_name.lower() + random.choice(string.punctuation) if name and dog_name and memorable_year else ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=20)),
        ''.join(random.choices(string.ascii_lowercase + string.digits + string.punctuation, k=30)),
        random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation) + random.choice(string.ascii_letters) + ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=15))
    ]
    
    # Extremely strong passwords, using longer and more complex elements
    very_strong_passwords = [
        ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=32)),
        ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k=40)),
        ''.join(random.choices(string.ascii_uppercase + string.digits + string.punctuation, k=36)),
        random.choice(string.ascii_uppercase) + ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=35)),
        random.choice(string.ascii_lowercase) + random.choice(string.digits) + ''.join(random.choices(string.ascii_letters + string.punctuation, k=30)),
        ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=48)),
        ''.join(random.choices(string.ascii_uppercase + string.digits + string.punctuation, k=50)),
    ]
    
    # Combine all passwords into one list
    all_passwords = weak_passwords + medium_passwords + strong_passwords + very_strong_passwords
    return all_passwords

# Function to save passwords to a file
def save_passwords_to_file(passwords):
    with open('passwords.txt', 'a') as file:
        for password in passwords:
            file.write(password + "\n")
    print("Passwords added to 'passwords.txt'.")

# Function to get user input for name, age, favorite things, dog name, and additional questions
def get_user_data():
    print("Please enter your data to generate passwords (Press Enter to skip any question):")
    
    name = input("What is your name? (Optional) ")
    age = input("How old are you? (Optional) ")
    likes = input("What are some things you like? (Optional, e.g., music, sports, etc.) ")
    dog_name = input("What is your dog's or cats name? (Optional) ")
    color = input("What is your favorite color? (Optional) ")
    birthplace = input("When were you born? (Optional) ")
    movie = input("What is your favorite movie or book? (Optional) ")
    memorable_year = input("What are the names of important people in youre life? (Optional) ")

    # Make sure the age is an integer if it's provided
    if age and not age.isdigit():
        print("Age should be a number. Setting age to '' by default.")
        age = ""
    
    return name, age, likes, dog_name, color, birthplace, movie, memorable_year

# Main function
def main():
    
    user_data = get_user_data()  # Gather user input
    passwords = generate_passwords(user_data)  # Generate passwords
    save_passwords_to_file(passwords)  # Save to file

if __name__ == "__main__":
    main()
