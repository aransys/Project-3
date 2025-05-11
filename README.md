# Todo List Application

A full-stack web application built with Python and Django for managing tasks. This project was developed as part of the L5 Diploma in Web Application Development, Unit 3: Back End Development.

## Purpose and Features

This application provides a comprehensive task management system that allows users to:

- Create, view, update, and delete tasks (CRUD functionality)
- Mark tasks as complete/incomplete
- Organize tasks with due dates
- Add detailed descriptions to tasks
- View both a list of all tasks and individual task details

The application serves as a practical solution for personal task management, helping users keep track of their responsibilities in an organized and efficient manner.

## Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite (development), PostgreSQL (production)
- **Deployment**: Heroku
- **Version Control**: Git, GitHub

## Data Schema

The application uses a single `Task` model with the following fields:

| Field       | Type          | Description                                 |
| ----------- | ------------- | ------------------------------------------- |
| title       | CharField     | The name of the task                        |
| description | TextField     | Detailed description of the task (optional) |
| completed   | BooleanField  | Task completion status                      |
| created_at  | DateTimeField | Timestamp when task was created             |
| due_date    | DateField     | When the task is due (optional)             |

The data schema is intentionally designed to be simple yet effective, focusing on the core information needed for task management while avoiding unnecessary complexity.

## Project Structure

todo_project/
├── todo_app/ # Main application
│ ├── migrations/ # Database migrations
│ ├── templates/ # HTML templates
│ │ └── todo_app/ # Application-specific templates
│ ├── admin.py # Admin configuration
│ ├── forms.py # Form definitions
│ ├── models.py # Data models
│ ├── urls.py # URL routing
│ └── views.py # View logic
├── todo_project/ # Project configuration
│ ├── settings.py # Django settings
│ ├── urls.py # Top-level URL routing
│ └── wsgi.py # WSGI configuration
├── .gitignore # Git ignore file
├── Procfile # Heroku deployment configuration
├── README.md # This documentation
└── requirements.txt # Python dependencies

## Installation and Setup for Local Development

1. **Clone the repository**:
   git clone https://github.com/yourusername/Project-3.git
   cd Project-3

2. **Create a virtual environment**:
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate

3. **Install dependencies**:
   pip install -r requirements.txt

4. **Apply migrations**:
   python manage.py migrate

5. **Create a superuser** (for admin access):
   python manage.py createsuperuser

6. **Run the development server**:
   python manage.py runserver

7. **Access the application**:

- Todo App: http://127.0.0.1:8000/
- Admin Interface: http://127.0.0.1:8000/admin/

## Deployment Process

This application is configured for deployment on Heroku. The following steps outline the deployment process:

1. **Create a Heroku account and install the Heroku CLI**

2. **Login to Heroku**:
   heroku login

3. **Create a new Heroku app**:
   heroku create your-app-name

4. **Provision a PostgreSQL database**:
   heroku addons
   heroku-postgresql

5. **Configure environment variables**:
   heroku config
   SECRET_KEY=your_secret_key
   heroku config
   DEBUG=False

6. **Deploy the application**:
   git push heroku main

7. **Apply migrations on Heroku**:
   heroku run python manage.py migrate

8. **Create superuser on Heroku** (optional):
   heroku run python manage.py createsuperuser

## Security Features

The application implements several security measures:

1. **Secret Key Protection**: The Django secret key is stored as an environment variable, not in the codebase.

2. **Debug Mode**: Debug mode is disabled in production to prevent sensitive information leakage.

3. **Database Configuration**: Database credentials are stored securely using environment variables.

4. **Secure Form Handling**: CSRF protection is enabled for all forms to prevent cross-site request forgery attacks.

5. **Input Validation**: All user inputs are validated to prevent injection attacks.

## Testing

The application was thoroughly tested using the following methods:

1. **Functionality Testing**: All CRUD operations were tested to ensure proper functionality.

- Creating tasks with various data
- Reading task details
- Updating task information
- Deleting tasks
- Toggling task completion status

2. **Responsiveness Testing**: The application was tested on various screen sizes to ensure proper display.

3. **User Experience Testing**: Navigation flow was tested to ensure a smooth user experience.

4. **Error Handling Testing**: Various error scenarios were tested to ensure graceful error handling.

A detailed testing log is available in the `testing.md` file.

## Future Enhancements

Potential future improvements for the application include:

1. User authentication and user-specific tasks
2. Task categories or tags
3. Priority levels for tasks
4. Email reminders for upcoming due dates
5. Bulk actions (complete/delete multiple tasks)
6. Search and filter functionality

## Author

[Aurimas Ransys]

## License

This project is licensed under the MIT License - see the LICENSE file for details.
