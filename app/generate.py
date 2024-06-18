import openai
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

openai.api_key = 'tvůj_api_klíč'

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-004",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def generate_character_image(description):
    response = openai.Image.create(
        prompt=description,
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']
    return image_url

def generate_map(size, cell_size):
    map_image = Image.new("RGB", (size * cell_size, size * cell_size), (255, 255, 255))
    draw = ImageDraw.Draw(map_image)
    
    for i in range(0, size * cell_size, cell_size):
        draw.line([(i, 0), (i, size * cell_size)], fill=(0, 0, 0))
        draw.line([(0, i), (size * cell_size, i)], fill=(0, 0, 0))

    plt.imshow(map_image)
    plt.show()
