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

6. **Access the API:**
   Open your browser and navigate to `http://localhost:8000` to access the Django REST API for the digital library.


## Deployment with Docker

1. **Build Docker Image:**
   ```bash
   # Build backend image
   docker build -t digital-library-backend .
   ```

2. **Run Docker Container:**
   ```bash
   # Run backend container
   docker run -p 8000:8000 -d digital-library-backend
   ```

## CI/CD Pipeline

The CI/CD pipeline is set up using GitHub Actions. Check the `.github/workflows` directory for the workflow configuration.

## Performance Consideration

To ensure high performance and reliability:

- Use Django's built-in caching mechanisms.
- Implement load balancing for distributing incoming traffic.
- Scale the Django backend horizontally by deploying multiple instances.

## Improvement Write-Up
-TODO

## Contributors

- Hasnat Abdullah (abdullah.2010bd@gmail.com)

Feel free to contribute by opening issues or submitting pull requests!