# This Python file uses the following encoding: utf-8
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QMessageBox,
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QPixmap, QImage
import requests


# TODO: make it more "responsive" and efficient
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.images = []
        self.current_image_index = -1
        self.worker = Worker()
        self.worker.load_fail_signal.connect(self.loadFailMsgBox)
        self.worker.load_complete_signal.connect(self.loadImages)

        self.initializeUI()

    def initializeUI(self):
        """Set up the application"""
        self.setWindowTitle("QT Nekos")
        self.setMinimumSize(800, 600)

        self.setUpMainWindow()
        self.worker.start()
        self.show()

    def setUpMainWindow(self):
        self.image_label = QLabel()

        self.previous_btn = QPushButton()
        self.previous_btn.setText("Previous Image")
        self.previous_btn.clicked.connect(self.getPreviousImage)

        self.next_btn = QPushButton()
        self.next_btn.setText("Next Image")
        self.next_btn.clicked.connect(self.getNextImage)

        h_button_layout = QHBoxLayout()
        h_button_layout.addWidget(self.previous_btn)
        h_button_layout.addWidget(self.next_btn)
        button_layout_container = QWidget()
        button_layout_container.setLayout(h_button_layout)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.image_label)
        v_layout.addStretch()
        v_layout.addWidget(button_layout_container)

        self.setLayout(v_layout)

    def getNextImage(self):
        if not (self.current_image_index > len(self.images) - 1):
            self.current_image_index += 1
            self.image_label.clear()
            self.image_label.update()
            self.loadNewImages()
        else:
            self.current_image_index = 0

    def getPreviousImage(self):
        if self.current_image_index != 0:
            self.current_image_index -= 1
            self.loadNewImages()
        else:
            self.current_image_index = len(self.images) - 1

    def loadNewImages(self):
        loader = ImageLoader(self.images[self.current_image_index]["url"])
        loader.image_loading_complete_signal.connect(self.updateImageLabel)
        loader.run()

    def loadImages(self, images):
        self.images = images
        self.current_image_index = 0

        loader = ImageLoader(self.images[self.current_image_index]["url"])
        loader.image_loading_complete_signal.connect(self.updateImageLabel)
        loader.run()

    def updateImageLabel(self, data):
        image = QImage()
        image.loadFromData(data)
        pixmap = QPixmap.fromImage(image)  # TODO: will it load faster it the pixmap variable already exists...
        self.image_label.setPixmap(
            pixmap.scaled(
                self.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.update()

    def loadFailMsgBox(self):
        msg = QMessageBox.warning(
            self,
            "Error",
            "Could not load nekos",
            QMessageBox.StandardButton.Ok,
            QMessageBox.StandardButton.Ok,
        )
        if msg == QMessageBox.StandardButton.Ok:
            exit(1)


class Worker(QThread):
    load_complete_signal = pyqtSignal(list)
    load_fail_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

    def stopRunning(self) -> None:
        self.terminate()
        self.wait()

        self.load_complete_signal.emit([])

    def run(self) -> None:
        try:
            response = requests.get("https://nekos.best/api/v2/neko?amount=20")
            images = response.json()["results"]
            self.load_complete_signal.emit(images)
        except Exception:
            self.load_fail_signal.emit()


class ImageLoader(QThread):
    image_loading_complete_signal = pyqtSignal(bytes)
    image_loading_fail_signal = pyqtSignal()

    def __init__(self, url):
        super().__init__()
        self.url = url

    def stopRunning(self) -> None:
        self.terminate()
        self.wait()

    def run(self) -> None:
        content = requests.get(self.url).content
        self.image_loading_complete_signal.emit(content)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
