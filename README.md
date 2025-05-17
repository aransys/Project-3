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

## Project Rationale

### Target Audience

This task management application addresses the needs of:

- **Students**: Managing coursework deadlines and assignments
- **Professionals**: Tracking daily tasks and project milestones
- **General Users**: Organizing personal responsibilities

### Problem Statement

Many existing task management solutions are overly complex for simple personal use. This application provides:

- Straightforward CRUD operations without unnecessary features
- Clean, distraction-free interface
- Essential fields only (title, description, due date, completion status)

### Design Decisions

- **Bootstrap 5**: Ensures responsive design across all devices
- **Django Framework**: Provides robust backend with built-in security
- **Minimal UI**: Reduces cognitive load and improves user focus
- **Single Task Model**: Simplifies data management while meeting core needs

## Data Schema

### Task Model Structure

| Field       | Type          | Constraints                     | Default | Description          |
| ----------- | ------------- | ------------------------------- | ------- | -------------------- |
| id          | AutoField     | Primary Key                     | Auto    | Unique identifier    |
| title       | CharField     | max_length=200, NOT NULL        | -       | Task title/name      |
| description | TextField     | Optional, blank=True            | ''      | Detailed description |
| completed   | BooleanField  | -                               | False   | Completion status    |
| created_at  | DateTimeField | auto_now_add=True               | Now     | Creation timestamp   |
| due_date    | DateField     | Optional, blank=True, null=True | None    | Due date             |

### Database Design Decisions

- **Simple flat structure**: Chosen for clarity and assignment scope
- **No user relationships**: Application designed for single-user usage
- **Optional fields**: Description and due_date allow flexible task creation
- **Automatic timestamps**: created_at auto-populated for audit trail

## Template Implementation

### Template Structure

templates/
└── todo_app/
├── base.html # Base template with common elements
├── task_list.html # Homepage showing all tasks
├── task_detail.html # Individual task view
├── task_form.html # Create/Edit task form
└── task_confirm_delete.html # Deletion confirmation

### Key Template Features

1. **Template Inheritance**

   ```django
   {% extends 'todo_app/base.html' %}
   {% block content %}...{% endblock %}

   ```

2. **Template Logic**

   ```django
   {% for task in tasks %}
   {% if task.completed %}
   <span class="badge bg-success">Completed</span>
   {% else %}
   <span class="badge bg-warning">Pending</span>
   {% endif %}
   {% empty %}
   <p>No tasks available.</p>
   {% endfor %}

   ```

3. **URL Reversing**

   ```django
   <a href="{% url 'task_detail' task.pk %}">View Task</a>

   ```

4. **Form Rendering**

   ```django
   <form method="post">
   {% csrf_token %}
   {{ form.as_p }}
   < button type="submit" class="btn btn-primary">Save</>
   </form>

   ```

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
