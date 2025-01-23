# To-Do List App
A simple, lightweight To-Do List application built using **PyQt5** for the graphical user interface (GUI) and **JSON** for task storage. This app allows users to add and delete tasks, with persistent task storage in a local JSON file.

## Features
- **Add Tasks**: Users can add new tasks to their to-do list via a text input field.
- **Delete Tasks**: Users can select tasks from the list and delete them.
- **Persistent Storage**: Tasks are saved in a `tasks.json` file, ensuring that tasks persist even when the application is closed and reopened.
- **User Interface**: A simple, intuitive GUI built with PyQt5 that displays tasks in a list, provides input for adding new tasks, and includes buttons for adding and deleting tasks.

## Requirements
- Python 3.x
- PyQt5 (can be installed via pip)

To install the required libraries, run:

pip install pyqt5

## How to Run
1. Clone the repository or download the script.
2. Ensure Python 3.x is installed on your system.
3. Run the Python script:

python todo_app.py

This will launch the **To-Do List** application.

## Functionality

### Add Task
- Enter a task in the input field and press the **Add Task** button.
- The task will be added to the list and saved to the `tasks.json` file.

### Delete Task
- Select a task from the list.
- Press the **Delete Selected Task** button to remove the selected task.
- The task will be removed from both the list and the `tasks.json` file.

## Data Persistence
- **Tasks** are saved to and loaded from a file named `tasks.json`. If the file does not exist, the app will create it automatically.
- Tasks will persist across app restarts, allowing users to pick up where they left off.

## Screenshots
![image](https://github.com/user-attachments/assets/99609785-cd30-498d-a454-66a7b8532494)

## Credits
## Current Enhancements
## Future Enhancements

