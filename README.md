# ConnectApp Backend

A Django-based backend application for ConnectApp, built with PostgreSQL database support and configured for both development and production environments.

## 🚀 Features

- Django 5.2.4 framework
- PostgreSQL database integration
- Environment-based configuration (development/production)
- Azure PostgreSQL database support
- Modular settings architecture

## 📋 Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.8 or higher
- PostgreSQL
- pip (Python package installer)
- Virtual environment (recommended)

## 🛠 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rallabhandissrikar/connectApp-Backend.git
   cd connectApp-Backend
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory with the following variables:
   ```properties
   # Development Database Configuration
   django_db_name_dev=your_dev_db_name
   django_db_user_dev=your_dev_db_user
   django_db_password_dev=your_dev_db_password
   django_db_host_dev=your_dev_db_host
   django_db_port_dev=5432

   # Production Database Configuration
   django-secret-key-production=your_production_secret_key
   django_db_name_prod=your_prod_db_name
   django_db_user_prod=your_prod_db_user
   django_db_password_prod=your_prod_db_password
   django_db_host_prod=your_prod_db_host
   django_db_port_prod=5432
   ```

5. **Run database migrations:**
   ```bash
   python manage.py migrate --settings=core.settings.dev
   ```

6. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser --settings=core.settings.dev
   ```

## 🚀 Running the Application

### Development Mode
```bash
python manage.py runserver --settings=core.settings.dev
```

The application will be available at `http://127.0.0.1:8000/`

### Production Mode
```bash
python manage.py runserver --settings=core.settings.production
```

## 📁 Project Structure

```
connectApp/
├── core/                    # Core Django configuration
│   ├── __init__.py
│   ├── asgi.py             # ASGI configuration
│   ├── urls.py             # URL routing
│   ├── wsgi.py             # WSGI configuration
│   └── settings/           # Environment-specific settings
│       ├── base.py         # Base settings
│       ├── dev.py          # Development settings
│       └── production.py   # Production settings
├── .env                    # Environment variables
├── .venv/                  # Virtual environment
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## 🔧 Configuration

The project uses a modular settings approach:

- **`base.py`**: Common settings shared across all environments
- **`dev.py`**: Development-specific settings (Debug=True, local database)
- **`production.py`**: Production-specific settings (Debug=False, production database)

## 📦 Dependencies

- **Django 5.2.4**: Web framework
- **psycopg 3.2.9**: PostgreSQL adapter for Python
- **python-decouple 3.8**: Environment variable management
- **asgiref 3.9.1**: ASGI utilities
- **sqlparse 0.5.3**: SQL parser

## 🗄️ Database

The application is configured to use PostgreSQL with Azure Database for PostgreSQL support. Make sure your database is properly configured and accessible.

### Database Commands

```bash
# Run migrations
python manage.py migrate --settings=core.settings.dev

# Create migrations for changes
python manage.py makemigrations --settings=core.settings.dev

# Access Django shell
python manage.py shell --settings=core.settings.dev
```

## 🔐 Security

- Environment variables are used for sensitive configuration
- Secret keys are stored in `.env` file (not committed to version control)
- Separate configurations for development and production environments

## 🚀 Deployment

For production deployment:

1. Set up your production database
2. Configure production environment variables
3. Set `DEBUG = False` in production settings
4. Configure `ALLOWED_HOSTS` appropriately
5. Use a production WSGI server like Gunicorn

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

- **Repository**: [rallabhandissrikar/connectApp-Backend](https://github.com/rallabhandissrikar/connectApp-Backend)
- **Branch**: main

## 🔧 Development Notes

- Use environment-specific settings when running Django commands
- Keep sensitive information in `.env` file
- Follow Django best practices for development
- Ensure database connectivity before running the application

---

**Happy Coding! 🎉**
