import hashlib
import json
import os

STATIC_SALT = "a_secure_static_salt_for_this_demo"
DATA_FILE = "user_data.json" # File to store user data

def load_users():
    """Load user data from the JSON file."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Warning: User data file is corrupted. Starting with an empty database.")
            return {}
    return {}

def save_users(data):
    """Save user data to the JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

users = load_users()

def hash_sha256(password: str) -> str:
    salted_password = STATIC_SALT + password
    return hashlib.sha256(salted_password.encode('utf-8')).hexdigest()

def login ():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        if username in users:
            input_hash = hash_sha256(password)
            if users[username] == input_hash:
                print(f"Welcome, {username}! You have successfully logged in.")
                break
            else:
                print("\033[31mWarning: Access Denied\nIncorrect Password, Please check again\n\033[0m")
        
        elif username not in users:
            print(f"User '{username}' not found. Let's register.")
            register()

def register():
    while True:
        username = input("Enter a new username: ")

        if username in users:
            print("Username already exists. Please choose a different one.")
        else:
            password = input("Enter a password: ")
            
            hashed_password = hash_sha256(password)
            users[username] = hashed_password
            save_users(users)
            
            print(f"User '{username}' registered successfully!")
            break
            
if __name__ == '__main__':
    running = input("Do you want to start the program (y/n): ").strip().lower()
    if running == 'y':
        login()
    else:
        pass