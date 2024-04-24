# To-Do Project with FastAPI

This is a sample To-Do project built with the FastAPI framework. It is intended for educational purposes and to demonstrate basic CRUD operations with FastAPI, SQLAlchemy, PostgreSQL, and Alembic for database migrations.

## Project Overview

This project allows users to create, read, update, and delete tasks in a To-Do list. It serves as an introduction to building RESTful APIs with FastAPI and integrating a PostgreSQL database for persistent storage.

## Technologies Used

- **FastAPI**: A modern, high-performance web framework for building APIs with Python.
- **SQLAlchemy**: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **PostgreSQL**: A powerful, open-source relational database system.
- **Alembic**: A lightweight database migration tool for SQLAlchemy.

## Installation and Setup

To run this project locally, follow these steps:

1. Clone the repository:
   ```
   git clone <your-repository-url>
   cd <repository-folder>
   ```
   
2. Create a virtual environment and activate it:
```
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```

3. Install the project dependencies:
```
pip install -r requirements.txt
```

4. Set up the PostgreSQL database:
Create a new PostgreSQL database.
Update the database configuration in the project with your PostgreSQL connection details.

5. Apply database migrations using Alembic:
```
 alembic upgrade head
```
6. Start the FastAPI server:
```
uvicorn main:app --reload
```
7. Open your web browser and navigate to http://localhost:8000/docs to view the interactive API documentation provided by FastAPI.
