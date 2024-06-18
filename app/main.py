from dotenv import load_dotenv
import os
import openai
from generate import generate_response, generate_character_image, generate_map
from recognize import recognize_speech
from database import init_db, add_character

# Načtení proměnných prostředí
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def main():
    init_db()
    while True:
        command = recognize_speech()
        if command:
            if "generuj postavu" in command:
                description = generate_response("Popiš postavu pro RPG hru.")
                image_url = generate_character_image(description)
                add_character(description, image_url)
                print(f"Postava: {description}\nObrázek: {image_url}")
            elif "generuj mapu" in command:
                generate_map(10, 25)
            elif "konec" in command:
                break

if __name__ == "__main__":
    main()
