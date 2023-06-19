import sys

from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("Calculator+")

        # Set window icon
        self.setWindowIcon(QIcon(QPixmap("calculator.png")))

        # Initialize the grid layout and set it as the widget's layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        # Create the result field, add it to the grid layout
        self.result_field = QLineEdit()
        self.grid.addWidget(self.result_field, 0, 0, 1, 4)

        # Create the buttons and add them to the grid layout
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)

        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("=", 4, 2)
        self.create_button("+", 4, 3)
        self.create_button("C", 5, 0)

        # Set focus to the result field and set the layout
        self.result_field.setFocus()
        self.setLayout(self.grid)

    def create_button(self, text, row, column):
        """Create a button with the given text, add a clicked signal and add it to the grid layout"""
        button = QPushButton(text)
        button.clicked.connect(lambda: self.button_click(text))
        self.grid.addWidget(button, row, column)

    def button_click(self, text):
        """Handle button click events"""
        if text == "=":
            self.calculate()
        elif text == "C":
            self.result_field.setText("")
        else:
            self.result_field.setText(self.result_field.text() + text)

    def calculate(self):
        """Evaluate the expression in the result field and update the result field"""
        try:
            result = eval(self.result_field.text())
            self.result_field.setText(str(result))
        except:
            self.result_field.setText("Error")


if __name__ == "__main__":
    # Create the QApplication and the Calculator widget, show it and run the app
    app = QApplication(sys.argv)

    # Set the application icon
    app.setWindowIcon(QIcon(QPixmap("calculator.png")))

    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())