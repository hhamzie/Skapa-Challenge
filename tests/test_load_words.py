import pytest
from main import load_words  

@pytest.fixture
def test_load_words_valid_input(mocker):
    mocker.patch('main.read_csv', return_value=["apple", "application", "banana", "band", "candy"])

    letters = "aanpple"
    result = load_words(letters)
    assert result == {"apple", "banana"}, "Should include correct words based on the letters provided"

def test_load_words_no_matching_words(mocker):
    
    mocker.patch('main.read_csv', return_value=["xylophone", "zebra", "quartz"])
    letters = "aanpple"
    result = load_words(letters)

    assert result == set(), "Should return an empty set for no matching words"

