# HealthTracker - Personal Health Management System

## 🎯 Project Overview

HealthTracker is a comprehensive web application built with Django that helps users monitor and manage their health metrics, including weight tracking, exercise logging, meal planning, and health goal setting. The application features a modern, responsive UI with both light and dark themes.

## ✨ Key Features

- **User Authentication & Profiles**: Secure registration, login, and personalized dashboards
- **Medical Profile Management**: Blood group, allergies, medical conditions, emergency contacts
- **Health Metrics Tracking**: Weight, BMI, blood pressure, heart rate, glucose levels
- **Medical Reports**: Upload, download, and organize medical documents (PDFs, images)
- **Medicine & Prescription Tracking**: Medication schedules, dosage reminders, prescription management
- **Exercise & Activity Logging**: Workout tracking with duration, calories burned, and exercise types
- **Nutrition Management**: Meal logging, calorie tracking, and nutritional information
- **Goal Setting & Progress**: Set health goals and track progress with visual charts
- **Data Visualization**: Interactive charts and graphs for health trends
- **Document Management**: Secure file storage with categorization and search
- **Responsive Design**: Mobile-first approach with light/dark theme toggle
- **Export Functionality**: Export health data and medical summaries as PDF reports

## 🏗️ Project Structure

```
healthtracker/
├── manage.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
├── .replit                     # Replit configuration
├── render.yaml                 # Render deployment config
├── healthtracker/              # Main project directory
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/                       # Custom apps directory
│   ├── __init__.py
│   ├── accounts/               # User management & medical profiles
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── tests.py
│   │   └── migrations/
│   ├── tracker/                # Core health tracking
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── tests.py
│   │   └── migrations/
│   ├── medical/                # Medical records & documents
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── tests.py
│   │   └── migrations/
│   ├── medicines/              # Medicine & prescription tracking
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── tests.py
│   │   └── migrations/
│   └── dashboard/              # Dashboard and analytics
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       ├── tests.py
│       └── migrations/
├── templates/                  # HTML templates
│   ├── base.html
│   ├── registration/
│   │   ├── login.html
│   │   └── register.html
│   └── dashboard/
│       └── dashboard.html
├── static/                     # Static files
│   ├── css/
│   │   ├── style.css
│   │   └── themes.css
│   └── js/
│       ├── main.js
│       └── theme-toggle.js
├── media/                      # User uploaded files
│   ├── profile_pics/
│   ├── medical_reports/
│   │   ├── lab_reports/
│   │   ├── prescriptions/
│   │   ├── xrays/
│   │   └── other_documents/
│   └── medicine_images/
└── attached_assets/            # Project documentation
```

## 🔧 Technology Stack

**Backend:**
- Django 5.2.3
- PostgreSQL (production) / SQLite (development)
- Pillow (image handling)
- python-decouple (environment management)
- dj-database-url (database configuration)

**Frontend:**
- HTML5, CSS3, JavaScript (ES6+)
- Bootstrap 5 (responsive framework)
- Font Awesome (icons)
- Chart.js (data visualization)

**Deployment:**
- Render (cloud hosting)
- Gunicorn (WSGI server)
- PostgreSQL (production database)

**Development:**
- Replit (online IDE)
- SQLite (development database)

## 📊 Database Models Overview

### User Profile (Extended)
- Extended Django User model
- Height, weight, age, activity level
- Blood group, allergies, medical conditions
- Emergency contact information
- Health goals and preferences
- Profile picture

### Medical Profile
- Blood group (A+, B+, O+, etc.)
- Known allergies and reactions
- Chronic conditions
- Emergency contacts
- Insurance information
- Preferred hospitals/doctors

### Medical Report
- User (ForeignKey)
- Report type (Lab, X-ray, Prescription, etc.)
- Upload date
- File (PDF/Image)
- Description/notes
- Doctor/clinic information
- Report date

### Medicine Entry
- User (ForeignKey)
- Medicine name
- Dosage and frequency
- Start date, end date
- Prescription image (optional)
- Doctor prescribed
- Notes and side effects

### Weight Entry
- User (ForeignKey)
- Weight value
- Date recorded
- Notes (optional)

### Vital Signs Entry
- User (ForeignKey)
- Blood pressure (systolic/diastolic)
- Heart rate
- Blood glucose
- Temperature
- Date recorded

### Exercise Entry
- User (ForeignKey)
- Exercise type
- Duration
- Calories burned
- Date performed

### Meal Entry
- User (ForeignKey)
- Meal name
- Calories
- Meal type (breakfast, lunch, dinner, snack)
- Date consumed

### Health Goal
- User (ForeignKey)
- Goal type (weight loss, muscle gain, etc.)
- Target value
- Target date
- Current progress

## 🚀 Getting Started

### Prerequisites
- Python 3.12+
- pip
- Git

### Installation Steps

#### Option 1: Replit (Recommended)
1. Fork this repository on Replit
2. The environment will be automatically configured
3. Run the project using the Run button

#### Option 2: Local Development
```bash
# Clone the repository
git clone https://github.com/your-username/healthtracker.git
cd healthtracker

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
# Edit .env with your configuration

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver 0.0.0.0:3000
```

## 🧪 Testing

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test apps.tracker

# Run with coverage (if coverage is installed)
coverage run --source='.' manage.py test
coverage report
```

## 🎨 Design System

### Color Palette
**Light Theme:**
- Primary: #007bff
- Secondary: #6c757d
- Success: #28a745
- Background: #ffffff

**Dark Theme:**
- Primary: #0d6efd
- Secondary: #6c757d
- Success: #20c997
- Background: #121212

### Typography
- Headers: 'Poppins', sans-serif
- Body: 'Inter', sans-serif
- Code: 'Fira Code', monospace

## 🔒 Security Features

- CSRF protection
- SQL injection prevention
- XSS protection
- Secure password hashing
- Input validation and sanitization
- Environment-based configuration

## 📈 Performance Optimization

- Database query optimization
- Static file compression
- Lazy loading for images
- Minified CSS/JS

## 🚀 Deployment Guide

### Render Deployment

1. **Prepare for Deployment**
   - Ensure `render.yaml` is configured
   - Set up environment variables
   - Configure database settings

2. **Deploy to Render**
   ```bash
   # Connect your GitHub repository to Render
   # Render will automatically detect render.yaml
   # Set environment variables in Render dashboard:
   # - SECRET_KEY (generate a secure key)
   # - DEBUG=False
   # - ALLOWED_HOSTS=*
   ```

3. **Database Setup**
   - Render will automatically create PostgreSQL database
   - Database URL will be injected as environment variable
   - Migrations will run automatically during build

4. **Static Files**
   - Static files are collected during build process
   - Served directly by the Django application

### Environment Variables
Create a `.env` file with:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
DATABASE_URL=  # Leave empty for SQLite in development
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For questions or issues, please open an issue on GitHub or contact "ribhuroy@outlook.com".

---

**Built with ❤️ using Django and deployed on Render**