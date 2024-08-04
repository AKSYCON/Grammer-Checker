import tkinter as tk
from tkinter import scrolledtext
import language_tool_python

# Initialize the grammar checking tool
tool = language_tool_python.LanguageTool('en-US')

def check_grammar():
    text_to_check = check_text_box.get("1.0", tk.END).strip()
    
    if not text_to_check:
        result_label.config(text="Please enter the text to check.")
        return
    
    # Check grammar using language_tool_python
    matches = tool.check(text_to_check)
    
    if not matches:
        result_label.config(text="No grammatical errors found!")
    else:
        result_text = f"Found {len(matches)} issues:\n"
        for match in matches:
            result_text += f"- {match.message} (from {match.offset} to {match.offset + match.errorLength})\n"
        result_label.config(text=result_text)

# Setting up the main window
root = tk.Tk()
root.title("Grammar Checker")

# Configure the style of the window
root.configure(bg="#f0f0f0")

# Text to check input
tk.Label(root, text="Text to Check:", bg="#f0f0f0", font=("Arial", 12, "bold")).pack(padx=20, pady=5, anchor="w")
check_text_box = scrolledtext.ScrolledText(root, width=80, height=15, font=("Arial", 12), bg="#ffffff", fg="#000000", bd=2, relief="sunken")
check_text_box.pack(padx=20, pady=5)

# Check button
check_button = tk.Button(root, text="Check Grammar", command=check_grammar, font=("Arial", 12), bg="#4CAF50", fg="#ffffff", bd=0, relief="raised", padx=10, pady=5)
check_button.pack(padx=20, pady=10)

# Result label
result_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 12), wraplength=600, justify="left")
result_label.pack(padx=20, pady=10)

# Run the application
root.mainloop()
