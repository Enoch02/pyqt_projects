import os.path
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import (
    QWidget,
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QScrollArea,
)
from PySide6.QtWidgets import QMainWindow
from main_window import Ui_MainWindow
from note_model import NoteModel

basedir = os.path.dirname(__file__)


class StickyNotesWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = NoteModel()
        self.get_notes()

        self.notesListView.setModel(self.model)

    def get_notes(self):
        path = os.path.join(basedir, "notes")

        # TODO: replace with db
        """if os.path.exists(path):
            self.notes = os.listdir()"""
        self.model.notes.extend(["hello", "world"])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StickyNotesWindow()
    window.show()

    app.exec()
