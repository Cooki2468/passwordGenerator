import random
import tkinter as tk
from tkinter import ttk

# Window setup

root = tk.Tk()
root.title('Password generator')
#root['bg'] = 'grey'


def generatePassword(length):
    # Define valid characters to generate password

    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '@', '#', '$' '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '<', '>', '?', '/']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    valid_characters = letters + symbols + numbers
    random.shuffle(valid_characters)
    random_numbers = []
    password = ''
    
    # Create list with random numbers to later change them to characters

    for i in range(length):
        random_numbers.append(random.randrange(0, len(valid_characters)))
    
    for j in range(length):
        # Change random letters to lowercase

        ifLowercase = random.randrange(1, 3)
        if valid_characters[random_numbers[j]] in letters:
            if ifLowercase % 2 == 0:
                valid_characters[random_numbers[j]] = valid_characters[random_numbers[j]].lower()

        password = password + valid_characters[random_numbers[j]]
    
    # Return password

    return password

# Create function that shows generated password

def showGeneratedPassword(text, length_entry):
    length = int(length_entry.get())
    entry_content = text.get()
    text.delete(0, length)
    text.insert(0, generatePassword(length))


# Get screen dimensions

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
win_height = 300
win_width = 300

# Find screen center

center_x = int(screen_width / 2 - win_width / 2)
center_y = int(screen_height / 2 - win_height / 2)

# Set window size

root.geometry(f'{win_width}x{win_height}+{center_x}+{center_y}')
root.resizable(False, False)

# Set icon

root.iconbitmap('favicon.ico')

# Display widgets

password_message = tk.Entry(root)

password_length_label = ttk.Label(root, text="Password length")

password_length_entry = ttk.Entry()
password_length_entry.insert(0, "12")

generate_password_button = ttk.Button(
    root,
    text='Generate Password',
    command=lambda: showGeneratedPassword(password_message, password_length_entry))

password_message.pack()
password_length_label.pack()
password_length_entry.pack()
generate_password_button.pack()



# Keep the window displaying

root.mainloop()