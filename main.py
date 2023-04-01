import random
import tkinter as tk
from tkinter import ttk

# Window setup

root = tk.Tk()
root.title('Password generator')
#root['bg'] = '#856ff8'


def generatePassword(length):
    # Define valid characters to generate password

    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '@', '#', '$' '%', '^', '&', '*', '_', '=', '?', '/']
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
    text.delete(0, length+1)
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

# Create grid

root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=2)
root.columnconfigure(2, weight=2)

# Display widgets

padding = {'ipadx': 0, 'ipady': 0}
margin = {'padx': 5, 'pady': 5}
style = ttk.Style()

password_length_label = ttk.Label(root, text="Password length")
password_length_label.grid(column=0, row=0, **padding, **margin)

password_length_entry = ttk.Entry(root)
password_length_entry.insert(0, "12")
password_length_entry.grid(column=1, row=0, **padding, **margin, sticky=tk.E)

password_message_label = ttk.Label(root, text='Your password')
password_message_label.grid(column=0, row=1, **padding, **margin)

password_message = ttk.Entry(root)
password_message.grid(column=1, row=1, **padding, **margin, sticky=tk.E)

generate_password_button = ttk.Button(
    root,
    text='Generate Password',
    command=lambda: showGeneratedPassword(password_message, password_length_entry))

generate_password_button.grid(column=1, row=2, sticky=tk.E, **padding, **margin)

# Keep the window displaying

root.mainloop()