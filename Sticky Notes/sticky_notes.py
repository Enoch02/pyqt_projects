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

basedir = os.path.dirname(__file__)


class StickyNotesWindow(QWidget):
    search_button: QPushButton
    search_text: QLineEdit

    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.notes: list[NoteWidget] = []

        self.init_window()
        self.setup_layout()

    def init_window(self):
        # TODO: how do i customize it
        # self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(QSize(300, 300))
        self.get_notes()

        self.setLayout(self.main_layout)

    def setup_layout(self):
        search_layout = QHBoxLayout()

        self.search_text = QLineEdit()
        self.search_text.setPlaceholderText("Search")

        search_pixmap = QPixmap(os.path.join(basedir, "icons/magnifier.png"))
        self.search_button = QPushButton()
        self.search_button.setIcon(QIcon(search_pixmap))

        search_layout.addWidget(self.search_text)
        search_layout.addWidget(self.search_button)
        self.main_layout.addLayout(search_layout)

        dummy_items = [
            "hello world",
            "something interesting",
            "cupcake",
            "banana bread",
            "another one",
            "foo",
            "bar",
            "baz",
            "more",
            "stuff",
            "fill",
            "the",
            "gaps",
        ]
        notes_preview_layout = QVBoxLayout()
        for item in dummy_items:
            preview = NotePreviewWidget(item)
            notes_preview_layout.addWidget(preview)

        scroll_area = QScrollArea()
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        container = QWidget()
        container.setLayout(notes_preview_layout)
        scroll_area.setWidget(container)

        self.main_layout.addWidget(scroll_area)

    def get_notes(self):
        path = os.path.join(basedir, "notes")

        # TODO: replace with db
        if os.path.exists(path):
            self.notes = os.listdir()


class NotePreviewWidget(QWidget):
    # TODO: might replace title
    def __init__(self, title: str):
        super().__init__()
        self.title = title
        self.main_layout = QVBoxLayout()

        self._init_widget()

    def _init_widget(self):
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.setLayout(self.main_layout)

        label = QLabel(self.title)
        label.setStyleSheet("color: blue")
        desc = QLabel(
            """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Vivamus nisl nulla, fringilla sit amet tellus id, finibus finibus augue.
            Curabitur maximus mauris at dolor bibendum, id rhoncus velit convallis."""
        )
        self.main_layout.addWidget(label)
        self.main_layout.addWidget(desc)


class NoteWidget(QWidget):
    def __init__(self, note_file_path: str):
        super().__init__()
        ...


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StickyNotesWindow()
    window.show()

    app.exec()
