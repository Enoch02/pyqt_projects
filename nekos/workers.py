import os.path

import requests
from PySide6.QtCore import QRunnable, Slot

from signals import GalleryWorkerSignals, ImageLoaderSignals
from util.cache_util import (
    get_item_from_cache,
    save_bytes_as_img,
    load_image_as_byte,
    cache,
)


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


class ImageLoaderWorker(QRunnable):
    def __init__(self, url: str):
        super().__init__()
        self.url = url
        self.signals = ImageLoaderSignals()

    @Slot()
    def run(self) -> None:
        self.signals.loading.emit(True)
        image_path = get_item_from_cache(self.url)

        match image_path:
            case None:
                try:
                    response = requests.get(self.url)

                    if response.status_code == 200:
                        image = response.content
                        cache[self.url] = save_bytes_as_img(
                            self.url.split("/")[-1],
                            image,
                        )
                        self.signals.success.emit(image)

                except Exception as e:
                    self.signals.loading.emit(False)
                    self.signals.failure.emit(str(e))
            case _:
                image = load_image_as_byte(image_path)
                self.signals.success.emit(image)

        self.signals.loading.emit(False)
