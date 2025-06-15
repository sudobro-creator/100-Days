#Requirement: Run `pip install pyfiglet` to use this script.

import pyfiglet
import random

def generate_father_day_message():
    messages = "Happy Father's Day! 🎉\n" 
    fonts = pyfiglet.FigletFont.getFonts()
    selected_font = random.choice(fonts)
    ascii_art = pyfiglet.figlet_format(messages, font=selected_font)
    return ascii_art

fathers_day_wish = generate_father_day_message()

print(fathers_day_wish)