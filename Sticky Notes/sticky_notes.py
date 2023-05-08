import os.path
import sys

from PyQt6.QtWidgets import QWidget, QApplication

basedir = os.path.dirname(__file__)


class StickyNotesWindow(QWidget):
    def __init__(self):
        super().__init__()

    def init_window(self):
        ...

    def setup_top_bar(self):
        ...

    def get_notes(self):
        ...


class NoteWidget(QWidget):
    def __init__(self, note_file):
        super().__init__()
        self.content: str = ""

    def set_up_widget(self):
        ...


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StickyNotesWindow()
    window.show()

    app.exec()
