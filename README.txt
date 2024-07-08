# Project Form Feedback

## Description
This project is a feedback application consisting of a frontend using Vue 2 and a backend using FastAPI. Feedback is stored in a PostgreSQL database.

## How to Run

### Frontend
1. Navigate to the `feedback-form` folder.
2. Run `npm install` command to install dependencies.
3. Run the `npm run serve` command to run the application.

### Backend
1. Navigate to the `feedback-api` folder.
2. Create a virtual environment and activate it.
3. Install dependencies using `pip install -r requirements.txt` command.
4. Start the FastAPI server using the `uvicorn app.main:app --reload` command.

### Testing
1. Make sure the local instance of PostgreSQL is running.
2. Run the `pytest` command in the `feedback-api` folder to run the tests.

## API documentation
Available endpoints:
- POST `/feedback/`: Saves the feedback value.