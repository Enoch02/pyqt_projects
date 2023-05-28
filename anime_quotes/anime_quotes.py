import sys

from PySide6.QtCore import QThreadPool
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QLabel
from anime_quotes_ui import Ui_MainWindow
from workers import RandomQuoteWorker
from stylesheet import STYLESHEET


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.getting_random_quotes = False
        self.threadpool = QThreadPool()

        self.setupUi(self)
        self.setWindowTitle("Anime Quotes")
        self.setFixedSize(800, 400)
        self.setup_window()
        self.show()

        # get random quote on first launch
        self.get_random_quote()

    def setup_window(self):
        self.quoteLabel.setText("")
        self.characterAnimeLabel.setText("")
        self.getQuoteButton.clicked.connect(self.get_random_quote)

        self.actionAbout.triggered.connect(self.show_about_dialog)

    def get_random_quote(self):
        if not self.getting_random_quotes:
            self.getting_random_quotes = True
            self.statusbar.showMessage("Loading...")

            worker = RandomQuoteWorker()
            worker.signals.success.connect(self.update_quote_view)
            worker.signals.failure.connect(self.show_error_dialog)

            self.threadpool.start(worker)

    def update_quote_view(self, new_quote: dict):
        self.quoteLabel.setText(f"\"{new_quote['quote']}\"")
        self.characterAnimeLabel.setText(
            f"{new_quote['character']} [{new_quote['anime']}]"
        )
        self.cleanup()

    def cleanup(self):
        self.getting_random_quotes = False
        self.statusbar.showMessage("")

    def show_error_dialog(self, message: str):
        self.cleanup()
        self.statusbar.showMessage("Error!")
        msg_box = QMessageBox.warning(
            self,
            "Error",
            message,
            QMessageBox.StandardButton.Retry,
        )

        if msg_box == QMessageBox.StandardButton.Retry:
            self.get_random_quote()

    def show_about_dialog(self):
        message = QLabel()

        QMessageBox.information(
            self,
            "About",
            """
            This program uses <a href="https://animechan.vercel.app">this API</a> to display quotes from
            anime. More features will be added.. eventually
            """,
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(STYLESHEET)
    window = MainWindow()
    app.exec()
