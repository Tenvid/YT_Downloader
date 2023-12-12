class VideoFormat:
    _id: int
    _resolution: str
    _has_video: bool
    _has_audio: bool
    _extension: str
    _bit_rate: float

    def __init__(self, video_id: int, resolution: str, has_video: bool, has_audio: bool, extension: str,
                 bit_rate: float):
        self._id = video_id
        self._resolution = resolution
        self._has_video = has_video
        self._has_audio = has_audio
        self._extension = extension
        self._bit_rate = bit_rate

    def has_video(self) -> bool:
        return self._has_video

    def has_audio(self) -> bool:
        return self._has_audio

    def has_video_audio(self) -> bool:
        return self.has_video() and self.has_audio()

    def get_id(self) -> str:
        return self._id

    def __str__(self) -> str:
        return (
            f"ID: {self._id} | Resolution: {self._resolution} | Video: {self._has_video} | Audio: {self._has_audio} | "
            f"Extension: {self._extension} | Bit Rate: {self._bit_rate}")
