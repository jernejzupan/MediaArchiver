import pytest
from archiver import metadata


def test_image_metadata():
    image_path = "test/metadata/test_data/images/DSC_0003.JPG"
    data = metadata.get_image_metadata(image_path)
    assert data["creation_time"] == "2019:04:13 15:03:49"
    assert data["camera_model"] in ["G8441"]


def test_video_metadata():
    video_path = "test/metadata/test_data/video/C0062_SM.mp4"
    data = metadata.get_video_metadata(video_path)
    assert data["creation_time"] == "2020-10-10T19:02:51.000000Z"
