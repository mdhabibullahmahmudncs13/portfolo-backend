# Portfolio Backend - Django REST API

Django REST Framework backend for the portfolio website, providing APIs for managing portfolio content including skills, projects, experience, certifications, and contact information.

---

## 🚀 Features

- **RESTful API** - Complete CRUD operations for all portfolio data
- **JWT Authentication** - Secure token-based authentication
- **Admin Panel** - Django admin interface for content management
- **Media Handling** - Image and file upload support
- **CORS Enabled** - Cross-origin resource sharing for frontend integration
- **Database Support** - SQLite for development, MySQL/PostgreSQL for production

---

## 📋 API Endpoints

### Public Endpoints (Read-Only)

```
GET  /api/hero/              - Get hero/about information
GET  /api/skills/            - List all skills
GET  /api/projects/          - List all projects
GET  /api/projects/featured/ - List featured projects
GET  /api/experience/        - List work experience
GET  /api/certifications/    - List certifications
GET  /api/contact/           - Get contact information
GET  /api/activities/        - List extracurricular activities
GET  /api/blog/              - List blog posts
POST /api/messages/          - Submit contact form
```

### Admin Endpoints (Authentication Required)

```
POST   /api/token/          - Obtain JWT token
POST   /api/token/refresh/  - Refresh JWT token
POST   /api/skills/         - Create new skill
PUT    /api/skills/{id}/    - Update skill
DELETE /api/skills/{id}/    - Delete skill
... (Similar CRUD for all resources)
```

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Django 4.2+**
- **Django REST Framework**
- **djangorestframework-simplejwt** - JWT authentication
- **django-cors-headers** - CORS support
- **Pillow** - Image processing
- **SQLite** - Development database
- **MySQL/PostgreSQL** - Production database

---

## 📦 Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager
- Virtual environment (recommended)

### Setup Steps

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   ```bash
   # Linux/Mac
   source venv/bin/activate
   
   # Windows
   venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - API: http://localhost:8000/api/
   - Admin Panel: http://localhost:8000/admin/

---

## 🗄️ Database Models

### Hero
Personal information and about section
- `name` - Full name
- `tagline` - Professional tagline
- `description` - About me description
- `image_url` - Profile image
- `video_url` - Background video
- `resume_url` - Resume PDF
- `media_type` - Image or video
- `github_url` - GitHub profile
- `linkedin_url` - LinkedIn profile
- `twitter_url` - Twitter/X profile
- `hackerrank_url` - HackerRank profile

### Skill
Technical skills organized by category
- `name` - Skill name
- `category` - Language/Framework/Tool/Platform/Other
- `icon` - Icon emoji or text
- `icon_image` - Icon image file
- `order` - Display order

### Project
Portfolio projects
- `title` - Project title
- `description` - Project description
- `image_url` - Project screenshot
- `demo_url` - Live demo link
- `github_url` - Source code link
- `technologies` - Tech stack (JSON array)
- `featured` - Featured project flag
- `order` - Display order

### Experience
Work experience entries
- `company` - Company name
- `position` - Job title
- `description` - Job description
- `start_date` - Start date
- `end_date` - End date (optional)
- `current` - Currently working flag
- `location` - Work location
- `order` - Display order

### Certification
Certifications, achievements, and participation
- `name` - Certification name
- `issuer` - Issuing organization
- `category` - Certificate/Achievement/Participation
- `issue_date` - Issue date
- `expiry_date` - Expiry date (optional)
- `credential_id` - Credential ID
- `credential_url` - Credential verification link
- `image_url` - Certificate image
- `order` - Display order

### Contact
Contact information
- `email` - Email address
- `phone` - Phone number
- `location` - Location
- `availability` - Availability status

### Message
Contact form submissions
- `name` - Sender name
- `email` - Sender email
- `subject` - Message subject
- `message` - Message content
- `read` - Read status
- `created_at` - Submission timestamp

### BlogPost
Blog posts (optional)
- `title` - Post title
- `slug` - URL slug
- `content` - Post content
- `excerpt` - Brief summary
- `published` - Published status
- `tags` - Post tags (JSON array)
- `created_at` - Creation date
- `updated_at` - Last update

### ExtraCurricularActivity
Leadership and activities
- `title` - Activity title
- `organization` - Organization name
- `role` - Your role
- `description` - Activity description
- `start_date` - Start date
- `end_date` - End date (optional)
- `current` - Currently active flag
- `achievements` - Achievements (JSON)
- `image_url` - Activity image
- `order` - Display order

---

## 🔐 Authentication

This API uses JWT (JSON Web Tokens) for authentication.

### Obtaining Token
```bash
POST /api/token/
Content-Type: application/json

{
  "username": "your_username",
  "password": "your_password"
}
```

Response:
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Using Token
```bash
GET /api/skills/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...
```

### Refreshing Token
```bash
POST /api/token/refresh/
Content-Type: application/json

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

---

## 📁 Project Structure

