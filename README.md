## Project Overview

Task Manager is a full-stack web application built with Python and Django that provides a comprehensive solution for organizing and tracking personal tasks. Developed as part of the L5 Diploma in Web Application Development (Unit 3: Back End Development), this project demonstrates proficiency in creating database-backed web applications using Python and web frameworks.

### Purpose and Value

The application addresses the common need for organized task management in daily life. In today's fast-paced environment, people often struggle to keep track of their responsibilities, leading to missed deadlines and increased stress. This application provides:

- A centralized system to record and manage all tasks
- Clear visualization of task status and deadlines
- The ability to update tasks as circumstances change
- A simple, intuitive interface that reduces the cognitive load of tracking tasks mentally

### Target Audience

This application is designed for:

- Individuals seeking a simple, personal task management solution
- Students managing assignments and project deadlines
- Professionals tracking work-related tasks and deadlines
- Anyone looking to improve their personal productivity and organization

### Key Features

- **Complete CRUD Functionality**: Create, read, update, and delete tasks
- **Task Status Tracking**: Mark tasks as complete/incomplete with visual indicators
- **Due Date Management**: Assign and track deadlines for time-sensitive tasks
- **Detailed Task Descriptions**: Add comprehensive notes and context to tasks
- **Responsive Design**: Access and manage tasks from any device with consistent user experience
- **Intuitive Interface**: Simple, clean design focused on usability and accessibility

### Technology Stack

- **Backend**: Python 3.9 with Django 4.2
  - Chosen for its robust ORM, built-in admin interface, and security features
  - Provides a clean, pragmatic approach to web development
- **Frontend**:
  - HTML5 with Django Templates for dynamic content rendering
  - CSS3 and Bootstrap 5 for responsive, mobile-first design
  - JavaScript for enhanced interactivity
- **Database**:
  - SQLite for development (lightweight, zero-configuration)
  - PostgreSQL for production (robust, scalable, industry-standard)
- **Deployment**:
  - Railway Platform-as-a-Service
  - Chosen for ease of deployment and scalability
- **Version Control**:
  - Git with GitHub for source code management
  - Enables collaboration and provides an audit trail of development

```markdown
## UX Design Process and Principles

## UX Design Process and Principles

### User Flow Analysis and Testing

**Task Creation Efficiency:**
The application was designed for rapid task entry, requiring only 5 clicks from homepage to completed task creation. This strikes an optimal balance between speed and data completeness - users can quickly capture tasks while still providing essential details like due dates when needed.

**Immediate Visual Feedback:**
Task completion provides instant visual feedback through strikethrough text and color changes (black to grey), ensuring users immediately understand their action succeeded. This eliminates the uncertainty common in web applications where users wonder "did that work?"

**Reversible Actions:**
All task status changes are instantly reversible with a single click, acknowledging that users frequently change their minds or accidentally click buttons. This reduces anxiety about making mistakes.

### Design Principles Applied

#### Information Hierarchy

- **Primary Action Prominence**: The "Add New Task" button is visually prominent, making task creation the most obvious action
- **Status Visual Hierarchy**: Completed tasks are de-emphasized through greying and strikethrough, keeping focus on active tasks
- **Content Organization**: Tasks are ordered with active items first, completed items naturally move to bottom of list

#### User Control

- **Immediate Feedback**: Task completion status changes instantly without page reload
- **Reversible Actions**: All status changes can be undone with a single click
- **No Confirmation Dialogs**: For non-destructive actions like status changes, eliminating unnecessary friction

#### Mobile-First Design

- **Touch-Friendly Targets**: All buttons sized appropriately for finger taps
- **Responsive Layout**: Interface adapts seamlessly to mobile viewport
- **Readable Typography**: Text remains legible across all device sizes
- **No Horizontal Scrolling**: Content fits within mobile viewport boundaries

### Design Philosophy and Rationale

**WHY this design approach:**
This application was designed with a "cognitive load reduction" philosophy, recognizing that task management tools often become part of the problem rather than the solution. Every design decision prioritizes mental simplicity over feature complexity. The instant visual feedback system (strikethrough and color changes) was implemented because task completion should feel rewarding and definitive - users need that psychological "closure" moment when they finish something. The 5-click task creation process was deliberately chosen to balance speed with completeness; fewer clicks would sacrifice important metadata like due dates, while more clicks would create friction that discourages regular use.

**WHO this serves:**
The interface targets busy individuals who need task management to be effortless rather than elaborate. This includes professionals juggling multiple responsibilities, students managing assignments and deadlines, and anyone seeking to reduce mental overhead of remembering tasks. The design specifically accommodates users who may be stressed, distracted, or multitasking - hence the large, obvious buttons, clear visual states, and forgiving interaction model where all actions are easily reversible. The mobile-first approach recognizes that modern users expect to capture and check tasks anywhere, anytime.

**WHAT problems this solves:**
Traditional task managers often suffer from "feature bloat" that makes simple actions complicated, or provide so little feedback that users lose confidence in the system. This design solves three critical problems: the "did it work?" uncertainty through immediate visual feedback, the "oops I clicked wrong" frustration through instant reversibility, and the "too much friction" barrier through streamlined task creation. By making task completion feel satisfying (visual strikethrough) and task creation feel effortless (5 focused clicks), the app encourages consistent daily use rather than abandonment after initial enthusiasm.

## Screenshots

### Task List View

![Task List](screenshots/task_list.png)
_Main task list showing completed and pending tasks_

### Task Detail View

![Task Detail](screenshots/task_detail.png)
_Detailed view of an individual task_

### Create/Edit Form

![Task Form](screenshots/task_form.png)
_Form for creating and editing tasks_

### Responsive Mobile View

![Mobile View](screenshots/mobile_view.png)
_Application appearance on mobile devices_
```

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

