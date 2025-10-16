# Virtual Gaming Leaderboard API

A Django REST Framework (DRF) project that provides a backend API for managing categories, games, players, and scores for a virtual gaming leaderboard, Includes automated tests and manual Postman/Insomnia collections  

The API supports full CRUD operations and includes authentication, testing, and pagination.  

Key decisions:
- Leaderboard calculation is encapsulated in `leaderboard/services.py` for testability and reuse.
- Aggregations are performed via Django ORM and optimized with DB indexes on `Score(game, -value, timestamp)`.
- Frontend demo available in `/frontend` (simple HTML + JS).

---

## Tech stack
- Python 3.12, Django 5.x, Django REST Framework  
- PostgreSQL (development-ready; SQLite used for tests)  
- pytest for tests  
- Optional: Docker + docker-compose for local development


## Features
- Manage **Categories** (e.g. Puzzle, Action, Strategy)
- Manage **Games** (linked to Categories)
- Manage **Players**
- Track **Scores** (per Player, per Game)
- REST API with **CRUD endpoints**
- Authentication support
- Tested with **Postman/Insomnia** and automated Django tests

---


## Project Structure
Virtual-Gaming-Leaderboard/
│
├── leaderboard_api/            ← outer project folder (Django project root)
│   ├── manage.py
│   ├── leaderboard_api/        ← inner config package (with settings.py, urls.py, wsgi.py)
│   ├── category/
│   ├── games/
│   ├── players/
│   ├── scores/
│   ├── leaderboard/
│
├── frontend/                   ← optional frontend folder
├── requirements.txt
└── README.md





API Endpoints
| Resource    | Endpoint                            | Methods                 |
| ----------- | ----------------------------------- | ----------------------- |
| Categories  | `/api/categories/`                  | GET, POST               |
|             | `/api/categories/{id}/`             | GET, PUT, PATCH, DELETE |
| Games       | `/api/games/`                       | GET, POST               |
|             | `/api/games/{id}/`                  | GET, PUT, PATCH, DELETE |
| Players     | `/api/players/`                     | GET, POST               |
|             | `/api/players/{id}/`                | GET, PUT, PATCH, DELETE |
| Scores      | `/api/scores/`                      | GET, POST               |
|             | `/api/scores/{id}/`                 | GET, PUT, PATCH, DELETE |
| Leaderboard | `/api/games/{game_id}/leaderboard/` | GET                     |


## Quickstart (local)
1. Clone
```bash
git clone https://github.com/bkay29/virtual-gaming-leaderboard-api.git
cd virtual-gaming-leaderboard-api


2. Create venv & install:
'''bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


3. Create .env (see .env.example) with DB and SECRET_KEY, or use SQLite for quick runs.
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3

you can locally using SQLite - no database setup required.


4. Run migrations and start:
'''bash
python manage.py migrate
python manage.py runserver

Visit
Home: http://127.0.0.1:8000/
 - “Welcome to Virtual Gaming Leaderboard”
Browsable API Root: http://127.0.0.1:8000/api/
 - lists all available endpoints.
DRF Login (optional): http://127.0.0.1:8000/api-auth/login/


5. Demo Leaderboard:
'''bash
curl http://127.0.0.1:8000/api/games/1/leaderboard/?top=10


Endpoints (examples)
 - GET /api/players/ — list players
 - POST /api/scores/ — add score (body: {player: id, game: id, value: 120})
 - GET /api/games/{game_id}/leaderboard/?top=10 — top N players for a game
 - GET /api/players/{id}/rank/ — (if implemented) returns player's rank and total.


Testing
'''bash 
pytest -q


Live demo/rontend
- Minimal frontend is available at /frontend/index.html (simple JS to call leaderboard endpoints). Can be deployed to GitHub Pages for quick live demo.

Deployment
API is ready for render or other production platforms

For deployment
Set DEBUG=False
Add Render domain to ALLOWED_HOSTS
Use environment variables for:
 - SECRET_KEY
 - DATABASE_URL (Render PostgreSQL)

Configure Gunicorn and create a Procfile:
'''bash
web: gunicorn leaderboard_api.wsgi

Static files are handled by WhiteNoise (configured)


Author: Bkay29
Built with Django, powered by purpose.