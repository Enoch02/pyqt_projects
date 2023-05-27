from PySide6.QtCore import QObject, Signal


class WorkerSignals(QObject):
    success = Signal(dict)
    failure = Signal(str)
