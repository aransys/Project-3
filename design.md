# Design Documentation

## UX Design

The user experience design for this application focuses on simplicity, clarity, and efficiency—allowing users to manage their tasks with minimal friction. The design follows established UX principles to create an intuitive and accessible interface.

### Design Principles

#### Information Hierarchy

- Task information is presented in a clear, organized fashion with each piece of information being easy to find
- Semantic HTML5 markup is used to convey the structure of the application
- Information is prioritized with the most important task details (title, due date, status) visible at a glance
- Tasks are sorted by due date by default, placing the most urgent items at the top

#### User Control

- All interactions with the application aim to produce a positive emotional response
- Users have clear feedback for all actions (task creation, updates, completion)
- Error messages are descriptive and suggest solutions
- Users are never asked for information the application already possesses
- Progress indicators and confirmation messages are shown for all significant actions

#### Consistency

- Visual and interactive elements maintain consistency across all pages
- Navigation elements are consistently positioned
- Color coding is consistent (e.g., red for overdue tasks, green for completed)
- Form elements and controls follow the same patterns throughout

#### Accessibility

- The application adheres to WCAG 2.1 guidelines
- High contrast color schemes ensure readability
- All form elements include proper labels and ARIA attributes
- Keyboard navigation is fully supported throughout the application
- Semantic HTML provides structure for screen readers

### User Journey

The main user journeys through the application are designed to be intuitive and efficient:

1. **Task Creation Journey**:

   - User navigates to the dashboard
   - Clicks prominently displayed "Add Task" button
   - Completes the task creation form with minimal required fields
   - Receives confirmation upon successful creation
   - Is returned to the dashboard with the new task visible

2. **Task Completion Journey**:

   - User identifies a completed task in their list
   - Toggles the completion status with a single click/tap
   - Receives immediate visual feedback of the status change
   - Task is visually indicated as complete

3. **Task Management Journey**:
   - User selects a task that needs updating
   - Navigates to the detail view via a clear call-to-action
   - Updates the necessary information
   - Saves changes with a single action
   - Receives confirmation of successful update

## Wireframes

### Desktop View - Task List

```
+------------------------------------------------------+
| Todo Application [+ New Task]|
+------------------------------------------------------+
| Tasks (5) |
+------------------------------------------------------+
| ☐ Complete assignment [Due: Today]|
| Details | Edit | Delete |
+------------------------------------------------------+
| ☑ Read documentation [Due: Yesterday]|
| Details | Edit | Delete |
+------------------------------------------------------+
| ☐ Prepare presentation [Due: Tomorrow]|
| Details | Edit | Delete |
+------------------------------------------------------+
```

### Mobile View - Task List

```
+-------------------------+
| Todo Application [+] |
+-------------------------+
| Tasks (5) |
+-------------------------+
| ☐ Complete assignment |
| [Due: Today] |
| Details | Edit | Delete |
+-------------------------+
| ☑ Read documentation |
| [Due: Yesterday] |
| Details | Edit | Delete |
+-------------------------+
```

### Task Detail View

```
+------------------------------------------------------+
| Todo Application [Back to List] |
+------------------------------------------------------+
| Task: Complete assignment |
+------------------------------------------------------+
| Status: ☐ Not Completed [Mark Done] |
| Due Date: May 15, 2023 |
| |
| Description: |
| Finish the Django project assignment for the |
| Web Application Development course. |
| |
| Created: May 10, 2023 |
| |
| [Edit] [Delete] |
+------------------------------------------------------+
```

## Information Hierarchy

### Primary Elements (Most Important)

- Task list with completion status
- Add new task button
- Task details
- Action buttons (Edit, Delete, Mark Complete)

### Secondary Elements

- Due dates
- Creation timestamps
- Task descriptions

### Navigation Structure

- Main task list (home page)
- Individual task detail pages
- Create/edit forms
- Delete confirmation
- Simple breadcrumb navigation for return paths

## User Control Principles

### Confirmation

- Delete actions require explicit confirmation
- Changes to task status show immediate visual feedback

### Feedback

- Success messages for all CRUD operations
- Error messages for validation failures
- Visual indicators for task completion status

### Progress

- Clear completion indicators (checkboxes, badges)
- Visual distinction between completed and pending tasks

### Undo Safety

- No destructive actions without confirmation
- Cancel buttons on all forms

## Accessibility Considerations

### Semantic HTML

- Proper heading hierarchy (h1-h6)
- Semantic elements (`<nav>`, `<main>`, `<section>`, etc.)
- Meaningful link text (no "click here")

### Color Contrast

- Bootstrap default classes ensure WCAG AA compliance
- Additional testing with WebAIM contrast checker
- Not relying solely on color to convey meaning

### Keyboard Navigation

- All actions accessible via keyboard
- Logical tab order
- Focus indicators preserved

### Screen Reader Support

- aria-labels for interactive elements
- Descriptive alt text for any images
- Tested with screen reader simulation

## Color Scheme

- **Primary**: Bootstrap primary blue (#0d6efd)
- **Success**: Green for completed tasks (#198754)
- **Warning**: Yellow for pending tasks (#ffc107)
- **Danger**: Red for delete actions (#dc3545)
- **Light/Dark**: Neutral grays for backgrounds

## Typography

- System font stack for optimal performance
- 16px base font size for readability
- 1.5 line height for comfortable reading
- Consistent heading sizes

## Responsive Design Approach

- Mobile-first development methodology
- Bootstrap 5 grid system for layout
- Flexbox for component alignment
- Breakpoints at standard device sizes:
  - Small: 576px
  - Medium: 768px
  - Large: 992px
  - X-Large: 1200px

## Design Decisions and Rationale

### Single-Page List vs. Multiple Views

The application uses multiple views instead of a single-page approach to maintain simplicity and follow Django's view structure. This decision prioritizes backend learning goals while maintaining good UX through clear navigation.

### Form Design

Forms use Bootstrap's built-in styling for consistency and accessibility. Inline validation provides immediate feedback to users when inputs don't meet requirements.

### Task Status Visualization

Completed tasks are visually distinguished using both color and iconography (checkboxes) to ensure users can quickly identify task status regardless of visual abilities.

### Minimalist Approach

The interface intentionally avoids complex features like drag-and-drop ordering or nested tasks to maintain simplicity for the target audience. This aligns with the application's goal of being straightforward and focused.
