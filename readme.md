# Appointment Management System

## Overview
This is a Django-based Appointment Management System where:
- **Patients** can search for doctors and book appointments.
- **Doctors** can create a profile and manage their appointments.
- **Administrators** can manage users and appointments.

---

## Features
### **Patients**
✅ Search for doctors by specialization or name.  
✅ Book, view, and cancel their appointments.  

### **Doctors**
✅ Create and update their profile.  
✅ View, confirm, and cancel appointments.  

### **Administrator**
✅ Manage users (patients & doctors).  
✅ Manage all appointments.  

---

## Installation and Setup

### **1. Clone the Repository**
```sh
git clone https://github.com/yourusername/appointment-system.git
cd appointment-system
```

### **2. Create and Activate a Virtual Environment**
```sh
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate virtual environment (Linux/macOS)
venv\Scripts\activate  # Activate virtual environment (Windows)
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4. Configure the Database**
```sh
python manage.py makemigrations
python manage.py migrate
```

### **5. Create a Superuser**
```sh
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### **6. Run the Development Server**
```sh
python manage.py runserver
```
Access the app at: **http://127.0.0.1:8000/**

---

## API Endpoints

### **Authentication**
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/api/token/` | Obtain JWT token |
| POST | `/api/token/refresh/` | Refresh JWT token |

### **Doctors**
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/doctors/` | List all doctors |
| GET | `/doctors/{id}/` | Get a single doctor |
| POST | `/doctors/` | Create a new doctor |

### **Patients**
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/patients/` | List all patients |
| GET | `/patients/{id}/` | Get a single patient |
| POST | `/patients/` | Create a new patient |

### **Appointments**
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/appointments/` | List all appointments |
| GET | `/appointments/{id}/` | Get a single appointment |
| POST | `/appointments/` | Create a new appointment |
| PUT | `/appointments/{id}/` | Update an appointment |
| DELETE | `/appointments/{id}/` | Delete an appointment |

---

## Admin Panel
Visit **http://127.0.0.1:8000/admin/** to manage users and appointments.

---

## Deployment
### **Deploying to Production**
1. Set up a production database (e.g., PostgreSQL).
2. Configure `settings.py` for production.
3. Use a WSGI server like Gunicorn.

```sh
pip install gunicorn
```

4. Run the server:
```sh
gunicorn appointment_system.wsgi:application --bind 0.0.0.0:8000
```

---
---

## Contribution
Feel free to open issues and pull requests to contribute to this project.

---

## Contact
For inquiries, contact **asengondo@gmail.com**.

Happy Coding! 🚀

