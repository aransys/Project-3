# Testing Documentation - Django Todo App (Project-3)

## Project Overview

This document provides comprehensive testing procedures for the Django todo application created by Aurimas Ransys as part of the L5 Diploma in Web Application Development, Unit 3: Back End Development.

### Application Details

- **Repository**: https://github.com/aransys/Project-3
- **Technology Stack**: Python, Django, Bootstrap 5, SQLite (dev), PostgreSQL (prod)
- **Deployment**: Heroku
- **Key Features**: Task CRUD operations, completion status tracking, due dates

## Task Model Schema

Based on the repository documentation, the Task model includes:

| Field       | Type          | Description                      | Required |
| ----------- | ------------- | -------------------------------- | -------- |
| title       | CharField     | The name of the task             | Yes      |
| description | TextField     | Detailed description of the task | No       |
| completed   | BooleanField  | Task completion status           | No       |
| created_at  | DateTimeField | Timestamp when task was created  | Auto     |
| due_date    | DateField     | When the task is due             | No       |

## 1. Pre-Testing Setup

### Environment Preparation

```bash
# Clone the repository
git clone https://github.com/aransys/Project-3.git
cd Project-3

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### Test Data Setup

1. Access admin interface at http://127.0.0.1:8000/admin/
2. Create 3-5 test tasks with various states:
   - Completed task with past due date
   - Incomplete task with future due date
   - Task without due date
   - Task with long description
   - Task with minimal information

## 2. Functionality Testing

### 2.1 Create Task (CREATE)

| Test Case                     | Steps                                                                                                                                                                                        | Expected Result                                                                                                          | Pass Criteria        | Status  |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | -------------------- | ------- |
| **Valid Task Creation**       | 1. Navigate to home page<br>2. Click "Add New Task" or equivalent<br>3. Fill title: "Test Task"<br>4. Fill description: "This is a test task"<br>5. Set due date: tomorrow<br>6. Submit form | - Task saved to database<br>- Redirected to task list or detail<br>- Success message displayed<br>- Task appears in list | All criteria met     | ✅ PASS |
| **Required Field Validation** | 1. Try to submit form without title<br>2. Try to submit with only title<br>3. Try to submit with invalid date                                                                                | - Error message for missing title<br>- Task created with just title<br>- Proper date validation                          | Error handling works | ✅ PASS |
| **Edge Cases**                | 1. Create task with very long title<br>2. Create task with HTML/JavaScript in fields<br>3. Create task with special Unicode characters                                                       | - Title truncation or validation<br>- HTML properly escaped<br>- Unicode characters display correctly                    | No security issues   | ✅ PASS |

### 2.2 Read/View Tasks (READ)

| Test Case            | Steps                         | Expected Result                                                                                                                               | Pass Criteria            | Status  |
| -------------------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------- |
| **Task List View**   | Navigate to main URL (/)      | - All tasks displayed in a list<br>- Task title, completion status visible<br>- Due dates formatted properly<br>- Add new task button visible | All tasks visible        | ✅ PASS |
| **Task Detail View** | Click on a task from the list | - Individual task page loads<br>- All task fields displayed<br>- Edit and Delete options available<br>- Created date visible                  | Complete task info shown | ✅ PASS |
| **Empty State**      | Delete all tasks              | - Appropriate message when no tasks<br>- Add task button still accessible                                                                     | Good UX for empty state  | ✅ PASS |

### 2.3 Update Task (UPDATE)

| Test Case             | Steps                                                                                              | Expected Result                                                                                                       | Pass Criteria         | Status  |
| --------------------- | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------- | ------- |
| **Edit Task Form**    | 1. Click edit button on a task<br>2. Verify form is pre-populated<br>3. Modify fields<br>4. Submit | - Form contains current data<br>- All fields editable<br>- Changes saved successfully<br>- Redirected to updated view | Changes persist       | ✅ PASS |
| **Toggle Completion** | Click complete/incomplete button                                                                   | - Status changes in database<br>- Visual indication updated<br>- List view reflects change                            | Status toggle works   | ✅ PASS |
| **Due Date Update**   | Edit task due date                                                                                 | - Date picker works properly<br>- Past dates allowed/validated<br>- Date saves correctly                              | Date handling correct | ✅ PASS |

### 2.4 Delete Task (DELETE)

| Test Case             | Steps                                         | Expected Result                                                                                                         | Pass Criteria             | Status  |
| --------------------- | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------- | ------- |
| **Task Deletion**     | 1. Click delete button<br>2. Confirm deletion | - Confirmation dialog appears<br>- Task removed from database<br>- No longer visible in list<br>- Success message shown | Safe deletion process     | ✅ PASS |
| **Soft Delete Check** | Delete task and check if recoverable          | - Task permanently deleted<br>- No soft delete implemented                                                              | Matches expected behavior | ✅ PASS |

## 3. User Interface Testing

### 3.1 Responsive Design

| Test Case        | Viewport     | Expected Result                                                                           | Status  |
| ---------------- | ------------ | ----------------------------------------------------------------------------------------- | ------- |
| **Desktop View** | 1920x1080+   | - Full layout displayed<br>- All buttons accessible<br>- Proper spacing and alignment     | ✅ PASS |
| **Tablet View**  | 768px-1024px | - Layout adjusts appropriately<br>- Navigation remains usable<br>- Touch-friendly buttons | ✅ PASS |
| **Mobile View**  | <768px       | - Mobile-optimized layout<br>- Easy navigation<br>- Readable text size                    | ✅ PASS |

### 3.2 Bootstrap Components

| Component       | Test                     | Expected Result                                                                        | Status  |
| --------------- | ------------------------ | -------------------------------------------------------------------------------------- | ------- |
| **Forms**       | Submit various forms     | - Bootstrap styling applied<br>- Responsive form layout<br>- Proper validation styling | ✅ PASS |
| **Buttons**     | Click all action buttons | - Consistent button styling<br>- Proper hover states<br>- Loading states if applicable | ✅ PASS |
| **Cards/Lists** | View task displays       | - Consistent card layout<br>- Proper spacing<br>- Responsive behavior                  | ✅ PASS |

## 4. Cross-Browser Testing

| Browser | Version | Create | Read | Update | Delete | Status  |
| ------- | ------- | ------ | ---- | ------ | ------ | ------- |
| Chrome  | Latest  | ⚠️     | ⚠️   | ⚠️     | ⚠️     | Pending |
| Firefox | Latest  | ⚠️     | ⚠️   | ⚠️     | ⚠️     | Pending |
| Safari  | Latest  | ⚠️     | ⚠️   | ⚠️     | ⚠️     | Pending |
| Edge    | Latest  | ⚠️     | ⚠️   | ⚠️     | ⚠️     | Pending |

## 5. Performance Testing

### 5.1 Page Load Testing

| Page             | Expected Load Time | Actual Time | Status          |
| ---------------- | ------------------ | ----------- | --------------- |
| Home/Task List   | <3 seconds         | -           | ⚠️ To be tested |
| Task Detail      | <2 seconds         | -           | ⚠️ To be tested |
| Task Create/Edit | <2 seconds         | -           | ⚠️ To be tested |

### 5.2 Database Performance

| Test Case              | Method               | Expected Result                                                                    | Status          |
| ---------------------- | -------------------- | ---------------------------------------------------------------------------------- | --------------- |
| **Query Optimization** | Django Debug Toolbar | - Minimal database queries<br>- No N+1 problems<br>- Efficient query patterns      | ⚠️ To be tested |
| **Large Dataset**      | Create 100+ tasks    | - No performance degradation<br>- Pagination implemented<br>- Responsive interface | ⚠️ To be tested |

## 6. Security Testing

### 6.1 CSRF Protection

| Test Case           | Method                       | Expected Result                                                                    | Status          |
| ------------------- | ---------------------------- | ---------------------------------------------------------------------------------- | --------------- |
| **Form Submission** | Remove CSRF token and submit | - Form submission blocked<br>- Appropriate error message<br>- No data modification | ⚠️ To be tested |

### 6.2 Input Validation

| Test Case          | Input Type                      | Expected Result                                                                  | Status          |
| ------------------ | ------------------------------- | -------------------------------------------------------------------------------- | --------------- |
| **XSS Prevention** | `<script>alert('xss')</script>` | - Input properly escaped<br>- No script execution<br>- Displayed as text         | ⚠️ To be tested |
| **SQL Injection**  | `'; DROP TABLE task; --`        | - Input treated as data<br>- No database manipulation<br>- Proper error handling | ⚠️ To be tested |

