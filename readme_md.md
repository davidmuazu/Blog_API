# Personal Blogging Platform REST API

A modular, scalable, and fully authenticated RESTful API built with **Python**, **Django**, and **Django REST Framework (DRF)**. Designed following clean software architecture principles, this platform enforces strict object-level content ownership, relational data management, and stateless JWT security.

---

## 📸 Key Features

* **JWT Authentication:** Secure user registration, authentication, and token management via `djangorestframework-simplejwt`.
* **Post Lifecycle Management:** Full CRUD capabilities for blog posts with automated author attribution.
* **Granular Object Permissions:** Custom permission classes (`IsAuthorOrReadOnly`, `IsCommentAuthorOrReadOnly`) ensuring content modifications are strictly limited to the original author.
* **Nested Comment System:** Post-specific commenting engine with query filtering and strict relational integrity checks (`get_object_or_404`).
* **Search & Querying:** Dynamic search capabilities across post titles and body content using DRF `SearchFilter`.
* **Admin Interface:** Configured Django Admin dashboard for administrative backend supervision.

---

## 🛠️ Tech Stack

* **Language:** Python 3.12+
* **Framework:** Django 5.x | Django REST Framework (DRF)
* **Authentication:** SimpleJWT (JSON Web Tokens)
* **Database:** SQLite (Development) / PostgreSQL-ready

---

## 📂 Project Architecture

The backend follows a modular app structure separated by domain responsibilities:

```text
blog_api/
│
├── config/             # Root configuration directory (settings, URLs, WSGI)
├── users/              # Custom user authentication and registration logic
├── posts/              # Post CRUD engine, custom ownership permissions, search
├── comments/           # Relational commenting system and comment permissions
├── manage.py           # Django command-line execution utility
└── requirements.txt    # Project dependencies
```

---

## ⚙️ Environment Variables & Configuration

Create a `.env` file in the project root directory (alongside `manage.py`) to manage environment configuration:

```ini
# Django Settings
SECRET_KEY=your-super-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Database (Default: SQLite)
DATABASE_URL=sqlite:///db.sqlite3
```

---

## 🚀 Getting Started

Follow these steps to get a local development environment running:

### 1. Prerequisites
Ensure you have **Python 3.10+** and **Git** installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/your-username/blog_api.git
cd blog_api
```

### 3. Set Up Virtual Environment
* **Linux/macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
* **Windows (Command Prompt / Git Bash):**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations
```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python manage.py runserver
```
The API will be live at `http://127.0.0.1:8000/`.

---

## 📡 API Reference & Endpoints

All request/response payloads utilize JSON formatting. Protected endpoints require a valid JWT Access Token attached in the HTTP Header:
```http
Authorization: Bearer <your_access_token>
```

### 1. Authentication (`/api/auth/`)

| Method | Endpoint | Auth Required | Description |
| :--- | :--- | :---: | :--- |
| `POST` | `/api/auth/register/` | No | Register a new user account |
| `POST` | `/api/auth/login/` | No | Obtain JWT Access and Refresh token pair |
| `POST` | `/api/auth/refresh/` | No | Obtain new Access Token using Refresh Token |

#### Sample Registration Body (`POST /api/auth/register/`):
```json
{
  "username": "developer",
  "email": "dev@example.com",
  "password": "SecurePassword123!"
}
```

---

### 2. Posts (`/api/posts/`)

| Method | Endpoint | Auth Required | Description |
| :--- | :--- | :---: | :--- |
| `GET` | `/api/posts/` | No | Retrieve list of all posts |
| `POST` | `/api/posts/` | **Yes** | Create a new blog post |
| `GET` | `/api/posts/<id>/` | No | Retrieve details of a specific post |
| `PUT` | `/api/posts/<id>/` | **Yes (Author Only)** | Full update of a post |
| `PATCH` | `/api/posts/<id>/` | **Yes (Author Only)** | Partial update of a post |
| `DELETE`| `/api/posts/<id>/` | **Yes (Author Only)** | Delete a post |

#### Search Query Parameter:
Filter posts by keyword across `title` or `content`:
```http
GET /api/posts/?search=django
```

---

### 3. Comments (`/api/`)

| Method | Endpoint | Auth Required | Description |
| :--- | :--- | :---: | :--- |
| `GET` | `/api/posts/<post_id>/comments/` | No | List all comments under a post |
| `POST` | `/api/posts/<post_id>/comments/` | **Yes** | Add a new comment to a post |
| `GET` | `/api/comments/<id>/` | No | Retrieve a specific comment |
| `PUT` | `/api/comments/<id>/` | **Yes (Author Only)** | Update comment text |
| `DELETE`| `/api/comments/<id>/` | **Yes (Author Only)** | Delete a comment |

---

## 🧪 Testing

Run Django's test suite to verify application functionality:

```bash
python manage.py test
```

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.