import pytest
from firstproj import speak


def test_speak(capsys):
    # Call the function
    speak()

    # Capture the output
    captured = capsys.readouterr()

    # Assert that the output is correct
    assert captured.out == "11\n"
