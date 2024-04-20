# Social Media Backend App

This backend application is built using FastAPI framework and serves as the backend for a social media platform. It provides various features such as managing users, creating and interacting with posts, and voting on posts.

## Features

- **User Management**: Allows users to register, login, and manage their profiles.
- **Post Management**: Enables users to create, read, update, and delete posts.
- **Voting System**: Users can up-vote or down-vote posts.
- **Authentication and Authorization**: Implements JWT-based authentication and role-based authorization.
- **Data Validation**: Utilizes Pydantic models for request and response data validation.
- **Swagger Documentation**: Automatically generated interactive API documentation using Swagger UI.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/social-media-backend.git
   cd social-media-backend

2. Create and activate a virtual environment (recommended):
    python -m venv venv
    source venv/bin/activate   # On Windows, use venv\Scripts\activate

3. Install the dependencies:
    pip install -r requirements.txt

4. Set up the environment variables by creating a .env file in the root directory and adding the following:
    refer to .env.sample file in the directory

5. Run the migrations to set up the database:
    alembic upgrade head

6. Start the FastAPI server:
    uvicorn app.main:app --reload

The API will be accessible at http://localhost:8000.

## Documentation
The API documentation is automatically generated and can be accessed at http://localhost:8000/docs.

## Contributing
Contributions are welcome! Please feel free to submit issues for bug fixes, feature requests, or any other improvements.

## License
This project is licensed under the MIT License.

Feel free to adjust the content according to your project specifics! Let me know if you need any further customization.