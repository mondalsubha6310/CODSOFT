import customtkinter as ctk  # type: ignore
import random
import string

# Function 
def generate_password():
    try:
        length_str = entry_length.get().strip()
        if not length_str.isdigit():
            label_status.configure(text="Error: Enter a valid number!", text_color="red")
            return
        
        length = int(length_str)
        if length <= 0:
            label_status.configure(text="Error: Length must be positive!", text_color="red")
            return

        characters = ""
        if var_numbers.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation
        if var_lowercase.get():
            characters += string.ascii_lowercase
        if var_uppercase.get():
            characters += string.ascii_uppercase

        if not characters:
            label_status.configure(text="Error: Select at least one character set!", text_color="red")
            return

        # Generate password 
        password = ''.join(random.choice(characters) for _ in range(length))
        entry_password.configure(state="normal")  # Enable entry for inserting text
        entry_password.delete(0, ctk.END)
        entry_password.insert(0, password)
        entry_password.configure(state="readonly")  # Make it read-only
        label_status.configure(text="Password generated successfully!", text_color="green")
    except ValueError:
        label_status.configure(text="Error: Invalid input!", text_color="red")


# Function to copy the password 
def copy_to_clipboard():
    password = entry_password.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update_idletasks()  # More stable than root.update()
        label_status.configure(text="Password copied to clipboard!", text_color="green")
    else:
        label_status.configure(text="Error: No password to copy!", text_color="red")


# Create the main window
ctk.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

root = ctk.CTk()
root.title("Custom Password Generator")
root.geometry("500x550")
root.resizable(False, False)

label_title = ctk.CTkLabel(root, text="Custom Password Generator", font=("Arial", 20, "bold"))
label_title.pack(pady=10)

# Length Input Frame
frame_length = ctk.CTkFrame(root)
frame_length.pack(pady=10, padx=20, fill="x")

label_length = ctk.CTkLabel(frame_length, text="Password Length:", font=("Arial", 14))
label_length.pack(side="left", padx=10, pady=5)

entry_length = ctk.CTkEntry(frame_length, width=150, font=("Arial", 14))
entry_length.pack(side="left", padx=10)

# Character Set Selection
frame_characters = ctk.CTkFrame(root)
frame_characters.pack(pady=10, padx=20, fill="x")

label_characters = ctk.CTkLabel(frame_characters, text="Select Character Sets:", font=("Arial", 14))
label_characters.pack(pady=10)

var_numbers = ctk.BooleanVar(value=False)
check_numbers = ctk.CTkCheckBox(frame_characters, text="Numbers", variable=var_numbers, font=("Arial", 14))
check_numbers.pack(anchor="w", padx=10, pady=5)

var_symbols = ctk.BooleanVar(value=False)
check_symbols = ctk.CTkCheckBox(frame_characters, text="Symbols", variable=var_symbols, font=("Arial", 14))
check_symbols.pack(anchor="w", padx=10, pady=5)

var_lowercase = ctk.BooleanVar(value=True)  
check_lowercase = ctk.CTkCheckBox(frame_characters, text="Lowercase Letters", variable=var_lowercase, font=("Arial", 14))
check_lowercase.pack(anchor="w", padx=10, pady=5)

var_uppercase = ctk.BooleanVar(value=True)
check_uppercase = ctk.CTkCheckBox(frame_characters, text="Uppercase Letters", variable=var_uppercase, font=("Arial", 14))
check_uppercase.pack(anchor="w", padx=10, pady=5)

# Generate Button
button_generate = ctk.CTkButton(root, text="Generate Password", command=generate_password, width=200, height=40)
button_generate.pack(pady=10)

# Password Display
entry_password = ctk.CTkEntry(root, width=300, font=("Arial", 14), justify="center", state="readonly")
entry_password.pack(pady=10)

# Copy to Clipboard Button
button_copy = ctk.CTkButton(root, text="Copy to Clipboard", command=copy_to_clipboard, width=200, height=40)
button_copy.pack(pady=10)

label_status = ctk.CTkLabel(root, text="", font=("Arial", 12))
label_status.pack(pady=10)

# Run the main loop
root.mainloop()