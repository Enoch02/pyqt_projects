import sys

from PySide6.QtCore import QThreadPool
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QMessageBox,
    QProgressBar,
)

from workers import ImageGalleryWorker, ImageLoaderWorker


class MainWindow(QWidget):
    count_label: QLabel
    image_label: QLabel
    previous_btn: QPushButton
    next_btn: QPushButton
    progress_bar: QProgressBar

    def __init__(self):
        super().__init__()
        self.images: list[dict[str, str]] = []
        self.current_image_index = -1
        self.threadpool = QThreadPool()

        self.load_gallery()
        self.initialize_ui()

    def initialize_ui(self):
        """Set up the application"""
        self.setWindowTitle("Nekos")
        self.setMinimumSize(800, 600)

        self.set_up_main_window()
        self.show()

    def set_up_main_window(self):
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(0)
        timer = QTimer()
        timer.setInterval(100)
        timer.timeout.connect(self.update_progress)

        self.count_label = QLabel("")
        self.image_label = QLabel()

        self.previous_btn = QPushButton()
        self.previous_btn.setText("Previous Image")
        self.previous_btn.clicked.connect(self.get_previous_image)

        self.next_btn = QPushButton()
        self.next_btn.setText("Next Image")
        self.next_btn.clicked.connect(self.get_next_image)

        h_button_layout = QHBoxLayout()
        h_button_layout.addWidget(self.previous_btn)
        h_button_layout.addWidget(self.next_btn)
        button_layout_container = QWidget()
        button_layout_container.setLayout(h_button_layout)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.count_label)
        v_layout.addWidget(self.image_label)
        v_layout.addStretch()
        v_layout.addWidget(self.progress_bar)
        v_layout.addWidget(button_layout_container)

        self.setLayout(v_layout)

    def load_gallery(self):
        if self.current_image_index == -1:
            worker = ImageGalleryWorker()
            worker.signals.success.connect(self.update_gallery)
            worker.signals.failure.connect(self.show_gallery_error_msg_box)

            self.threadpool.start(worker)

    def update_gallery(self, gallery: list[dict[str, str]]):
        self.images = self.images + gallery
        self.get_next_image()

    def load_image(self, url: str):
        worker = ImageLoaderWorker(url)
        worker.signals.success.connect(self.update_labels)
        worker.signals.loading.connect(self.show_progress)
        worker.signals.failure.connect(self.show_gallery_error_msg_box)

        self.threadpool.start(worker)

    def get_next_image(self):
        if not (self.current_image_index > len(self.images) - 1):
            image = self.images[self.current_image_index]

            self.current_image_index += 1
            self.image_label.clear()
            self.load_image(image["url"])
            self.image_label.update()
        else:
            self.current_image_index = 0

    def get_previous_image(self):
        if self.current_image_index != 0:
            self.current_image_index -= 1
        else:
            self.current_image_index = len(self.images) - 1

        image = self.images[self.current_image_index]
        self.load_image(image["url"])

    def update_labels(self, data: bytes):
        self.count_label.setText(f"{self.current_image_index + 1}/20")

        image = QImage()
        image.loadFromData(data)
        pixmap = QPixmap.fromImage(image)
        self.image_label.setPixmap(
            pixmap.scaled(
                self.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.update()

    def show_gallery_error_msg_box(self, msg: str):
        msg = QMessageBox.warning(
            self,
            "Error",
            msg,
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Retry,
        )
        if msg == QMessageBox.StandardButton.Close:
            app.exit()
        else:
            match len(self.images):
                case 0:
                    self.load_gallery()
                case _:
                    image = self.images[self.current_image_index]
                    self.load_image(image["url"])

    def show_progress(self, show: bool):
        self.progress_bar.setVisible(show)

    def update_progress(self):
        if self.progress_bar.isVisible():
            self.progress_bar.setValue(
                (self.progress_bar.value() + 1) % self.progress_bar.maximum()
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
