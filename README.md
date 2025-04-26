# CLI Todo List Tracker App

A simple command-line todo list tracker to log and manage tasks. The data is persisted in a JSON file

## Features

### Core Features

- **Add new task**
- **View all tasks**
- **View completed tasks** 
- **View pending tasks**
- **Update task**
- **Delete task**

### CLI Usability Features

- **Intuitive Commands** – Simple and clear commands like `Add a new task`, `View all tasks`, `View completed tasks`, ... `Exit`.
- **Data Persistence** – Store data in a JSON file to ensure it remains available between sessions.
- **Error Handling** – Gracefully handle invalid inputs.

## Usage

### Adding a Task

```sh
python main.py
```

Type 1 and Follow the prompt to make a choice

### Viewing Tasks

```sh
python main.py
```

Type 2 and Follow the prompt to make a choice

### To Exot

```sh
python main.py
```

Type 0

## Data Storage

- All transactions are stored in a CSV file (`tasks.json`).
- The file is automatically updated when a transaction is added.

## Future Improvements

🔹 Add due dates for tasks
🔹 Filter tasks by date range.
🔹 Sort tasks by due date for completed vs. pending
🔹 Use SQLite instead of JSON for storage
🔹 Add priority levels (High, Medium, Low)

## License

This project is licensed under the MIT License.