```
backend/
├── api/                      # Main API application
│   ├── migrations/           # Database migrations
│   ├── __init__.py
│   ├── admin.py             # Admin panel configuration
│   ├── apps.py              # App configuration
│   ├── models.py            # Database models
│   ├── serializers.py       # DRF serializers
│   ├── urls.py              # API routes
│   └── views.py             # API views
├── media/                    # User uploaded files
│   ├── certifications/       # Certificate images
│   ├── hero/                 # Profile images/videos/resumes
│   │   ├── images/
│   │   ├── videos/
│   │   └── resumes/
│   └── skills/               # Skill icons
│       └── icons/
├── portfolio_backend/        # Django project settings
│   ├── __init__.py
│   ├── asgi.py              # ASGI config
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI config
├── db.sqlite3               # SQLite database (development)
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file for sensitive configuration:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
```

### Settings Overview

Key settings in `portfolio_backend/settings.py`:

- **ALLOWED_HOSTS** - Allowed domains
- **CORS_ALLOWED_ORIGINS** - Frontend URLs for CORS
- **DATABASES** - Database configuration
- **MEDIA_ROOT** - Uploaded files location
- **MEDIA_URL** - Media files URL path
- **REST_FRAMEWORK** - DRF settings and authentication

---

## 🔧 Common Commands

### Database Management
```bash
# Create migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Reset database (development only)
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Data Management
```bash
# Export data to JSON
python manage.py dumpdata api.Skill --indent 2 > skills.json

# Import data from JSON
python manage.py loaddata skills.json

# Flush all data (CAUTION!)
python manage.py flush
```

### Server Management
```bash
# Run development server
python manage.py runserver

# Run on specific port
python manage.py runserver 8080

# Run on all interfaces
python manage.py runserver 0.0.0.0:8000
```

### Static Files
```bash
# Collect static files for production
python manage.py collectstatic --noinput
```

---

## 🧪 Testing

### Manual API Testing

Using curl:
```bash
# Get all skills
curl http://localhost:8000/api/skills/

# Get hero information
curl http://localhost:8000/api/hero/

# Submit contact form
curl -X POST http://localhost:8000/api/messages/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Test User","email":"test@example.com","subject":"Test","message":"Hello"}'
```

Using httpie:
```bash
# Get skills
http GET localhost:8000/api/skills/

# Create skill (with auth)
http POST localhost:8000/api/skills/ \
  name="Python" \
  category="language" \
  Authorization:"Bearer YOUR_TOKEN"
```

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Find process using port 8000
lsof -i :8000

# Kill the process
kill -9 <PID>

# Or run on different port
python manage.py runserver 8080
```

### Migration Errors
```bash
# Reset migrations (development only)
python manage.py migrate --fake api zero
rm api/migrations/000*.py
python manage.py makemigrations
python manage.py migrate
```

### CORS Issues
- Check `CORS_ALLOWED_ORIGINS` in settings.py
- Ensure frontend URL is listed
- Verify `django-cors-headers` is installed
- Check middleware order in settings

### Media Files Not Loading
```bash
# Check MEDIA_ROOT and MEDIA_URL in settings.py
# Ensure media files are in correct directory
# Verify file permissions
chmod -R 755 media/
```

---

## 🚀 Production Deployment

See [DEPLOY.md](../DEPLOY.md) in the root directory for detailed production deployment instructions to PythonAnywhere.

### Quick Production Checklist

- [ ] Set `DEBUG = False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use production database (MySQL/PostgreSQL)
- [ ] Set strong `SECRET_KEY`
- [ ] Configure `CORS_ALLOWED_ORIGINS` with actual frontend URL
- [ ] Set up static files serving
- [ ] Configure media files storage
- [ ] Enable HTTPS
- [ ] Set up database backups
- [ ] Configure logging

---

## 📚 API Documentation

### Example Requests

#### Get All Skills
```http
GET /api/skills/
```

Response:
```json
[
  {
    "id": 1,
    "name": "Python",
    "category": "language",
    "icon": "🐍",
    "icon_image": "http://localhost:8000/media/skills/icons/python.png",
    "order": 1
  }
]
```

#### Get Hero Information
```http
GET /api/hero/
```

Response:
```json
{
  "id": 1,
  "name": "MD HABIBULLAH MAHMUD",
  "tagline": "Full-stack Web Developer & DevOps",
  "description": "Code. Security. Infrastructure...",
  "github_url": "https://github.com/mdhabibullahmahmudncs13/",
  "linkedin_url": "https://www.linkedin.com/in/md-habibullah-mahmud-2423841a5/",
  "hackerrank_url": "https://www.hackerrank.com/profile/mdhabibullahmah1"
}
```

#### Submit Contact Form
```http
POST /api/messages/
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "subject": "Project Inquiry",
  "message": "I'd like to discuss a project..."
}
```

---

## 🤝 Contributing

This is a personal portfolio backend. If you're setting up your own:

1. Fork the repository
2. Clone your fork
3. Create a feature branch
4. Make your changes
5. Test thoroughly
6. Submit a pull request

---

## 📝 License

This project is open source and available for personal use.

---

## 🔗 Related Documentation

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [JWT Authentication](https://django-rest-framework-simplejwt.readthedocs.io/)
- [Deployment Guide](../DEPLOY.md)
- [Frontend README](../frontend/README.md)

---

**Last Updated:** December 2025