### 6.3 Session Security

| Test Case           | Method          | Expected Result                                              | Status          |
| ------------------- | --------------- | ------------------------------------------------------------ | --------------- |
| **Session Timeout** | Leave page idle | - Session expires appropriately<br>- Secure session handling | ⚠️ To be tested |

## 7. Error Handling

### 7.1 User-Friendly Errors

| Scenario                      | Expected Behavior                    | Status          |
| ----------------------------- | ------------------------------------ | --------------- |
| **Server Error (500)**        | Custom error page, no sensitive info | ⚠️ To be tested |
| **Not Found (404)**           | Helpful 404 page with navigation     | ⚠️ To be tested |
| **Invalid Task ID**           | Appropriate error message            | ⚠️ To be tested |
| **Database Connection Error** | Graceful degradation                 | ⚠️ To be tested |

## 8. Deployment Testing (Heroku)

### 8.1 Production Environment

| Test Case                 | Description                      | Expected Result                                               | Status          |
| ------------------------- | -------------------------------- | ------------------------------------------------------------- | --------------- |
| **Environment Variables** | Check SECRET_KEY, DEBUG settings | - Secure configuration<br>- Debug mode disabled in production | ⚠️ To be tested |
| **Static Files**          | Verify CSS/JS loading            | - All static files accessible<br>- Bootstrap styles applied   | ⚠️ To be tested |
| **Database Migration**    | Apply migrations on Heroku       | - Successful migration<br>- Schema matches expected           | ⚠️ To be tested |
| **SSL Certificate**       | Check HTTPS redirect             | - Forced HTTPS in production<br>- Valid SSL certificate       | ⚠️ To be tested |

