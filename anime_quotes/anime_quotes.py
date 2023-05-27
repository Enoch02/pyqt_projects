import sys

from PySide6.QtWidgets import QMainWindow, QApplication
from anime_quotes_ui import Ui_MainWindow
from workers import RandomQuoteWorker


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.getting_random_quotes = False

        self.setupUi(self)
        self.setWindowTitle("Anime Quotes")
        self.setFixedSize(400, 200)
        self.setup_quote_view()

        self.show()

    def setup_quote_view(self):
        self.quoteLabel.setText("")
        self.characterAnimeLabel.setText("")

        self.getQuoteButton.clicked.connect(self.get_random_quote)

    def get_random_quote(self):
        if not self.getting_random_quotes:
            self.getting_random_quotes = True
            worker = RandomQuoteWorker()
            worker.signals.success.connect(self.update_quote_view)
            worker.run()

    def update_quote_view(self, new_quote: dict):
        self.quoteLabel.setText(f"\"{new_quote['quote']}\"")
        self.characterAnimeLabel.setText(
            f"-{new_quote['character']} [{new_quote['anime']}]"
        )
        self.getting_random_quotes = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
