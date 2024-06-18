import pytest
from app.generate import generate_response, generate_character_image, generate_map

def test_generate_response():
    response = generate_response("Hello, how are you?")
    assert isinstance(response, str)
    assert len(response) > 0

def test_generate_character_image():
    description = "Test character"
    image_path = generate_character_image(description)
    assert isinstance(image_path, str)
    assert image_path.endswith(".png")

def test_generate_map():
    # Just test if the function runs without errors
    generate_map(10, 25)
