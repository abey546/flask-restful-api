
# Video Management RESTful API

## Project Overview
The project involves creating a RESTful API using Flask and Flask-RESTful that manages video data stored in a SQLite database via SQLAlchemy. The API allows clients to perform CRUD operations (Create, Read, Update, Delete) on video records. Each video record includes an ID, name, number of views, and number of likes. The API includes endpoints to:
- Create a new video (`PUT /video/<int:video_id>`)
- Retrieve video details (`GET /video/<int:video_id>`)
- Update specific fields of a video (`PATCH /video/<int:video_id>`)
- Delete a video ('delete /video/<int:video_id>`)

## Learning Objectives
The student is likely aiming to learn and practice the following skills and concepts through this project:

### RESTful API Design
- Understanding the principles of REST and how to design RESTful endpoints for CRUD operations.
- Learning how to handle HTTP methods (`GET`, `PUT`, `PATCH`, `DELETE`) appropriately.

### Flask Framework
- Gaining familiarity with Flask, a micro web framework in Python, to build web applications and APIs.
- Using Flask-RESTful to simplify the creation of RESTful APIs.

### Database Integration with SQLAlchemy
- Learning how to use SQLAlchemy, an ORM (Object-Relational Mapping) library, to interact with the SQLite database.
- Defining database models and performing database operations such as querying, inserting, and updating records.

### Request Parsing and Validation
- Using `reqparse` from Flask-RESTful to parse and validate incoming request data.
- Ensuring that required fields are present and data types are correct.

### Error Handling
- Implementing error handling to return appropriate HTTP status codes and messages (e.g., `404 Not Found`, `409 Conflict`).

### Data Serialization
- Using `marshal_with` from Flask-RESTful to serialize SQLAlchemy models into JSON format for API responses.

### Software Development Best Practices
- Structuring a Flask application using the factory pattern to create and configure the app.
- Managing application contexts and database initialization.
- Writing clean, maintainable, and well-documented code.

## Code Breakdown

### App Initialization and Configuration
- `create_app()` function initializes the Flask app and configures the SQLAlchemy database.
- Database URI is set to use a SQLite database file (`sqlite:///database.db`).

### Database Model
- `VideoModel` defines the structure of the video table with columns for `id`, `name`, `views`, and `likes`.

### Request Parsers
- `video_put_args` and `video_patch_args` parse and validate incoming data for `PUT` and `PATCH` requests respectively.

### Resource Fields
- `resource_fields` defines the fields to be serialized when returning video data in API responses.

### Video Resource
- `get(video_id)`: Retrieves a video by its ID.
- `put(video_id)`: Creates a new video with the provided ID and data.
- `patch(video_id)`: Updates specific fields of an existing video.

### API Endpoints
- `api.add_resource(Video, "/video/<int:video_id>")` adds the `Video` resource to the API with the specified endpoint.

### Running the App
- The Flask app is run with `debug=True`, enabling development features like the debugger and automatic reloading.

## How to Run
1. Clone the repository:
   ```sh
   git clone https://github.com/abey546/videomanagementapi.git
   cd videomanagementapi

2. install dependencies:
   ```sh
   pip install -r requirements.txt
3. Run the application:
   ```sh
   python main.py

Conclusion:
 
 This project provides hands-on experience in building a complete RESTful API with database integration, enhancing your understanding of web development and backend programming.