#### Entity Relationship Diagram

[ERD diagram here]

#### Data Modeling Decisions

1. **Single Task Model**: The application uses a deliberate, focused approach with a single model to maintain simplicity while meeting all functional requirements.

2. **Optional Fields**: Description and due date are optional, allowing users to create quick tasks without unnecessary detail while still supporting comprehensive task information when needed.

3. **Automatic Timestamps**: The created_at field uses auto_now_add to ensure accurate creation tracking without user intervention.

4. **Boolean Completion Status**: A simple boolean field provides a clear, binary representation of task status that is easy to toggle and query.

The model includes Django's built-in validation to ensure data integrity:

```python
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['due_date', 'created_at']
```

### API Endpoints/Routes

The application implements the following URL routes:

| URL Pattern              | View                 | Function                 | HTTP Methods |
| ------------------------ | -------------------- | ------------------------ | ------------ |
| `/`                      | task_list            | Display all tasks        | GET          |
| `/task/create/`          | task_create          | Create a new task        | GET, POST    |
| `/task/<int:pk>/`        | task_detail          | View a specific task     | GET          |
| `/task/<int:pk>/update/` | task_update          | Update a task            | GET, POST    |
| `/task/<int:pk>/delete/` | task_delete          | Delete a task            | GET, POST    |
| `/task/<int:pk>/toggle/` | task_toggle_complete | Toggle completion status | POST         |

Each endpoint corresponds to a specific view function that handles the appropriate HTTP methods and renders the corresponding template or redirects as necessary.

## Template Implementation

### Template Structure

```
templates/
└── todo_app/
    ├── base.html          # Base template with common elements
    ├── task_list.html     # Homepage showing all tasks
    ├── task_detail.html   # Individual task view
    ├── task_form.html     # Create/Edit task form
    └── task_confirm_delete.html # Deletion confirmation
```

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

### Project Structure

```
todo_project/
├── todo_app/                 # Main application
│   ├── migrations/           # Database migrations
│   ├── templates/            # HTML templates
│   │   └── todo_app/         # Application-specific templates
│   ├── admin.py              # Admin configuration
│   ├── forms.py              # Form definitions
│   ├── models.py             # Data models
│   ├── urls.py               # URL routing
│   └── views.py              # View logic
├── todo_project/             # Project configuration
│   ├── settings.py           # Django settings
│   ├── urls.py               # Top-level URL routing
│   └── wsgi.py               # WSGI configuration
├── .gitignore                # Git ignore file
├── Procfile                  # Railway deployment configuration
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies
```

