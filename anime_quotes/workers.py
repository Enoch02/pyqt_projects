import requests
from PySide6.QtCore import QRunnable, Slot
from signals import WorkerSignals


class RandomQuoteWorker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()

    @Slot()
    def run(self) -> None:
        response = requests.get("https://animechan.vercel.app/api/random")

        if response.status_code == 200:
            data = response.json()
            self.signals.success.emit(data)
