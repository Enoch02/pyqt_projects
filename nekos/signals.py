from PySide6.QtCore import QObject, Signal


class NekoSignals(QObject):
    failure = Signal(str)


class GalleryWorkerSignals(NekoSignals):
    success = Signal(list)


class ImageLoaderSignals(NekoSignals):
    loading = Signal(bool)
    success = Signal(bytes)
