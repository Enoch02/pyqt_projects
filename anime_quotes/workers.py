import requests
from PySide6.QtCore import QRunnable, Slot
from signals import WorkerSignals


class RandomQuoteWorker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()

    @Slot()
    def run(self) -> None:
        try:
            response = requests.get("https://animechan.vercel.app/api/random")

            if response.status_code == 200:
                data = response.json()
                self.signals.success.emit(data)

        except Exception as e:
            self.signals.failure.emit(str(e))
