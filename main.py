from flask import Flask
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from wtforms import StringField
from wtforms.validators import DataRequired
import os

# Initializing flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '14Ab3rhsv0z1nfiDzbv0an12jazf01nrPvijf321'


# Initializing database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
db = SQLAlchemy()
db.init_app(app)

# TODO: Create login manager and user loading


# TODO: Create user classes and database
class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[String] = mapped_column(String, nullable=False)
    email: Mapped[String] = mapped_column(String, nullable=False)


class SavedTrip(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    departing_city = mapped_column(String, nullable=False)
    destination_city = mapped_column(String, nullable=False)

# TODO: Create an admin only decorator

# TODO: Connect database


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return None


@app.route('/about')
def about():
    return None

# TODO: Create pages for login


# TODO:

if __name__ == "main":
    app.run(debug=True, host="0.0.0.0", port=5001)
