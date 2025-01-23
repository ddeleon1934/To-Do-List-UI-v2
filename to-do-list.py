import sys
import json
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QPushButton,
    QListWidget, QLineEdit, QWidget, QMessageBox, QLabel
)

# Global list to store tasks
tasks = []

class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List App")
        self.setGeometry(200, 200, 400, 300)

        # Main widget and layout
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)

        # Header label to display the title of the app
        self.header_label = QLabel("To-Do List", self)
        self.header_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(self.header_label)

        # List widget to display tasks
        self.task_list_widget = QListWidget(self)
        self.layout.addWidget(self.task_list_widget)

        # Input field for adding tasks
        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Enter a new task")
        self.layout.addWidget(self.task_input)

        # Buttons
        # Button to add a new task
        self.add_task_button = QPushButton("Add Task", self)
        self.add_task_button.clicked.connect(self.addTask)
        self.layout.addWidget(self.add_task_button)

        # Button to delete the selected task
        self.delete_task_button = QPushButton("Delete Selected Task", self)
        self.delete_task_button.clicked.connect(self.deleteTask)
        self.layout.addWidget(self.delete_task_button)

        # Load tasks from file when the app starts
        self.loadTasks()

    # Method to add a new task
    def addTask(self):
        task = self.task_input.text().strip()
        if task: # If the input is not empty
            tasks.append(task)
            self.task_list_widget.addItem(task)
            self.task_input.clear()
            self.saveTasks()
        else:
            QMessageBox.warning(self, "Input Error", "Please enter a valid task.")

    # Method to delete a selected task
    def deleteTask(self):
        selected_task = self.task_list_widget.currentRow()
        if selected_task >= 0:
            task = tasks.pop(selected_task)
            self.task_list_widget.takeItem(selected_task)
            self.saveTasks()
        else:
            QMessageBox.warning(self, "Selection Error", "Please select a task to delete.")

    # Method to save tasks to a JSON file
    def saveTasks(self):
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)

    # Method to load tasks from a JSON file
    def loadTasks(self):
        global tasks
        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
                self.task_list_widget.addItems(tasks)
        except FileNotFoundError:
            tasks = []

# Main execution point of the app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
