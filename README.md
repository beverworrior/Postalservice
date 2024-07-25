# Postal Service Web Application

This is a simple postal service web application built with Django. The application includes features for user authentication, shipment tracking, and a responsive front-end.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Running the Project Locally](#running-the-project-locally)
- [Deploying to Heroku](#deploying-to-heroku)
- [Troubleshooting](#troubleshooting)

## Features

- User registration and authentication
- Shipment tracking
- Responsive design
- Admin panel for managing shipments

## Requirements

- Python 3.8+
- Django 3.2+
- PostgreSQL
- Git
- Heroku CLI (for deployment)

## Setup

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd Postalservice
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory and add the following variables:

    ```plaintext
    SECRET_KEY=your-secret-key
    DATABASE_URL=your-database-url
    DEBUG=True
    ```

5. **Apply database migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

7. **Collect static files:**

    ```bash
    python manage.py collectstatic
    ```

## Running the Project Locally

1. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

2. **Open the application in your browser:**

    Go to `http://localhost:8000`

## Deploying to Heroku

1. **Log in to Heroku:**

    ```bash
    heroku login
    ```

2. **Create a new Heroku app:**

    ```bash
    heroku create
    ```

3. **Set up environment variables on Heroku:**

    ```bash
    heroku config:set SECRET_KEY=your-secret-key
    heroku config:set DATABASE_URL=your-database-url
    heroku config:set DEBUG=False
    ```

4. **Deploy to Heroku:**

    ```bash
    git push heroku master
    ```

5. **Run database migrations on Heroku:**

    ```bash
    heroku run python manage.py migrate
    ```

6. **Collect static files on Heroku:**

    ```bash
    heroku run python manage.py collectstatic --noinput
    ```

## Troubleshooting

- **CSRF Verification Failed:**
    - Ensure your CSRF settings are correctly configured in `settings.py`.
    - Add your domain to the `CSRF_TRUSTED_ORIGINS` setting.

- **400 Bad Request:**
    - Check that your `ALLOWED_HOSTS` setting includes your domain.
    - Ensure your browser is accepting cookies.

- **500 Server Error:**
    - Check the server logs for detailed error messages.
    - Ensure all environment variables are set correctly.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
