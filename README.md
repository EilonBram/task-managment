# Task Management App

## Overview

This project is a **Task Management System** that allows users to register, log in, and manage their tasks. The application is built with a REST API backend. The system ensures that tasks are securely associated with authenticated users, emphasizing security, error handling, and maintainability.

### Backend Features 
1. **User Registration**: Create a new user account.
2. **User Login**: Authenticate users and generate a JWT token.
3. **Task Management**:
   - Add tasks.
   - View all tasks.
   - Update task details.
   - Delete tasks.
4. **Secure API**: Each user manages only their tasks.


## Setup and Installation- backend
1. install pip package manager
2. install SQLite, to look at the data base. 
3. save the folders, and open the terminal with the path to that folder: "cd c:myPath.."
4. run the backend with this command in the terminal: "python app.py --port=5000 --host=127.0.0.1"
5. open SQLite to perform actions with the backend- run this: "sqlite3 cd c:myPath.."
6. now you can perform all the required actions with the backend:
   a. **register**- INSERT INTO User (username, password) VALUES ('newuser', 'securepassword');
   b. **login**-  SELECT * FROM User WHERE username = 'testuser' AND password = 'securepassword';
   c. **add a task**- INSERT INTO Task (description) VALUES ('This is the task description');
   d. **get all task**- SELECT * FROM Task;
   e. **update a task**- UPDATE Task SET description = 'Updated Task description', description = 'Updated Description', completed = True WHERE id = the id of the task (number);
   f. **delete a task**- DELETE FROM Task WHERE id = the id of the task (number);

## fronend
i build nice web for the task managment system. unfortunatly, during my push to githab, my frontend somhow crushed by my backend.
the backend remains the same, but i failed to restore my frontend folder. 
the backend works very good, so i hope its alright.

