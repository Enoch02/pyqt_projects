import requests
from PySide6.QtCore import QRunnable, Slot
from signals import GalleryWorkerSignals, ImageLoaderSignals


# TODO: better error messages?
class ImageGalleryWorker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = GalleryWorkerSignals()

    @Slot()
    def run(self) -> None:
        try:
            response = requests.get("https://nekos.best/api/v2/neko?amount=20")

            if response.status_code == 200:
                images: list[dict[str, str]] = response.json()["results"]
                self.signals.success.emit(images)

        except Exception as e:
            self.signals.failure.emit(str(e))


# TODO: add a caching
class ImageLoaderWorker(QRunnable):
    def __init__(self, url: str):
        super().__init__()
        self.url = url
        self.signals = ImageLoaderSignals()

    @Slot()
    def run(self) -> None:
        self.signals.loading.emit(True)
        try:
            response = requests.get(self.url)

            if response.status_code == 200:
                image_bytes = response.content
                self.signals.success.emit(image_bytes)

        except Exception as e:
            self.signals.loading.emit(False)
            self.signals.failure.emit(str(e))

        self.signals.loading.emit(False)
