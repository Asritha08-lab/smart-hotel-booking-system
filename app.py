from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "hotel_secret_key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hotel.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# User Table

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))


class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    rating = db.Column(db.Integer)
    price = db.Column(db.Integer)
    rooms = db.Column(db.Integer)


# ADD THIS HERE
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer)

    hotel_id = db.Column(db.Integer)

    hotel_name = db.Column(db.String(100))

    username = db.Column(db.String(100))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        user = User(
            name=name,
            email=email,
            password=password
        )

        db.session.add(user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(
            email=email,
            password=password
        ).first()

        
        if user:
            session["user_id"] = user.id
            session["user_name"] = user.name

            return redirect("/dashboard")

        return "Invalid Email or Password"

    return render_template("login.html")



@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect("/login")

    return render_template(
        "dashboard.html",
        username=session["user_name"]
    )
@app.route("/add_hotel", methods=["GET", "POST"])
def add_hotel():

    if request.method == "POST":

        hotel = Hotel(
            name=request.form["name"],
            location=request.form["location"],
            rating=request.form["rating"],
            price=request.form["price"],
            rooms=request.form["rooms"]
        )

        db.session.add(hotel)
        db.session.commit()

        return redirect("/hotels")

    return render_template("add_hotel.html")

@app.route("/hotels")
def hotels():

    location = request.args.get("location")
    sort = request.args.get("sort")

    query = Hotel.query

    if location:
        query = query.filter(
            Hotel.location.ilike(f"%{location}%")
        )

    if sort == "rating":
        query = query.order_by(
            Hotel.rating.desc()
        )
    elif sort == "price":
        query = query.order_by(
            Hotel.price.asc()
        )

    elif sort == "rooms":
        query = query.order_by(
            Hotel.rooms.desc()
    )
        


    all_hotels = query.all()

    return render_template(
        "hotels.html",
        hotels=all_hotels
    )

@app.route("/my_bookings")
def my_bookings():

    if "user_id" not in session:
        return redirect("/login")

    bookings = Booking.query.filter_by(
        user_id=session["user_id"]
    ).all()

    return render_template(
        "bookings.html",
        bookings=bookings
    )

@app.route("/book/<int:hotel_id>")
def book_hotel(hotel_id):

    if "user_id" not in session:
        return redirect("/login")

    hotel = Hotel.query.get(hotel_id)

    if hotel.rooms <= 0:
        return "No Rooms Available"

    booking = Booking(
        user_id=session["user_id"],
        username=session["user_name"],
        hotel_id=hotel.id,
        hotel_name=hotel.name
    )

    hotel.rooms -= 1

    db.session.add(booking)
    db.session.commit()

    return redirect("/my_bookings")


@app.route("/cancel_booking/<int:booking_id>")
def cancel_booking(booking_id):

    booking = Booking.query.get(booking_id)

    hotel = Hotel.query.get(booking.hotel_id)

    hotel.rooms += 1

    db.session.delete(booking)
    db.session.commit()

    return redirect("/my_bookings")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)