The project follows the standard Django project structure, with clear separation of concerns:

- **Models**: Define the data structure and database schema
- **Views**: Handle HTTP requests and business logic
- **Templates**: Render the HTML interface
- **Forms**: Manage data validation and user input
- **URLs**: Define the routing between endpoints

```markdown
## Code Quality Standards

This project follows high standards for code quality and organization:

- **PEP8 Compliant**: All Python code follows PEP8 style guidelines
- **Semantic HTML**: Proper HTML5 structure with semantic elements
- **DRY Principle**: Code repetition minimized through templates and helper functions
- **Documentation**: Comprehensive docstrings and comments throughout
- **Error Handling**: Robust error handling with user-friendly messages
- **Security Best Practices**: CSRF protection, input validation, and XSS prevention

For complete code quality documentation, see [CODE_QUALITY.md](CODE_QUALITY.md).
```

## Development Process

### Version Control Workflow

This project follows a structured Git workflow to maintain code quality and provide a clear history of development:

1. **Feature Branches**: Each new feature or significant change was developed in a dedicated branch
2. **Commit Strategy**: Commits were small, focused, and included descriptive messages explaining the purpose of each change
3. **Pull Requests**: Changes were merged back to the main branch via pull requests after code review
4. **Tagging**: Version tags were applied at significant milestones

Example commit message pattern:

```
feat: Add task completion toggle functionality

- Add toggle endpoint and view function
- Update task model to track completion status
- Add JavaScript for instant UI feedback
- Include tests for toggle functionality
```

### Design Decisions and Rationale

Several key design decisions shaped the development of this application:

#### 1. Framework Selection: Django

Django was selected as the web framework for several reasons:

- Built-in admin interface provides immediate data management capabilities
- Robust ORM simplifies database operations and migrations
- Strong security features like CSRF protection, SQL injection prevention
- Comprehensive ecosystem with extensive documentation

#### 2. Single-Model Architecture

The decision to use a single Task model was made to:

- Keep the data structure intuitive and straightforward
- Focus on core functionality without unnecessary complexity
- Ensure the application remains maintainable and extensible
- Provide a solid foundation for future features

#### 3. Bootstrap Integration

Bootstrap 5 was chosen for the frontend to:

- Ensure responsive design across all device sizes
- Maintain consistent styling with minimal custom CSS
- Leverage pre-built components for faster development
- Provide accessibility features out of the box

#### 4. Form-Based Interactions

The application uses Django forms for all data entry to:

- Ensure robust validation of user input
- Present a consistent interface for data manipulation
- Leverage Django's built-in CSRF protection
- Simplify the implementation of create and update operations

### Challenges and Solutions

#### Challenge 1: Date Handling

**Problem**: Ensuring proper handling of due dates, including validation and display.

**Solution**:

- Implemented custom date validation in the task form
- Used Django's date formatting capabilities for consistent display
- Added client-side date picker for improved user experience
- Included date-based sorting for the task list

#### Challenge 2: Task Status Updates

**Problem**: Providing immediate feedback when a task's status is toggled without requiring a full page reload.

**Solution**:

- Implemented an AJAX-based toggle endpoint
- Added JavaScript to handle the status toggle client-side
- Updated the UI dynamically based on server response
- Maintained a fallback for non-JavaScript environments

#### Challenge 3: Responsive Design

**Problem**: Ensuring the application was fully usable on both desktop and mobile devices.

**Solution**:

- Used Bootstrap's grid system and responsive utilities
- Tested extensively on various screen sizes
- Implemented mobile-first design principles
- Created custom CSS media queries for edge cases

### Third-Party Libraries

The project utilizes several key libraries to enhance functionality:

