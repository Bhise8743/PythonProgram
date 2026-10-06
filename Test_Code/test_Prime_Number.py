from Code.Prime_Number import is_prime

def test_11_is_prime():
    assert is_prime(11) == True
    

def test_47_is_prime():
    assert is_prime(47) == True
    
def test_22_is_prime():
    assert is_prime(22) == False
    
# python -m pytest .\Test_Code\test_Prime_Number.py
