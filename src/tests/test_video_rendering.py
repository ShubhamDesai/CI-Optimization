# test_video_rendering.py

from video_rendering import render_high_quality_video

def test_render_high_quality_video():
    result = render_high_quality_video()
    assert result == "Video Rendering Complete"
