# Introduction
This project is an API inspired by the requirements of the Payroll code challenge written by Wave Financial for their Full-Stack Engineer applicants. See [Wave Software Development Challenge](https://github.com/wvchallenges/se-challenge-payroll) for more details. 

# Features
This API has four endpoints:
- One endpoint to **register** an account and another to **login**
- Another endpoint to **upload** a csv file containing timekeeping data for employees
- A final endpoint to **retrieve** a report containing payroll information based on a bi-monthly pay cycle

The API also features user authentication and permissions for both endpoints. 

# Prerequisites
PostgreSQL is required to accommodate the DecimalFields used in this project. SQLite3 does not support this model field. 

# Assumptions
Beyond the assumptions already outlined in requirements in the link above, the API assumes that:
- Only a staff account is capable of creating job groups (for now - changes coming soon!)
- Job groups have been created in the database in advance of uploading a csv file. 

# Installation
1. Clone the repository
```
git clone https://github.com/cfaqiri/codechallenge.git
```
2. Install the requirements (virtual environment recommended)
```
pip install -r requirements.txt
```
3. Configure a PostgreSQL server in settings.py
4. Make all migrations
```
python manage.py migrate
```
5. Create a superuser
```
python manage.py createsuperuser
```
6. Log into /admin and add job groups

# Routes
## Register
The endpoint to register an account can be accessed via a POST request to the '/register' url.
## Login
The endpoint to sign in can be accessed via a POST request to the '/login' url.
## Upload 
The endpoint to upload a file can be accessed via a POST request to the '/upload' url.
## Retrieve
The endpoint to retrieve payroll information can be accessed via a GET request to the '/retrieve' url.



