# Smart Hotel Booking System

A Flask-based web application that allows users to register, log in, browse hotels, search and sort hotel listings, book rooms, and manage their bookings.

## Live Demo

https://smart-hotel-booking-system-b97c.onrender.com/

---

## Features

### User Management
- User Registration
- User Login
- Session-Based Authentication
- Secure Logout

### Hotel Management
- Add New Hotels
- View Available Hotels
- Search Hotels by Location
- Sort Hotels by Rating
- Sort Hotels by Price
- Sort Hotels by Available Rooms

### Booking System
- Book Hotel Rooms
- Automatic Room Availability Update
- View Booking History
- Cancel Bookings

### Database
- SQLite Database
- SQLAlchemy ORM Integration

---

## Technologies Used

- Python
- Flask
- SQLite
- SQLAlchemy
- HTML
- CSS
- Jinja2 Templates

---

## Project Structure

```text
smart-hotel-booking-system/
│
├── app.py
├── requirements.txt
├── Procfile
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add_hotel.html
│   ├── hotels.html
│   └── bookings.html
│
├── static/
│
└── instance/
    └── hotel.db
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/smart-hotel-booking-system.git
cd smart-hotel-booking-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Key Functionalities

- User Registration and Login
- Hotel Listing and Search
- Hotel Sorting
- Room Booking
- Booking History Management
- Booking Cancellation

---

## Future Enhancements

- Admin Dashboard
- Hotel Images Upload
- Online Payment Integration
- Email Notifications
- AI-Based Hotel Recommendations
- Responsive UI Design

---

## Author

Asritha Nalubala

B.Tech Computer Science Engineering

Python | Flask | SQL | Web Development

---

If you found this project useful, consider giving it a star on GitHub.
