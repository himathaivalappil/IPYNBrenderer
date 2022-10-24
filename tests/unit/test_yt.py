import pytest
from IPYNBrenderer.custom_exception import InvalidURLException
from IPYNBrenderer import get_time_info

good_URL_data = [
    ("https://www.youtube.com/watch?v=twpO0KbJ28M", 0),
    ("https://youtu.be/twpO0KbJ28M", 0),
    ("https://youtu.be/1-68pFs_HIE?t=45", 45),
    ("https://www.youtube.com/watch?v=1-68pFs_HIE&list=PLrdaCCBhU_hlLUujFA5KUjb3yathXilut&index=4&t=54s", 54)
]

@pytest.mark.parametrize("URL, response", good_URL_data)
def test_get_time_info(URL, response):
    assert get_time_info(URL) == response


