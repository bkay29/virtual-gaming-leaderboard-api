# Virtual Gaming Leaderboard API

A Django REST Framework (DRF) project that provides a backend API for managing categories, games, players, and scores for a virtual gaming leaderboard.  

The API supports full CRUD operations and includes authentication, testing, and pagination.  

---

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
leaderboard_api/
│── category/ # Category app (models, views, serializers, tests)
│── games/ # Games app
│── players/ # Players app
│── scores/ # Scores app
│── leaderboard/ # Leaderboard logic
│── leaderboard_api/ # Main project folder (settings, urls)
│── manage.py



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



Testing
Manual Testing (Postman / Insomnia)
Tests CRUD for all endpoints.


Tech Stack
Python 3.12
Django 5.x
Django REST Framework
PostgreSQL (or SQLite for tests)
pytest/unittest (for automated testing)


Author
Ednah Bridget Kakah
Backend Developer 