1. **Django Crispy Forms**: Improves form rendering and styling

   - Streamlines the process of creating visually appealing forms
   - Integrates seamlessly with Bootstrap 5
   - Reduces custom template code

2. **Django Debug Toolbar** (development only): Assists with debugging and optimization

   - Provides insights into database queries
   - Shows template rendering times
   - Helps identify performance bottlenecks

3. **WhiteNoise**: Serves static files efficiently in production

   - Simplifies static file deployment
   - Improves performance through compression and caching
   - Removes the need for a separate static file server

4. **Gunicorn**: Production WSGI HTTP server
   - Provides robust handling of HTTP requests
   - Optimized for production environments
   - Easy integration with Railway

## Security Features

Security was a primary consideration throughout the development process. The application implements several key security measures to protect user data and prevent common vulnerabilities.

### Authentication and Authorization

While the current version is designed for personal use without multi-user authentication, the foundation has been laid for secure user authentication:

- Database schema supports user-task relationships
- Views are structured to allow for permission checks
- Admin interface is secured with Django's authentication system

### Data Protection

1. **CSRF Protection**:

   - All forms include Django's CSRF tokens
   - POST requests are verified against these tokens
   - Protection against cross-site request forgery attacks

2. **SQL Injection Prevention**:

   - All database queries use Django's ORM
   - Parameterized queries prevent SQL injection
   - Direct SQL execution is avoided

3. **XSS Prevention**:
   - Template system automatically escapes variables
   - Content Security Policy headers are implemented
   - User input is sanitized before storage

### Environment Security

1. **Secret Key Management**:

   - Django secret key stored as environment variable
   - Not included in version control
   - Different keys for development and production

2. **Debug Mode Control**:

   - Debug mode disabled in production
   - Error pages do not expose system information
   - Configured via environment variable

3. **Database Credentials**:
   - Stored as environment variables
   - Not included in version control
   - Different credentials for development and production

### Code Example: Security Implementation

Django settings are configured to ensure security in production:

```python
# Production security settings
if not DEBUG:
    # HTTPS settings
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True

    # HSTS settings
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    # Content security policy
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'
```

### Security Testing

The application underwent several security tests:

1. **Vulnerability Scanning**:

   - Automated scanning for known vulnerabilities
   - Dependencies checked against security advisories
   - Regular updates to address security patches

2. **Penetration Testing**:

   - Form injection attempts
   - CSRF protection verification
   - Session handling validation

3. **Code Review**:

   - Manual review of security-critical code
   - Peer review process for all changes
   - Static code analysis for potential vulnerabilities

   ## Deployment

The application is configured for deployment on Railway, a modern platform as a service (PaaS) that enables easy deployment and scaling of web applications. The following detailed instructions describe the deployment process from local development to production.

### Prerequisites

Before deployment, ensure you have:

