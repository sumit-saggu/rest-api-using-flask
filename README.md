# Flask User Management API

A simple Flask-based REST API for managing users, with HTML forms for adding and updating users from your browser.

## Features

- **Add User:** Create a new user via API (`/user`) or web form (`/newUser`).
- **List Users:** View all users (`/`).
- **Search User:** Get a user by ID (`/userSearch/<userId>`).
- **Update User:** Update user details via API (`/update/<userId>`) or web form (`/update`).
- **Delete User:** Remove a user by ID (`/delete/<userId>`).

## Endpoints

| Method   | Endpoint                        | Description                |
|----------|---------------------------------|----------------------------|
| GET      | `/`                             | List all users             |
| GET      | `/userSearch/<userId>`          | Get user by ID             |
| POST     | `/user`                         | Add user (JSON)            |
| GET/POST | `/newUser`                      | Add user (HTML form)       |
| PUT      | `/update/<userId>`              | Update user (JSON)         |
| GET      | `/update`                       | Update user (HTML form)    |
| DELETE   | `/delete/<userId>`              | Delete user                |

## How to Run

1. **Install dependencies:**
    ```sh
    pip install flask
    ```

2. **Start the server:**
    ```sh
    python app.py
    ```

3. **Open in browser:**
    - Add user: [http://localhost:5000/newUser](http://localhost:5000/newUser)
    - Update user: [http://localhost:5000/update](http://localhost:5000/update)

## Example API Usage

**Add a user (POST /user):**
```json
{
  "name": "Alice",
  "email": "alice@example.com",
  "password": "secret"
}
```

**Update a user (PUT /update/1):**
```json
{
  "name": "Alice Updated",
  "email": "alice@newmail.com"
}
```

**Delete a user (DELETE /delete/1):**
Use an API tool or JavaScript fetch as shown in the HTML files.

## Notes

- This app uses an in-memory list for users; data will reset when the server restarts.
- Passwords are stored in plain text for demonstration only. **Do not use in production.**
