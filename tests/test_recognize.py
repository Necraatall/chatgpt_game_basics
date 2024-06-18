import pytest
from app.recognize import recognize_speech

def test_recognize_speech():
    # Test if the function can be called without errors
    # In a real test, you would mock the microphone input
    try:
        recognize_speech()
    except Exception as e:
        pytest.fail(f"recognize_speech raised {type(e).__name__} unexpectedly!")
