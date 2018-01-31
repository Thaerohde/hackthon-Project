from cs50 import SQL
from flask import  request
from flask_session import Session
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

class User_Data:
    def __init__ (self):
        # Configure CS50 Library to use SQLite database
        self.db = SQL("sqlite:///sport.db")

    def create_user(self, username, hash, email):

        return self.db.execute("INSERT INTO users (username, hash, email) VALUES(:username,:hash, :email)",
                                    username=username,hash= hash, email=email)

    def get_user_info(self, username):
        return self.db.execute("SELECT * FROM users WHERE username = :username", username=username)

    def check_user(self, email):
        return self.db.execute("SELECT * FROM users WHERE email = :email", email = email)

    def create_new_event(self, eventDate, eventPlace, eventType, eventName):
        return self.db.execute("INSERT INTO history (date, place, type, eventname) VALUES (:date, :place, :type, :eventname)",
        date = eventDate, place = eventPlace ,type = eventType, eventname = eventName)

    def get_events(self):
        return self.db.execute("SELECT eventname FROM index WHERE created")

"""db.execute("INSERT INTO history (id,name,symbol,price,shares,total) VALUES(:id,:name,:symbol, :price,:shares,:total)",
        id = session["user_id"],name = place["name"],symbol = bought, price =usd(place["price"]),shares = request.form.get("shares")"""