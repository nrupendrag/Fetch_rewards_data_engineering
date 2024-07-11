# Fetch Rewards Data Engineering Take Home

## Project Overview
- **Purpose:** This project is designed to process user login behavior data from an AWS SQS queue, anonymize sensitive information, and store the data in a PostgreSQL database. The application is containerized using Docker and orchestrated with Docker Compose to ensure consistency across different environments.
- **Functionality:** Anonymize sensitive information and store the data in a PostgreSQL database.
- **Technologies Used:** Docker, Docker Compose, Python, AWS SQS, PostgreSQL.

## Prerequisites
Before you begin, ensure you have the following software installed:
- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)
- **Python 3.x**: [Install Python](https://www.python.org/downloads/)
- **Git**: [Install Git](https://git-scm.com/downloads)

## Installation

### 1. Clone the Repository
### First, clone the repository from GitHub to your local machine:
git clone https://github.com/<username>/fetch_rewards_data_engineering.git  
cd fetch_rewards_data_engineering

### 2. Set Up Docker Environment
### Use Docker Compose to set up and run the required services (LocalStack and PostgreSQL):
docker-compose up -d

### 3. Set Up Python Environment
### Navigate to the app directory and set up a Python virtual environment:
cd app
python -m venv venv
### Activate the virtual environment On Windows:
venv\Scripts\activate

### 4. Install Python Dependencies
### Install the necessary Python packages listed in requirements.txt:
Running the Application
### Ensure the Docker containers are running:
docker-compose ps  
-**This command should show that the localstack and postgres services are up and running.**
### Run the application:
python app.py

### Assumptions:
-**The SQS queue and PostgreSQL are running locally via Docker**.  
-**The input data structure is consistent with the provided examples.**  
-**Default values are acceptable for missing data fields.**  
  
### Future Enhancements:
### To make this project more robust and production-ready, consider the following enhancements:
-**Implement robust error handling and retry mechanisms**.   
-**Add unit tests for each component.**  
-**Optimize performance for larger datasets.**  
-**Implement logging and monitoring.**  
-**Secure sensitive information using environment variables or a secrets manager.**  
