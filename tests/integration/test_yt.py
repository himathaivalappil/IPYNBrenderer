import pytest
from IPYNBrenderer import render_youtube_video
from IPYNBrenderer.custom_exception import InvalidURLException

class TestYTRenderer:
    URL_test_success_data = [
    ("https://www.youtube.com/watch?v=twpO0KbJ28M", "Success!"),
    ("https://youtu.be/twpO0KbJ28M", "Success!"),
    ("https://youtu.be/1-68pFs_HIE?t=45", "Success!"),
    ("https://www.youtube.com/watch?v=1-68pFs_HIE&list=PLrdaCCBhU_hlLUujFA5KUjb3yathXilut&index=4&t=54s", "Success!")
    ]

    URL_test_bad_data = [
    ("https://www.youtube.com/watch?v=twpOdfghfgh0KbJ28M"),
    ("https://youtu.be/twpO0KbJ28M?&&&t"),
    ("https://youtu.be/1-68pFs_HIE?tt=-45"),
    ("https://www.youtube.com/watch?v=1-68pFs_HIE&list=PLrdaCCBhU_hlLUujFA5KUjb3yathXilut&index=4&t==45s"),
    ("https://www.youtube.com/watch?v=1-68pFs_HIE&list=PLrdaCCBhU_hlLUujFA5KUjb3yathXilut&index=4t=54s")
    ]

    @pytest.mark.parametrize("URL, response", URL_test_success_data)
    def test_render_yt_success(self, URL, response):
        assert render_youtube_video(URL) == response

    @pytest.mark.parametrize("URL", URL_test_bad_data)
    def test_render_yt_fail(self, URL):
        with pytest.raises(InvalidURLException):
            render_youtube_video(URL)
