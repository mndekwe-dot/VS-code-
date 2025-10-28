def validate_input(user_input):
    if user_input != "":
        return True
    else:
        return False


def convert_to_binary(text):
    # If it's a number
    if text.isdigit():
        return bin(int(text))
    else:
        # Convert each letter to binary (ASCII)
        binary_text = ""
        for char in text:
            binary_text += format(ord(char), "08b") + " "
        return binary_text.strip()


def create_message(name, age, name_binary, age_binary):
    message = "Hello " + name + ", you are " + age + " years old!\n"
    message += "Name in binary: " + name_binary + "\n"
    message += "Age in binary: " + age_binary
    return message
