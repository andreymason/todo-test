# Django ToDo List App

This is a Django-based ToDo list app that allows you to manage tasks with various features such as task creation, editing, deletion, and marking tasks as completed. It also provides a REST API to interact with the app.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/andreymason/todo-test.git

2. Navigate to the project directory:
   ```bash
   cd todo

3. Set up a virtual environment (recommended) and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate

4. Install the project dependencies:
   ```bash
   pip install -r requirements.txt
5. Apply database migrations:
   ```bash
   python manage.py migrate
6. Start the development server:
   ```bash
   python manage.py runserver
7. Access the application in your web browser at http://localhost:8000.

### Usage
## API Endpoints
The app provides the following API endpoints:

GET /tasks/: Retrieve a list of tasks.

POST /tasks/: Create a new task.

GET /tasks/{task_id}/: Retrieve details of a specific task.

PUT /tasks/{task_id}/: Update a task.

PATCH /tasks/{task_id}/mark_as_done/: Mark a task as completed.

DELETE /tasks/{task_id}/: Delete a task.

You can use the API endpoints to interact with the app programmatically.

## Web Interface
The app also provides a web interface to manage tasks. To access it, follow these steps:

Open your web browser.

Navigate to http://localhost:8000/tasks/ to view the list of tasks.

Use the provided features to create, edit, delete, and mark tasks as completed.

Filtering and Sorting

The API endpoints and web interface support various filtering and sorting options:

GET /tasks/?status=done: Filter tasks by status (done or todo).

GET /tasks/?priority=3: Filter tasks by priority (1-5).

GET /tasks/?title=search: Filter tasks by title (full-text search).

GET /tasks/?sort_by=creation_time: Sort tasks by creation time.

GET /tasks/?sort_by=priority: Sort tasks by priority.

Feel free to customize the filtering and sorting options as per your requirements.

## Authentication and Permissions
To restrict access and manage permissions, you can implement authentication and authorization mechanisms in your Django project. This README assumes an open and public access setup, but it's highly recommended to secure the app based on your deployment requirements.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please create a new issue or submit a pull request.