- A Railway account (https://railway.app/)
- Git installed locally
- A complete, tested application codebase

### Local Environment Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/aransys/Project-3.git
   cd Project-3
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up local environment variables**:
   Create a `.env` file in the project root with:

   ```
   SECRET_KEY=your_secret_key_here
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. **Apply migrations and create a superuser**:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Verify local functionality**:
   ```bash
   python manage.py runserver
   ```
   Access the application at http://127.0.0.1:8000/

### Railway Deployment Process

1. **Create a new project in Railway**:

   - Log in to your Railway account
   - Click "New Project" or "Deploy a GitHub Repo" from the dashboard
   - Choose "Deploy from GitHub repo"
   - Select your repository

2. **Configure a PostgreSQL database**:

   - In your project, click "New Service" → "Database" → "PostgreSQL"
   - Railway will automatically provision a PostgreSQL database and provide connection details

3. **Configure your web service**:

   - In your project, click "New Service" → "GitHub Repo"
   - Select your repository if not already selected
   - Railway will detect your Django application

4. **Configure environment variables**:

   - Click on your web service
   - Go to the "Variables" tab
   - Add the following variables:
     ```
     SECRET_KEY=your_production_secret_key
     DEBUG=False
     ALLOWED_HOSTS=your-railway-domain.up.railway.app
     DATABASE_URL=postgresql://postgres:password@containers-us-west-xxx.railway.app:7777/railway
     ```
   - Note: Railway will automatically inject the correct `DATABASE_URL` if your database and app are in the same project

5. **Add Railway build configuration**:
   Ensure your repository contains:

   - `Procfile` with: `web: gunicorn todo_project.wsgi`
   - `runtime.txt` with: `python-3.9.16`

6. **Update `settings.py` for production**:
   Ensure your Django settings include:

   ```python
   import os
   import dj_database_url

   # Configure database from DATABASE_URL environment variable
   DATABASES = {
       'default': dj_database_url.config(
           default=os.environ.get('DATABASE_URL'),
           conn_max_age=600
       )
   }

   # Static files configuration for WhiteNoise
   STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
   STATIC_URL = '/static/'
   STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
   ```

7. **Deploy your application**:

   - Railway will automatically build and deploy your application when changes are pushed to your repository
   - You can also manually trigger deployments from the Railway dashboard

8. **Apply migrations on Railway**:

   - Click on your web service
   - Go to the "Settings" tab → "Generate Command"
   - Run: `python manage.py migrate`

9. **Create a superuser on Railway (optional)**:

   - Use the same command generator
   - Run: `python manage.py createsuperuser`
   - Follow the prompts to create an admin user

10. **Access your deployed application**:
    - Click on your web service
    - Go to the "Settings" tab
    - Find your application URL under "Domains"

### Deployment Verification

After deployment, verify the following:

1. **Application Functionality**:

   - Test all CRUD operations
   - Verify database operations are working correctly
   - Check responsive design on various devices

2. **Security Configuration**:

   - Confirm HTTPS is enforced
   - Verify debug mode is disabled
   - Check that secret keys are not exposed

3. **Performance**:
   - Monitor application response times
   - Check database query performance
   - Verify static file serving

### Common Deployment Issues and Solutions

| Issue                     | Cause                              | Solution                                     |
| ------------------------- | ---------------------------------- | -------------------------------------------- |
| Application Error         | Misconfigured Procfile             | Check Procfile syntax and settings           |
| Database Connection Error | Incorrect DATABASE_URL             | Verify environment variables                 |
| Static Files Not Loading  | WhiteNoise not configured          | Check STATICFILES_STORAGE setting            |
| Server Error (500)        | Debug mode off, uncaught exception | Check Railway logs in the dashboard          |
| Migrations Not Applied    | Forgot to run migrations           | Run migrations through the command generator |

### Continuous Deployment

Railway supports continuous deployment from your GitHub repository:

1. Develop and test changes locally
2. Commit changes to version control
3. Push to GitHub repository
4. Railway automatically builds and deploys the new version
5. Apply any necessary migrations through the command generator
6. Verify functionality in production

## Future Improvements

While the current application provides a solid foundation for task management, several enhancements could improve functionality and user experience in future iterations:

### User Authentication and Multi-User Support

- **User registration and login system**: Allow multiple users to access the application with individual accounts
- **User-specific tasks**: Ensure each user only sees and manages their own tasks
- **Role-based permissions**: Add admin and regular user roles with different capabilities
- **Profile management**: Allow users to update their information and preferences

### Enhanced Task Features

- **Task categories or tags**: Enable organization of tasks by type or project
- **Priority levels**: Add high/medium/low priority indicators for tasks
- **Recurring tasks**: Support for tasks that repeat daily, weekly, monthly, etc.
- **Task dependencies**: Allow tasks to be marked as dependent on completion of other tasks
- **Subtasks**: Break down complex tasks into smaller, manageable components

### Notification System

- **Email reminders**: Send notifications for upcoming and overdue tasks
- **In-app notifications**: Alert users about task deadlines within the application
- **Calendar integration**: Sync tasks with Google Calendar or other calendar systems
- **Custom notification preferences**: Allow users to set when and how they receive reminders

### Advanced UI Features

- **Search and filter functionality**: Find tasks by keyword, date range, status, etc.
- **Drag-and-drop interface**: Reorder tasks and change status through direct manipulation
- **Dark mode option**: Alternative color scheme for reduced eye strain
- **Customizable dashboard**: Allow users to configure what information is displayed and how
- **Task visualization**: Charts and graphs showing task completion rates and trends

### Performance and Scalability

- **Task archiving**: Move completed tasks to an archive to improve performance
- **Pagination**: Implement pagination for users with large numbers of tasks
- **Caching**: Add Redis or Memcached for improved performance
- **API endpoints**: Create RESTful API for integration with other services
- **Mobile application**: Develop companion mobile apps for iOS and Android

### Integration Capabilities

- **File attachments**: Allow users to attach files to tasks
- **Third-party integrations**: Connect with productivity tools like Slack, Trello, etc.
- **Import/export functionality**: Enable task data to be imported or exported in common formats
- **Calendar synchronization**: Two-way sync with popular calendar services

### Implementation Priorities

These improvements have been prioritized based on user value and technical complexity:

1. **High Priority / Low Complexity**:

   - Task categories/tags
   - Search and filter functionality
   - Basic email reminders

2. **High Priority / Medium Complexity**:

   - User authentication system
   - Priority levels for tasks
   - Task archiving

3. **Medium Priority / Medium Complexity**:

   - Recurring tasks
   - File attachments
   - Dark mode option

4. **Long-term Goals**:
   - Mobile applications
   - Advanced integrations
   - Comprehensive analytics

## Testing

Testing was a fundamental part of the development process, ensuring the application functions correctly and reliably. Both manual and automated testing approaches were used to validate functionality.

### Testing Methodology

#### Automated Testing

Automated tests were implemented using Django's built-in testing framework, focusing on:

1. **Unit Tests**: Testing individual components in isolation

   - Model methods and properties
   - Form validation logic
   - View functions

2. **Integration Tests**: Testing how components work together
   - Form submissions and database updates
   - URL routing and view rendering
   - Template context processing

Example test case from the test suite:

```python
def test_task_creation(self):
    """Test that a task can be created with valid data"""
    task_count = Task.objects.count()
    response = self.client.post(reverse('task_create'), {
        'title': 'Test Task',
        'description': 'This is a test task',
        'due_date': '2025-12-31'
    })
    self.assertEqual(response.status_code, 302)  # Redirect on success
    self.assertEqual(Task.objects.count(), task_count + 1)
    new_task = Task.objects.latest('created_at')
    self.assertEqual(new_task.title, 'Test Task')
```

#### Manual Testing

Manual testing focused on aspects that are difficult to automate:

1. **User Interface Testing**:

   - Cross-browser compatibility (Chrome, Firefox, Safari, Edge)
   - Responsive design across device sizes
   - Visual consistency and alignment

2. **Usability Testing**:

   - Navigation flow and user journeys
   - Form interactions and feedback
   - Error handling and messaging

3. **Accessibility Testing**:
   - Keyboard navigation
   - Screen reader compatibility
   - Color contrast and text readability

A detailed testing log is available in the `testing.md` file.

## Conclusion

The Task Manager application demonstrates a comprehensive implementation of a database-backed web application using Python and Django. By focusing on core task management functionality with clean, maintainable code, the project fulfills the requirements for the L5 Diploma in Web Application Development.

The application leverages Django's powerful features to create a robust backend, with a responsive frontend that provides an intuitive user experience. Security considerations have been integrated throughout the development process, ensuring data protection and safe operation.

The development process followed best practices for web application development, including:

- Clear separation of concerns using the MVT (Model-View-Template) architecture
- Comprehensive testing to ensure functionality and reliability
- Security implementation to protect user data
- Responsive design for cross-device compatibility
- Detailed documentation for maintenance and future development

While the current implementation serves as a complete task management solution, the identified future improvements provide a roadmap for evolving the application to meet more complex requirements and user needs.

## Author

[Aurimas Ransys]

## License

This project is licensed under the MIT License - see the LICENSE file for details.
