# Clinic Booking System

A Django-based clinic booking system for scheduling and managing appointments efficiently. This project includes a database for storing appointment details, email notifications for confirmation and alerts, and a user-friendly interface for admins and patients.

---

## Features
- Appointment scheduling and management.
- Email notifications for appointment confirmation and reminders.
- Responsive design for ease of use.
- Secure and scalable backend using Django and MySQL.

---

## Prerequisites
Before you begin, ensure you have the following installed:
- Python (>= 3.8)
- Django (>= 5.0.1)
- MySQL
- A Gmail account for email notifications.

---

## Installation Guide

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/clinic-booking-system.git
cd clinic-booking-system
```

### 2. Set Up a Virtual Environment
```bash
python -m venv env
source env/bin/activate   # On Windows, use `env\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the Database
Create a database in MySQL named `booking_system`. Update the database settings in `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'booking_system',
        'USER': 'root',
        'PASSWORD': 'your-database-password',
        'HOST': 'localhost',
    }
}
```

### 5. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser
```bash
python manage.py createsuperuser
```

### 7. Set Up Email Configuration
Add your email credentials in `settings.py` for sending notifications:
```python
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
```

Enable "Less Secure Apps" or create an **App Password** for your Gmail account to use as `EMAIL_HOST_PASSWORD`.

### 8. Add Static and Media Files
Ensure the `static` and `media` directories are properly set up:
```bash
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### 9. Run the Development Server
```bash
python manage.py runserver
```

Access the app in your browser at `http://127.0.0.1:8000`.

---

## Project Structure
- **Appointment:** Contains models, views, and templates for appointment management.
- **templates:** HTML files for the user interface.
- **static:** CSS, JavaScript, and image files.
- **media:** Uploaded files like images/documents.

---

## Additional Features
### Email Notifications
The system sends emails for:
1. **Appointment Confirmation:** Automatically sent after booking.
2. **Alerts/Reminders:** Configurable to send reminders for upcoming appointments.

You can customize the email templates in the `Appointment` app.

---

## Deployment
For production:
- Set `DEBUG = False` in `settings.py`.
- Add your domain to `ALLOWED_HOSTS`.
- Use a production-ready database like PostgreSQL.
- Configure a production email backend.

---


This README provides a step-by-step guide to set up, run, and customize the project while outlining its features and configuration requirements. Let me know if you need further adjustments!