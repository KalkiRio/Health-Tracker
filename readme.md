#Note: This project is under redevelopment and is being updated for better look and feel, if you want to contribute feel free to do so, Thanks.

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
├── Procfile                    # For Heroku deployment
├── runtime.txt                 # Python version for deployment
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
│   │   ├── serializers.py      # For API endpoints
│   │   └── migrations/
│   ├── tracker/                # Core health tracking
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── utils.py            # Helper functions
│   │   └── migrations/
│   ├── medical/                # Medical records & documents
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── utils.py            # File handling utilities
│   │   └── migrations/
│   ├── medicines/              # Medicine & prescription tracking
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── tasks.py            # For medication reminders
│   │   └── migrations/
│   └── dashboard/              # Dashboard and analytics
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       └── migrations/
├── templates/                  # HTML templates
│   ├── base.html
│   ├── registration/
│   │   ├── login.html
│   │   ├── register.html
│   │   └── profile.html
│   ├── tracker/
│   │   ├── dashboard.html
│   │   ├── add_weight.html
│   │   ├── add_exercise.html
│   │   ├── add_meal.html
│   │   └── goals.html
│   ├── medical/
│   │   ├── medical_profile.html
│   │   ├── upload_report.html
│   │   ├── reports_list.html
│   │   └── report_detail.html
│   ├── medicines/
│   │   ├── medicine_list.html
│   │   ├── add_medicine.html
│   │   ├── prescription_upload.html
│   │   └── medication_schedule.html
│   └── includes/
│       ├── navbar.html
│       ├── sidebar.html
│       └── footer.html
├── static/                     # Static files
│   ├── css/
│   │   ├── style.css
│   │   ├── themes.css
│   │   └── responsive.css
│   ├── js/
│   │   ├── main.js
│   │   ├── charts.js
│   │   ├── theme-toggle.js
│   │   └── dashboard.js
│   ├── images/
│   │   ├── logo.png
│   │   └── default-avatar.png
│   └── vendors/                # Third-party libraries
│       ├── bootstrap/
│       ├── chart.js/
│       └── fontawesome/
├── media/                      # User uploaded files
│   ├── profile_pics/
│   ├── medical_reports/
│   │   ├── lab_reports/
│   │   ├── prescriptions/
│   │   ├── xrays/
│   │   └── other_documents/
│   └── medicine_images/
└── tests/                      # Test files
    ├── __init__.py
    ├── test_models.py
    ├── test_views.py
    └── test_forms.py
```

1. **Environment Setup**
   - Create virtual environment
   - Install Django and dependencies
   - Setup project structure
   - Configure settings for development/production

2. **User Authentication System**
   - Custom User model with health profile
   - Registration and login functionality
   - User profile management
   - Password reset functionality

3. **Basic UI Framework**
   - Create base templates
   - Implement responsive design with CSS Grid/Flexbox
   - Add theme toggle functionality
   - Setup static files handling

1. **Production Preparation**
   - Environment variables setup
   - Database migration scripts
   - Static files configuration
   - Security settings

2. **Deployment**
   - Heroku deployment setup
   - Database configuration
   - Domain and SSL setup
   - Performance optimization

## 🔧 Technology Stack

**Backend:**
- Django 5.0 +
- Django REST Framework (for API endpoints)
- PostgreSQL (production) / SQLite (development)
- Pillow (image handling)

**Frontend:**
- HTML5, CSS3, JavaScript (ES6+)
- Bootstrap 5 (responsive framework)
- Chart.js (data visualization)
- Font Awesome (icons)

**Deployment:**
- Heroku (free tier)
- WhiteNoise (static files)
- Gunicorn (WSGI server)

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
- Python 3.9+
- pip
- Git

### Installation Steps
```bash
# Clone the repository
git clone https://github.com/KalkiRio/Health-Tracker.git
cd healthtracker

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
# Edit .env with your configuration

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run development server
python manage.py runserver
```

## 🧪 Testing

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test apps.tracker

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

## 📚 API Documentation

The application includes RESTful API endpoints for:
- User authentication
- Health data CRUD operations
- Dashboard analytics
- Data export

API documentation available at `/api/docs/` when running the server.

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
- Rate limiting
- Input validation and sanitization

## 📈 Performance Optimization

- Database query optimization
- Static file compression
- Lazy loading for images
- Caching strategies
- Minified CSS/JS

## 🚀 Deployment Guide

### Heroku Deployment

1. **Prepare for Deployment**
   ```bash
   # Install Heroku CLI
   # Create Procfile and runtime.txt
   ```

2. **Create Heroku App**
   ```bash
   heroku create your-healthtracker-app
   heroku config:set DEBUG=False
   heroku config:set SECRET_KEY=your-secret-key
   ```

3. **Deploy**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push heroku main
   heroku run python manage.py migrate
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

For questions or issues, please open an issue on GitHub or contact "ribhuroy@outlook.com" .

---

**Built with ❤️ using Django**
