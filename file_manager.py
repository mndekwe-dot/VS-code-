# file_manager.py

def save_message(message):
    try:
        file = open("user_message.txt", "w")
        file.write(message)
        file.close()
        print("Message saved successfully.")
    except:
        print("Something went wrong while saving the file.")


def read_message():
    try:
        file = open("user_message.txt", "r")
        print("Reading saved message...")
        print(file.read())
        file.close()
    except:
        print("Could not read the file.")
