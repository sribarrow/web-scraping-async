from src.scrape_w_sess import get_session
import pytest

# def test_connection()-> None:
#     try:
#         get_session()
#     except NameError as e:
#         # assert isinstance(e, Exception)
#         pytest.fail("Module does not exist.")

# Component Testing    
def test_get_session()-> None:
    try:
        get_session()
    except NameError as e:
        # assert isinstance(e, Exception)
        pytest.fail("Module does not exist.")
        
# Unit Testing