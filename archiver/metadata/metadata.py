import exifread
import ffmpeg
from os import walk, path
import logging

logger = logging.getLogger(__name__)


def get_image_metadata(file_path):
    logger.debug(f"\n\t{file_path}")
    data = _get_image_tags(file_path, tags=["Image Model", "Image DateTime"])
    image_metadata = {
        "creation_time": str(data["Image DateTime"]),
        "camera_model": str(data["Image Model"]),
    }
    logger.debug(f"\n\t{image_metadata}")
    return image_metadata


def _get_image_tags(file_path, tags):
    logger.debug(f"\n\t{file_path}\n\t{tags}")
    with open(file_path, "rb") as file:
        file_tags = exifread.process_file(file)
        collect_tags = {}
        for tag_name in tags:
            collect_tags[tag_name] = file_tags[tag_name]
        logger.debug(f"\n\t{collect_tags}")
        return collect_tags


def get_video_metadata(file_path):
    logger.debug(f"\n\t{file_path}")
    data = _get_video_tags(file_path, ["creation_time"])
    video_metadata = {
        "creation_time": str(data["creation_time"]),
    }
    logger.debug(f"\n\t{video_metadata}")
    return video_metadata


def _get_video_tags(file_path, tags=["creation_time"]):
    logger.debug(f"\n\t{file_path}\n\t{tags}")
    video = ffmpeg.probe(file_path)
    file_tags = video["streams"][0]["tags"]
    collect_tags = {}
    for tag_name in tags:
        collect_tags[tag_name] = file_tags[tag_name]
    logger.debug(f"\n\t{collect_tags}")
    return collect_tags
