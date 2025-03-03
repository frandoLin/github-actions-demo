import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import add_numbers, get_medical_info

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0

def test_get_medical_info():
    assert "liver" in get_medical_info("live").lower()
    assert "not found" in get_medical_info("unknown condition").lower()