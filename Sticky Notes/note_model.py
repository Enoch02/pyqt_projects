from typing import Any, Union

from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt, QPersistentModelIndex


class NoteModel(QAbstractListModel):
    def __init__(self, notes=None):
        super().__init__()
        self.notes = notes or []

    def data(self, index: QModelIndex, role: int = ...) -> Any:
        if role == Qt.ItemDataRole.DisplayRole:
            # title, content = self.notes[index.row()]
            title = self.notes[index.row()]
            return title

        if role == Qt.ItemDataRole.DecorationRole:
            ...  # todo

    def rowCount(self, parent: Union[QModelIndex, QPersistentModelIndex] = ...) -> int:
        return len(self.notes)
