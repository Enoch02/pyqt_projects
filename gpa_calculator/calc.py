import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QFormLayout,
    QLineEdit,
    QComboBox,
    QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.courses: list[QHBoxLayout] = []
        self.current_index = 0

        self.setWindowTitle("Gpa Calculator")
        self.setFixedSize(400, 600)
        self.setup_ui()
        self.spawn_course_entry()

    def setup_ui(self):
        labels_h_box = QHBoxLayout()
        course_label = QLabel("Course")
        course_label.setFixedWidth(250)
        credits_label = QLabel("Credit")

        labels_h_box.addWidget(course_label)
        labels_h_box.addWidget(credits_label)

        self.courses_form = QFormLayout()
        self.courses_form.setFieldGrowthPolicy(
            QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow
        )
        self.courses_form.addRow(labels_h_box)

        add_course_btn = QPushButton("Add Course")
        add_course_btn.clicked.connect(self.spawn_course_entry)

        calculate_btn = QPushButton("Calculate")

        actions_h_box = QHBoxLayout()
        actions_h_box.setAlignment(Qt.AlignmentFlag.AlignBottom)
        actions_h_box.addWidget(add_course_btn)
        actions_h_box.addWidget(calculate_btn)

        main_v_box = QVBoxLayout()
        # main_v_box.addLayout(labels_h_box)
        main_v_box.addLayout(self.courses_form)
        main_v_box.addLayout(actions_h_box)

        main_layout_container = QWidget()
        main_layout_container.setLayout(main_v_box)

        self.setCentralWidget(main_layout_container)

    def spawn_course_entry(self):
        course_title_edit = QLineEdit()
        course_title_edit.setFixedWidth(250)

        course_unit_edit = QLineEdit()
        course_grade_combo = QComboBox()
        course_grade_combo.addItems(["A", "B", "C", "D", "E", "F"])

        course_remove_btn = QPushButton()
        # TODO: use path relative to python script
        course_remove_btn.setIcon(QIcon("./cross.png"))

        course_h_box = QHBoxLayout()
        course_h_box.addWidget(course_title_edit)
        course_h_box.addWidget(course_unit_edit)
        course_h_box.addWidget(course_grade_combo)
        course_h_box.addWidget(course_remove_btn)

        course_remove_btn.clicked.connect(
            lambda: self.delete_course(self.current_index)
        )
        self.courses.append(course_h_box)

        self.current_index += 1

        self.courses_form.addRow(course_h_box)

    def delete_course(self, index: int):
        print(index)
        self.courses[index].deleteLater()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
