
import pytest
from main import read_csv  

def test_read_csv_valid_file():
    """Test reading a valid CSV file."""
    words = read_csv('tests/sample_data/valid.csv')
    assert len(words) > 0  #valid file

def test_read_csv_empty_file():
    """Test reading an empty CSV file."""
    words = read_csv('tests/sample_data/empty.csv')
    assert words == [] #not valid file
