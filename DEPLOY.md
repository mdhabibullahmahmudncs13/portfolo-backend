# Deploying Django Portfolio Backend on PythonAnywhere

This guide walks you through deploying your Django portfolio backend on PythonAnywhere.

## Prerequisites

- A PythonAnywhere account (free or paid)
- Your project code in a Git repository (GitHub, GitLab, etc.)

## Step 1: Create a PythonAnywhere Account

1. Go to [https://www.pythonanywhere.com](https://www.pythonanywhere.com)
2. Sign up for an account (Beginner account is free)
3. Verify your email address

## Step 2: Clone Your Repository

1. Open a **Bash console** from your PythonAnywhere dashboard
2. Clone your repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
   ```

## Step 3: Create a Virtual Environment

```bash
mkvirtualenv --python=/usr/bin/python3.10 portfolio-env
```

Or if you prefer using venv:
```bash
python3.10 -m venv venv
source venv/bin/activate
```

## Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 5: Configure Environment Variables

1. Create a `.env` file in your project root:
   ```bash
   nano .env
   ```

2. Add the following configuration:
   ```env
   SECRET_KEY=your-super-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=yourusername.pythonanywhere.com
   CORS_ALLOWED_ORIGINS=https://your-frontend-domain.com,https://www.your-frontend-domain.com
   ```

3. Generate a new SECRET_KEY:
   ```bash
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```

## Step 6: Database Setup

1. Run migrations:
   ```bash
   python manage.py migrate
   ```

2. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

3. Collect static files:
   ```bash
   python manage.py collectstatic --noinput
   ```

## Step 7: Configure PythonAnywhere Web App

1. Go to the **Web** tab in your PythonAnywhere dashboard
2. Click **Add a new web app**
3. Choose **Manual configuration** (not Django wizard)
4. Select **Python 3.10** (or your preferred version)

### Configure Source Code Path

Set the source code directory to:
```
/home/yourusername/YOUR_REPO_NAME
```

### Configure Virtual Environment

Set the virtualenv path to:
```
/home/yourusername/.virtualenvs/portfolio-env
```

Or if using venv:
```
/home/yourusername/YOUR_REPO_NAME/venv
```

### Configure WSGI File

1. Click on the **WSGI configuration file** link
2. Delete all content and replace with:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/yourusername/YOUR_REPO_NAME'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variable for Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio_backend.settings'

# Load environment variables from .env file
from pathlib import Path
env_path = Path('/home/yourusername/YOUR_REPO_NAME/.env')
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ.setdefault(key, value)

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Important:** Replace `yourusername` and `YOUR_REPO_NAME` with your actual values.

## Step 8: Configure Static and Media Files

1. In the **Web** tab, scroll to the **Static files** section
2. Add the following mappings:

   | URL          | Directory                                              |
   |--------------|--------------------------------------------------------|
   | /static/     | /home/yourusername/YOUR_REPO_NAME/staticfiles         |
   | /media/      | /home/yourusername/YOUR_REPO_NAME/media               |

## Step 9: Set Up HTTPS (Free accounts get HTTPS automatically)

PythonAnywhere provides free HTTPS for `*.pythonanywhere.com` domains. Your site will be available at:
```
https://yourusername.pythonanywhere.com
```

## Step 10: Reload Your Web App

1. Go to the **Web** tab
2. Click the green **Reload** button
3. Your application should now be live!

## Step 11: Test Your Deployment

Visit your endpoints:
- Admin panel: `https://yourusername.pythonanywhere.com/admin/`
- API: `https://yourusername.pythonanywhere.com/api/`

## Updating Your Application

When you make changes to your code:

1. Open a Bash console
2. Navigate to your project:
   ```bash
   cd YOUR_REPO_NAME
   ```
3. Pull the latest changes:
   ```bash
   git pull
   ```
4. Activate virtual environment:
   ```bash
   workon portfolio-env
   ```
5. Install any new dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Run migrations if needed:
   ```bash
   python manage.py migrate
   ```
7. Collect static files:
   ```bash
   python manage.py collectstatic --noinput
   ```
8. Reload the web app from the **Web** tab

## Troubleshooting

### Check Error Logs

1. Go to the **Web** tab
2. Click on the **Error log** and **Server log** links
3. Look for Python tracebacks and error messages

### Common Issues

**Issue: 502 Bad Gateway**
- Check your WSGI file configuration
- Verify all paths are correct
- Check error logs

**Issue: Static files not loading**
- Verify static files mappings in Web tab
- Ensure `collectstatic` was run successfully
- Check STATIC_ROOT in settings.py

**Issue: Database errors**
- Ensure migrations were run
- Check database file permissions
- SQLite database should be in a writable directory

**Issue: Import errors**
- Verify virtual environment is activated
- Check all dependencies are installed
- Ensure python-decouple is installed

**Issue: CORS errors**
- Update CORS_ALLOWED_ORIGINS in .env
- Ensure your frontend domain is listed
- Include both with and without 'www' if applicable

### Debug Mode

To enable debug mode temporarily:
1. Edit `.env` file: `DEBUG=True`
2. Reload web app
3. **Remember to set `DEBUG=False` in production!**

## Important Notes

- **Free tier limitations**: 
  - CPU usage limits
  - Daily quota for outgoing internet connections
  - Your app sleeps after inactivity (wakes on first request)
  
- **Database**: SQLite works fine for small projects, but consider upgrading to MySQL for production (available on paid plans)

- **Media files**: On free accounts, uploaded media persists but has storage limits

- **Custom domain**: Available on paid plans only

- **Always keep DEBUG=False in production**

- **Regularly backup your database and media files**

## Security Checklist

- ✅ SECRET_KEY is unique and secret
- ✅ DEBUG is set to False
- ✅ ALLOWED_HOSTS is configured correctly
- ✅ CORS_ALLOWED_ORIGINS includes only your frontend domains
- ✅ Database has a strong admin password
- ✅ .env file is not committed to Git (add to .gitignore)

## Additional Resources

- [PythonAnywhere Help Pages](https://help.pythonanywhere.com/)
- [Deploying Django on PythonAnywhere](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/)
- [PythonAnywhere Forums](https://www.pythonanywhere.com/forums/)

---

Your Django portfolio backend should now be successfully deployed on PythonAnywhere! 🚀
