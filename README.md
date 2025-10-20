# Virtual Gaming Leaderboard API

A Django REST Framework (DRF) project that provides a backend API for managing categories, games, players, and scores for a virtual gaming leaderboard, Includes automated tests and manual Postman/Insomnia collections  

The API supports full CRUD operations and includes authentication, testing, and pagination.  

---
## Project Goals
- The API will allow users (players) to register and manage their profiles.
- Players can submit, update, and delete their scores.
- The system will generate a leaderboard that ranks players based on their scores.
- Filtering options will allow users to view leaderboards by limit, category, or date.
- The project will use Django Rest Framework (DRF) and PostgreSQL for database management.
- The API will be deployed to render

---
# Key decisions:
- Leaderboard calculation is encapsulated in `leaderboard/services.py` for testability and reuse.
- Aggregations are performed via Django ORM and optimized with DB indexes on `Score(game, -value, timestamp)`.
- Frontend demo available in `/frontend` (simple HTML + JS).

---

## Tech stack
 Backend Frameworks & Core Tools
- Python 3.12 – Primary programming language.
- Django 5.x – Web framework for building robust, scalable backends.
- Django REST Framework (DRF) – Provides API serialization, authentication, and view handling for RESTful endpoints.

 Database & ORM
- PostgreSQL – Main production database for reliability and scalability.
- SQLite – Lightweight database used for local development and testing.
- dj-database-url – Simplifies database configuration using environment variables.
- psycopg2-binary / mysqlclient – Database adapters for PostgreSQL and MySQL.

Storage & Cloud Utilities
- django-storages, boto3, botocore, s3transfer – Handle media and static file storage with AWS S3 or compatible services.
- django-csp – Adds Content Security Policy headers for enhanced app security.
- whitenoise – Serves static files efficiently in production without extra setup.

Filtering, Tagging & Media Handling
- django-filter – Adds filtering capabilities to API endpoints.
- django-taggit – Simplifies tagging functionality for models.
- pillow – Image processing library for handling uploaded media.

Environment & Config Management
- python-dotenv – Loads environment variables from a .env file.
- packaging, six, tzdata – Core utilities ensuring compatibility and timezone accuracy.

Deployment & Server
- Gunicorn – WSGI HTTP server for running Django apps in production.
- asgiref – ASGI utility for async support in Django.

Testing & Development
- pytest – Framework for automated testing.
- sqlparse, python-dateutil, urllib3, jmespath – Utility libraries for parsing, time handling, HTTP requests, and JSON data manipulation.

---

## Features 
- Players - manage player profiles.
- Scores - manage score submissions, tracks what a player scores in a game.
- Games - represents a virtual game (e.g call of duty, candy crush, clash of clans)
- Categories - groups games in different categories (e.g action, puzzle, strategy, racing) 
- leaderboard - ranking logic and leaderboard endpoints.

---

## Project Structure
Virtual-Gaming-Leaderboard/
│
├── leaderboard_api/            - outer project folder (Django project root)
│   ├── manage.py
│   ├── leaderboard_api/        - inner config package (with settings.py, urls.py, wsgi.py)
│   ├── category/
│   ├── games/
│   ├── players/
│   ├── scores/
│   ├── leaderboard/
│
├── frontend/                   - frontend folder
├── requirements.txt
└── README.md

---

## API Endpoints and HTTP Methods

| Resource | Method | Endpoint | Description | Data / Params |
|-----------|---------|-----------|--------------|----------------|
| **Games** | `POST` | `/games/` | Create a new game | `name`, `category_id` |
|  | `GET` | `/games/` | List all games | — |
|  | `GET` | `/games/{id}/` | Retrieve details of a single game | — |
|  | `PUT` | `/games/{id}/` | Update game information | `name`, `category_id` |
|  | `DELETE` | `/games/{id}/` | Delete a game | — |
| **Players** | `POST` | `/players/` | Create a new player | `username`, `display_name`, `is_active` |
|  | `GET` | `/players/` | List all players (profiles) | — |
|  | `GET` | `/players/{id}/` | Retrieve a single player’s profile | — |
|  | `PUT` | `/players/{id}/` | Update a player’s profile | `display_name`, `is_active` |
|  | `DELETE` | `/players/{id}/` | Delete a player *(soft delete recommended)* | — |
| **Scores** | `POST` | `/scores/` | Submit a new score | `player_id`, `game_id`, `value` |
|  | `GET` | `/scores/` | List all scores *(optional filters: player, game)* | — |
|  | `PUT` | `/scores/{id}/` | Update a score | `value` |
|  | `DELETE` | `/scores/{id}/` | Delete a score entry | — |
| **Categories** | `POST` | `/categories/` | Create a new category | `name` |
|  | `GET` | `/categories/` | List all categories | — |
|  | `GET` | `/categories/{id}/` | Retrieve a single category | — |
|  | `PUT` | `/categories/{id}/` | Update a category name | `name` |
|  | `DELETE` | `/categories/{id}/` | Delete a category | — |
| **Leaderboard** | `GET` | `/leaderboard/?limit=10` | Retrieve top N players ranked by score | Query: `limit`, `category`, `date_range (today, this_week)` |
|  | `GET` | `/players/{id}/rank/` | Retrieve a specific player’s rank and score | — |

---
# Role Permissions Matrix
- Public user - Can only view leaderboard, rankings, players, and scores (read-only).

- Admin - Full control (create, update, delete players & scores, plus optional game/category management)

---

## Quickstart (local)
1. Clone
```bash
git clone https://github.com/bkay29/virtual-gaming-leaderboard-api.git
cd virtual-gaming-leaderboard-api


2. Create venv & install dependancies:
'''bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


3. Create .env (see .env.example) 
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3

you can locally using SQLite - no database setup required.


4. Run migrations and start the server:
'''bash
python manage.py migrate
python manage.py runserver

Visit
Home: http://127.0.0.1:8000/  - “Welcome to Virtual Gaming Leaderboard”
API Root: http://127.0.0.1:8000/api/  - Browsable DR view - lists all available endpoints.
DRF Login : http://127.0.0.1:8000/api-auth/login/


5. Testing using Postman
'''bash
use base url
curl http://127.0.0.1:8000/api/


Example requests:
 - GET /api/players/ — lists players
 - GET /api/players/{id}/rank/ — (if implemented) returns player's
 - GET /api/games/ - lists games
 - GET /api/games/{game_id}/leaderboard/?top=10 — top N players for a game


Testing using Pytest
'''bash 
pytest -q

 
6. Demo Leaderboard
request using curl:
    http://127.0.0.1:8000/api/games/1/leaderboard/?top=10


7. Live demo/frontend
- Minimal frontend is available at /frontend/index.html (simple JS to call leaderboard endpoints). Can be deployed to GitHub Pages for quick live demo.


8. Deployment
set env. variables 
DEBUG=False
Add Render domain to ALLOWED_HOSTS
Use environment variables for:
 - SECRET_KEY
 - DATABASE_URL (Render PostgreSQL)


9. Configure Gunicorn and create a Procfile:
web: gunicorn leaderboard_api.wsgi

Static files are automatically served via WhiteNoise.


10. STATUS: Active Deployment
live URLS:
https://virtual-gaming-leaderboard-api.onrender.com/api/
https://virtual-gaming-leaderboard-api.onrender.com/api/games/
https://virtual-gaming-leaderboard-api.onrender.com/api/players/
https://virtual-gaming-leaderboard-api.onrender.com/api/categories/
https://virtual-gaming-leaderboard-api.onrender.com/api/games/1/leaderboard/?top=10


Built with Django + DRF

by:bkay29