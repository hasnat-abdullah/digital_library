# Digital Library Management System

## Overview

This repository contains the Django backend for a full-stack digital library management system. The backend serves as a RESTful API, handling data operations for book records. The system includes a PostgreSQL database for storing book records.

## Technical Stack

- **Backend:**
  - Django
  - Django Rest Framework

- **Database:**
  - PostgreSQL

- **Deployment:**
  - Docker

- **CI/CD Pipeline:**
  - GitHub Actions

## Setup Instructions

### Prerequisites

- Python and pip installed
- PostgreSQL installed and running
- Docker installed (for containerization)

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/hasnat-abdullah/digital_library.git
   cd digital-library-backend
   ```

2. **Install Dependencies:**
   ```bash
   # Install backend dependencies
   pip install -r requirements/local.txt
   ```

3. **Update environment variables:**
   - Create a PostgreSQL database.
   - Create a `.env` file in the root directory of the project. Get necessary variable names from `example.env` and use appropriate values according to environment.
   - put `DB_HOST=localhost` in .env file if you run by `python manage.py runserver` command. If you run by docker-compose then put `DB_HOST=db` in .env file.

4. **Run Migrations:**
   ```bash
   # Apply database migrations
   python manage.py migrate
   ```

5. **Run the Django Development Server:**
   ```bash
   # Start the Django development server
   python manage.py runserver
   ```
   
6. **Seed database with fake data:**
   ```bash
   # seed db with few data
   python manage.py seed_db
   ```
7. **Run the following command to create a superuser:**
      ```shell
      python manage.py createsuperuser
      ```
      Follow the prompts and provide the required information such as first name, last name, email, and password.

8. **Access the API DOC:**
   Open your browser and navigate to `http://localhost:8000/api/v1/doc/re/` to access the Django REST API for the digital library.


## Run with Docker

1. **Build & Run Docker Container:**
   ```bash
   # Run backend container
   docker-compose -f docker-compose.yml up --build 
   ```

2. **Seed Database with fake data**

   1. Access the shell of the Docker container by running the following command:
      ```shell
      docker exec -it <container_name> /bin/bash
      ```
      Replace `<container_name>` with the name or ID of your Docker container.

   2. Once inside the container's shell, navigate to the project directory:
      ```shell
      cd /app
      ```

   3. Run the following command to create a superuser:
      ```shell
      python manage.py createsuperuser
      ```
      Follow the prompts and provide the required information such as first name, last name, email, and password.

   3. Run the following command to seed db with some data:
      ```shell
      python manage.py seed_db
      ```

   4. Exit the container's shell:
      ```shell
      exit
      ```

## CI/CD Pipeline

The CI/CD pipeline is set up using GitHub Actions. Check the `.github/workflows` directory for the workflow configuration.

## Performance Consideration

To ensure high performance and reliability:

- Use Django's built-in caching mechanisms.
- Implement load balancing for distributing incoming traffic.
- Scale the Django backend horizontally by deploying multiple instances.


## Contributors

- Hasnat Abdullah (abdullah.2010bd@gmail.com)

Feel free to contribute by opening issues or submitting pull requests!