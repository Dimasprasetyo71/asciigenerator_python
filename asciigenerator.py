import os
import pyfiglet
from termcolor import colored
from datetime import datetime
import time
from tkinter import filedialog, Tk, messagebox
from PIL import Image, ImageDraw, ImageFont
import random

def get_user_input():
    """Get and validate custom text input from the user."""
    while True:
        text = input("Enter the text you want to convert to ASCII art: ").strip()
        if text and text.isprintable():
            return text
        print("Input cannot be empty or contain special characters. Please try again.")

def get_multiple_lines_input():
    """Get multiple lines of input from the user."""
    print("Enter the text you want to convert to ASCII art (type 'done' on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line.lower() == 'done':
            break
        lines.append(line)
    return "\n".join(lines)

def get_font_choice():
    """Allow user to choose a font for the ASCII art."""
    fonts = pyfiglet.FigletFont.getFonts()
    print(f"Available fonts: {', '.join(fonts[:10])}...")
    font = input("Enter the font for your ASCII art (or press Enter for default 'slant'): ").strip() or 'slant'
    
    if font not in fonts:
        print("Invalid font selected. Defaulting to 'slant'.")
        font = 'slant'
    
    return font

def get_color_choice():
    """Allow user to choose a color for the ASCII art."""
    available_colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    color = input(f"Enter the color for your ASCII art ({', '.join(available_colors)}): ").lower().strip()
    
    if color not in available_colors:
        print("Invalid color selected. Defaulting to 'cyan'.")
        color = 'cyan'
    
    return color

def show_loading_spinner():
    """Show a loading spinner while generating ASCII art."""
    spinner = ['|', '/', '-', '\\']
    for _ in range(10):  
        for symbol in spinner:
            print(f"\rGenerating ASCII Art... {symbol}", end='', flush=True)
            time.sleep(0.2)
    print("\rDone!                            ")

def preview_ascii_art(result):
    """Preview the ASCII art before saving."""
    preview_choice = input("Do you want to preview the ASCII art? (yes/no): ").strip().lower()
    if preview_choice == "yes":
        print("\nPreviewing ASCII Art...\n")
        print(result)
    else:
        print("\nSkipping preview.\n")

def preview_ascii_art_in_popup(result):
    """Preview the ASCII art in a pop-up window."""
    from tkinter import Text, Scrollbar
    
    window = Tk()
    window.title("Preview ASCII Art")
    
    scrollbar = Scrollbar(window)
    scrollbar.pack(side='right', fill='y')

    text_box = Text(window, wrap='word', width=80, height=20, yscrollcommand=scrollbar.set)
    text_box.insert('1.0', result)
    text_box.config(state='disabled')
    text_box.pack(padx=10, pady=10)

    scrollbar.config(command=text_box.yview)
    window.mainloop()

def get_save_path():
    """Allow user to specify custom file path via file dialog or current directory."""
    print("\nYour ASCII art will be saved in the selected folder or current directory.")
    root = Tk()
    root.withdraw()  # Hide the root window
    custom_path = filedialog.askdirectory(title="Select Folder to Save ASCII Art")
    
    if not custom_path:  
        print("No folder selected. Saving in the current directory.")
        custom_path = os.getcwd()

    return custom_path

def check_file_exists(filepath):
    """Check if a file already exists and prompt user to overwrite or create a new file."""
    if os.path.exists(filepath):
        choice = input(f"File {filepath} already exists. Overwrite? (yes/no): ").strip().lower()
        return choice == 'yes'
    return True

def save_ascii_art(result):
    """Save the ASCII art to a file with timestamp or custom filename."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = input("Enter the filename (or press Enter to use default): ").strip()
    if not filename:
        filename = f"dimas_{timestamp}.txt"
    
    custom_path = get_save_path()
    filepath = os.path.join(custom_path, filename)
    
    if not check_file_exists(filepath):  
        print("File not saved.")
        return

    print(f"Saving to: {filepath}...")
    
    try:
        with open(filepath, "w") as file:
            file.write(result)
        print(f"ASCII art saved to {filepath}")
    except IOError:
        print("Error: Unable to write to file. Check permissions.")

def get_file_format_choice():
    """Ask the user for the file format (txt, md, html)."""
    formats = ['txt', 'md', 'html']
    print(f"Available formats: {', '.join(formats)}")
    format_choice = input(f"Enter the format for your ASCII art file ({', '.join(formats)}): ").strip().lower()
    if format_choice not in formats:
        print("Invalid format selected. Defaulting to 'txt'.")
        format_choice = 'txt'
    return format_choice

def generate_ascii_art(text, font, color):
    """Generate ASCII art and apply color."""
    result = pyfiglet.figlet_format(text, font=font)
    colored_result = colored(result, color)
    return colored_result

def generate_random_ascii_art():
    """Generate a random ASCII art with random text, font, and color."""
    random_text = random.choice(["Hello", "World", "Python", "Coding", "ASCII Art"])
    random_font = random.choice(pyfiglet.FigletFont.getFonts())
    random_color = random.choice(['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'])
    
    print(f"Generating random ASCII art for text: {random_text}, font: {random_font}, color: {random_color}")
    return generate_ascii_art(random_text, random_font, random_color)

def save_ascii_art_as_image(result, filename, font_size=20):
    """Convert ASCII art to an image and save it with a given font size."""
    image = Image.new('RGB', (600, 400), color='white')
    draw = ImageDraw.Draw(image)
    
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
        draw.text((10, 10), result, font=font, fill='black')
        image.save(f"{filename}.png")
        print(f"Image saved as {filename}.png")
    except Exception as e:
        print(f"Error: {e}")

def main():
    """Main function to control the flow of the program."""
    while True:
        choice = input("Do you want to generate custom ASCII art or random? (custom/random): ").strip().lower()
        if choice == 'random':
            result = generate_random_ascii_art()
        else:
            text = get_user_input()
            font = get_font_choice()
            color = get_color_choice()

            show_loading_spinner()

            result = generate_ascii_art(text, font, color)

        print(result)

        preview_ascii_art(result)

        if input("Do you want to preview in pop-up? (yes/no): ").strip().lower() == "yes":
            preview_ascii_art_in_popup(result)

        save_ascii_art(result)

        if input("Do you want to save as image? (yes/no): ").strip().lower() == "yes":
            file_format = get_file_format_choice()
            save_ascii_art_as_image(result, f"dimas_{datetime.now().strftime('%Y%m%d_%H%M%S')}")

        # Ask if user wants to generate another ASCII art
        if input("Do you want to generate another ASCII art? (yes/no): ").strip().lower() != 'yes':
            break

if __name__ == "__main__":
    main()
