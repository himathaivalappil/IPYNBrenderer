
from IPython import display
from ensure import ensure_annotations
from IPYNBrenderer.custom_exception import InvalidURLException
from IPYNBrenderer.logger import logger
from py_youtube import Data


@ensure_annotations
def get_time_info(URL: str) -> int:
    def _verify_vide_id_len(vid_ID, __expected_length=11):
        len_video_id = len(vid_ID)
        if len_video_id != __expected_length:
            raise InvalidURLException(
                f"Invalid video ID with length: {len_video_id}, expected length: {__expected_length}"
                )

    try:
        split_val = URL.split("=")
        if len(split_val) > 5:
            raise InvalidURLException
        if "watch" in URL:
            if ("&t" in URL):
                vid_id, time = split_val[1][0:11], int(split_val[-1][0:-1])
                _verify_vide_id_len(vid_id)
                logger.info(f"video starts at {time}")
                return time
            else:
                vid_id, time = split_val[-1], 0
                _verify_vide_id_len(vid_id)
                logger.info(f"video starts at {time}")
                return time
        else:
            if ("=" in URL) and ("?t" in URL):
                vid_id, time = split_val[0].split("/")[-1][0:-2], int(split_val[-1])
                _verify_vide_id_len(vid_id)
                logger.info(f"video starts at {time}")
                return time
            else:
                vid_id, time = URL.split("/")[-1], 0
                _verify_vide_id_len(vid_id)
                logger.info(f"video starts at {time}")
                return time
    except Exception:
        raise InvalidURLException


@ensure_annotations
def render_youtube_video(URL: str, width: int = 780, height: int = 600) -> str:
    try:
        if URL is None:
            raise InvalidURLException("URL cannot be None")
        data = Data(URL).data()
        if data["publishdate"] is not None:
            time = get_time_info(URL)
            vid_ID = data["id"]
            embed_url = f"https://www.youtube.com/embed/{vid_ID}?start={time}"
            logger.info("embed URL: {}".format(embed_url))
            iframe = """<iframe
            width="{width}" height="{height}"
            src="https://www.youtube.com/embed/1-68pFs_HIE?start=717"
            title="YouTube video player" frameborder="0"
            allow="accelerometer; autoplay; clipboard-write;
            encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen>
            </iframe>
            """

            display.display(display.HTML(iframe))
            return "Success!"
        else:
            raise InvalidURLException("Publish date cannot be None")
    except Exception as e:
        raise e
