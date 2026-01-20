# Portfolio Website

A dynamic, full-stack portfolio website built with **Django** and **Bootstrap**. This project allows you to manage and showcase your professional portfolio, projects, skills, education, and experience through an intuitive admin dashboard.

## Features

✨ **Core Functionality:**
- 📱 **Responsive Design** - Mobile-first approach with Bootstrap framework
- 🎨 **Dynamic Content Management** - Easily update your portfolio content via admin dashboard
- 📄 **Resume Management** - Upload and manage your resume
- 💼 **Project Showcase** - Display your projects with descriptions and tech stack
- 📚 **Skills & Experience** - Highlight your technical skills and professional experience
- 🎓 **Education Timeline** - Showcase your educational background
- 💬 **Contact Form** - Allow visitors to send you messages
- 🔐 **User Authentication** - Secure login and registration system
- 🎯 **SEO-Friendly** - Built with best practices for search engine optimization

## Tech Stack

**Backend:**
- Django 4.2
- SQLite (development)
- Python 3.x

**Frontend:**
- Bootstrap 5
- HTML5, CSS3, JavaScript
- Responsive Design with AOS animations

**Additional Libraries:**
- Glightbox (image lightbox)
- Isotope (portfolio filtering)
- Typed.js (text animation)
- Swiper (carousel)

## Project Structure

```
portfolio/
├── backend/                 # Django app for admin functionality
│   ├── models.py           # Database models (HomeContent, Skill, Project, etc.)
│   ├── views.py            # Backend views and logic
│   ├── urls.py             # URL routing for backend
│   ├── templates/          # Admin templates
│   └── migrations/         # Database migrations
├── frontend/               # Django app for public website
│   ├── views.py           # Frontend views
│   ├── templates/         # Public-facing templates
│   └── static/            # CSS, JS, and images
├── myproject/             # Django project settings
│   ├── settings.py        # Project configuration
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI application
├── media/                 # Uploaded files (resumes, projects)
├── Craftivo/              # Template assets folder
├── db.sqlite3             # Development database
└── manage.py              # Django management script
```

## Database Models

**HomeContent** - Your personal information and profile
- Name, Role, Location, Email, Phone
- About Me sections
- Resume file upload

**Skill** - Technical and professional skills

**Experience** - Work experience and internships

**Education** - Educational background and degrees

**Project** - Portfolio projects with descriptions and tech stack

**ContactMessage** - Messages received from contact form

**User** - User accounts for authentication

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd portfolio
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install django
   ```

5. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Frontend: http://127.0.0.1:8000/
   - Admin Dashboard: http://127.0.0.1:8000/backend/
   - Django Admin: http://127.0.0.1:8000/admin/

## Usage

### Managing Your Portfolio

1. **Login to Admin Dashboard**
   - Navigate to http://127.0.0.1:8000/backend/ and log in with your credentials

2. **Update Personal Information**
   - Edit your name, role, and professional summary
   - Add your profile photo and resume

3. **Add Skills**
   - List all your technical and professional skills

4. **Showcase Projects**
   - Add project titles, descriptions, technologies used, and links

5. **Document Experience**
   - Add your work experience with company, position, duration, and description

6. **List Education**
   - Add your educational qualifications and institutions

7. **Monitor Contact Messages**
   - View and manage messages received from your website visitors

## Customization

### Frontend Customization
- Edit templates in `frontend/templates/` to change layout and styling
- Modify CSS in `frontend/static/assets/css/main.css`
- Update JavaScript in `frontend/static/assets/js/main.js`

### Backend Configuration
- Update `myproject/settings.py` for project-wide settings
- Add new Django apps in the `INSTALLED_APPS` list

## Deployment

For production deployment:

1. Set `DEBUG = False` in `settings.py`
2. Configure `ALLOWED_HOSTS` with your domain
3. Use a production database (PostgreSQL recommended)
4. Configure a web server (Gunicorn, uWSGI)
5. Use a reverse proxy (Nginx)
6. Set up HTTPS/SSL
7. Migrate to a production-grade server

Popular deployment options:
- Heroku
- PythonAnywhere
- AWS (EC2, Elastic Beanstalk)
- DigitalOcean
- Azure App Service

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or suggestions, please open an issue in the repository or contact via the website's contact form.

## Author

**Aswin PS**  
B.Tech Graduate in Information Technology  
Python & Django Developer  

- GitHub: https://github.com/aswinps11  
- LinkedIn: https://www.linkedin.com/in/aswinps11/


---

**Happy Portfolio Building! 🚀**
