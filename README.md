# User Authentication API

## Overview
This FastAPI project provides user authentication using JWT and MongoDB. It includes secure endpoints for user management and is structured for scalability.

## Features
### Must Have
- **Login and Logout** endpoints.
- Secure CRUD operations for users.
- Predefined script to create a user in the database.

### Good to Have
- Predefined Pydantic models for users and tokens.
- MongoDB Atlas integration.
- Scalable code structure for future extensions.

## Installation

### Prerequisites
- Python 3.8+
- MongoDB Atlas (or local MongoDB server)
- Dependencies in `requirements.txt`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/sourabhs701/Resolute.git
   cd Resolute


   pip install -r requirements.txt -t .  # Install to current directory

   zip -r app.zip .  # Includes code and dependencies

   aws lambda update-function-code --function-name User_auth --zip-file fileb://app.zip

