# Coffee Shop E-commerce Platform

A Django-based e-commerce web application for a coffee shop, featuring product management, user authentication, and order processing capabilities.

🌐 Demo in live
Visit the app web: https://coffeeshop-production-87be.up.railway.app

## 🚀 Features

- **User Authentication System**
  - User registration, login, and logout
  - Secure password handling with Django's built-in authentication
  
- **Product Management**
  - Full CRUD operations for products
  - Product catalog with images
  - Product availability tracking
  - Automatic timestamp tracking for product creation

- **Order Management**
  - Shopping cart functionality
  - Order processing system
  - Order-product relationship tracking

- **REST API**
  - RESTful API endpoints for product data
  - JSON serialization with Django REST Framework
  - API endpoints for creating and listing products

- **Modern UI**
  - Responsive design with Tailwind CSS
  - Template inheritance with Django's template system
  - Dynamic form handling with django-widget-tweaks and django-crispy-forms

## 🛠️ Tech Stack

**Backend:**
- Python 3.10.12
- Django 5.2
- Django REST Framework
- PostgreSQL

**Frontend:**
- HTML5
- Tailwind CSS
- Django Templates

**Deployment:**
- Gunicorn (WSGI HTTP Server)
- Railway (Database & Application Hosting)

## 📋 Prerequisites

- Python 3.10 or higher
- PostgreSQL
- pip (Python package manager)
- Virtual environment (recommended)

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/JarolGabriel/coffee_shop
cd coffee_shop
```

### 2. Create and activate virtual environment

```bash
python -m venv venv

# On Linux/Mac
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file in the project root with the following variables:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
PGDATABASE=your_database_name
PGUSER=your_database_user
PGPASSWORD=your_database_password
PGHOST=your_database_host
PGPORT=5432
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Visit `http://localhost:8000` to view the application.

## 📁 Project Structure

```
coffee_shop/
├── coffee_shop/          # Project configuration
│   ├── settings.py       # Django settings
│   ├── urls.py           # Root URL configuration
│   └── wsgi.py           # WSGI configuration
├── products/             # Products app
│   ├── models.py         # Product model
│   ├── views.py          # Product views
│   ├── serializers.py    # DRF serializers
│   ├── urls.py           # Product URLs
│   └── templates/        # Product templates
├── users/                # User authentication app
│   ├── views.py          # Auth views
│   ├── urls.py           # Auth URLs
│   └── templates/        # Auth templates
├── orders/               # Orders app
│   ├── models.py         # Order models
│   ├── views.py          # Order views
│   └── urls.py           # Order URLs
├── templates/            # Global templates
│   └── base.html         # Base template
├── media/                # User-uploaded files
├── staticfiles/          # Collected static files
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
├── Procfile              # Deployment configuration
└── runtime.txt           # Python version specification
```

## 🗄️ Database Schema

### Product Model
- `name` - Product name
- `price` - Product price (Decimal)
- `description` - Product description (Text)
- `photo` - Product image (ImageField)
- `available` - Availability status (Boolean)
- `created_at` - Creation timestamp (Auto)

### Order & OrderProduct Models
- Order tracking with user relationships
- Many-to-many relationship between orders and products
- Quantity tracking per product in an order

## 🔌 API Endpoints

```
GET  /api/                    # List all products (JSON)
POST /api/products/create/    # Create a new product (JSON)
```

## 🎨 Key Features Implementation

### Template Inheritance
The project uses Django's template inheritance system with a `base.html` template that includes:
- Tailwind CSS integration
- Responsive navigation
- Consistent styling across all pages

### Form Handling
- Integration with `django-widget-tweaks` for flexible form rendering
- `django-crispy-forms` for enhanced form styling
- CSRF protection on all forms

### Media File Management
- Configured media file handling for product images
- Automatic URL generation for uploaded files

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

## 🚀 Deployment

The application is configured for deployment on Railway with:
- Gunicorn as the production WSGI server
- PostgreSQL database
- Environment-based configuration
- Static file collection support

### Deploy to Railway

1. Push your code to GitHub
2. Connect your repository to Railway
3. Add environment variables in Railway dashboard
4. Railway will automatically detect Django and deploy

## 📝 Development Notes

- The project uses PostgreSQL in production (Railway) and can use SQLite for local development
- All database credentials are managed through environment variables
- Static files are collected to `staticfiles/` directory for production
- Media files are stored in `media/` directory

## 🔐 Security

- Secret key managed through environment variables
- DEBUG mode disabled in production
- CSRF protection enabled
- Secure password hashing with Django's authentication system

## 👨‍💻 Author

Jarol Gabriel - Full-Stack Developer in training
- Learning path: JavaScript/Node.js → PostgreSQL → Python → Django → DRF → Next.js

## 📄 License

This project is part of a Django course and is for educational purposes.

## 🙏 Acknowledgments

- Django documentation
- Django REST Framework
- Tailwind CSS
- Railway for hosting solutions# Force redeploy
