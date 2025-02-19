import random
import nltk
from nltk.corpus import words

nltk.download('words')

english_words = words.words()

common_numbers = [str(i).zfill(3) for i in range(1000)]
common_symbols = ["!", "@", "#", "$", "%", "&", "*"]

def generate_random_password():
    word = random.choice(english_words)
    password_structure = random.choice([
        word + random.choice(common_numbers),
        word + random.choice(common_symbols),
        random.choice(common_numbers) + random.choice(common_symbols),
        word + random.choice(common_numbers) + random.choice(common_symbols),
        random.choice(common_symbols) + word + random.choice(common_numbers),
        random.choice(common_symbols) + random.choice(common_numbers) + word,
    ])
    
    password = ''.join(random.choice([ch.upper(), ch.lower()]) for ch in password_structure)
    return password

def save_passwords_to_file():
    count = 0
    with open('passwords.txt', 'a') as file:
        while count < 1000000:
            password = generate_random_password()
            file.write(password + "\n")
            count += 1
    print("1,000,000 passwords have been added to 'passwords.txt'.")

def main():
    save_passwords_to_file()

if __name__ == "__main__":
    main()