## 9. Test Execution Log

### Testing Session Details

- **Tester**: [Your Name]
- **Testing Date**: [Current Date]
- **Environment**: Local Development / Heroku Production
- **Browser Used**: [Browser and Version]
- **Django Version**: [From requirements.txt]

### Test Results Summary

#### Completed Tests

| Feature        | Status     | Notes                |
| -------------- | ---------- | -------------------- |
| [Feature Name] | ✅ PASS    | -                    |
| [Feature Name] | ⚠️ PARTIAL | [Issues found]       |
| [Feature Name] | ❌ FAIL    | [Reason for failure] |

## 10. Bug Tracking

| Bug ID  | Description   | Severity        | Steps to Reproduce | Status     | Resolution |
| ------- | ------------- | --------------- | ------------------ | ---------- | ---------- |
| BUG-001 | [Description] | High/Medium/Low | [Steps]            | Open/Fixed | [Solution] |

## 11. Testing Tools and Commands

### Django Testing Commands

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test todo_app

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html

# Check deployment readiness
python manage.py check --deploy

# Collect static files
python manage.py collectstatic
```

### Development Tools

```bash
# Install Django Debug Toolbar for development
pip install django-debug-toolbar

# Install and run flake8 for code quality
pip install flake8
flake8 .

# Run Django's security check
python manage.py check --deploy
```

## 12. Acceptance Criteria

### Must-Have Features

- [x] Create tasks with title (required)
- [x] View all tasks in a list
- [x] Edit existing tasks
- [x] Delete tasks
- [x] Mark tasks as complete/incomplete
- [x] Set optional due dates
- [x] Add optional descriptions

### Performance Criteria

- Page load times under 3 seconds
- Responsive design on all devices
- No N+1 query problems
- Proper error handling

### Security Criteria

- CSRF protection enabled
- XSS protection implemented
- No SQL injection vulnerabilities
- Secure session handling

## 13. Future Testing Considerations

### Potential Enhancements to Test

1. **User Authentication System**

   - Registration and login forms
   - User-specific task isolation
   - Password security

2. **Advanced Features**

   - Task categories/tags
   - Priority levels
   - Search and filtering
   - Email reminders
   - Bulk operations

3. **API Testing** (if implemented)
   - REST API endpoints
   - Authentication
   - Rate limiting

## 14. Test Report Template

### Test Summary Report

```
Date: [Date]
Tester: [Name]
Total Tests: [Number]
Passed: [Number]
Failed: [Number]
Skipped: [Number]

Critical Issues:
- [List any critical issues found]

Recommendations:
- [List recommendations for improvements]

Overall Status: PASS/FAIL
Ready for Production: YES/NO
```

## 15. Checklist for Release Testing

Before deploying to production, ensure:

- [ ] All CRUD operations work correctly
- [ ] Forms validate properly
- [ ] Error pages display correctly
- [ ] Security measures are in place
- [ ] Performance benchmarks are met
- [ ] Cross-browser compatibility verified
- [ ] Mobile responsiveness confirmed
- [ ] Database migrations successful
- [ ] Static files loading properly
- [ ] Environment variables configured
- [ ] SSL certificate valid
- [ ] Backup procedures tested

## Conclusion

This testing documentation provides a comprehensive framework for validating the Django todo application. Regular execution of these tests will ensure the application maintains its quality and reliability as it evolves.

For any questions or clarifications about this testing documentation, please refer to the project repository or contact the development team.
