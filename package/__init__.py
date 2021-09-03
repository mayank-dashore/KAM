from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_session import Session

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'

db = SQLAlchemy(app)
Session(app)
bcrypt = Bcrypt(app)

# this is some dummy data for development pourpouse
products = [
    {'name': "Potatoes", 'qty': 1, 'unit': "quintel", 'price': 100, 'isVerified': True, 'desc': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nesciunt sit nobis ab est voluptatum nisi non numquam earum quis praesentium.'},
    {'name': "Potatoes", 'qty': 1, 'unit': "quintel", 'price': 100, 'isVerified': True, 'desc': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nesciunt sit nobis ab est voluptatum nisi non numquam earum quis praesentium.'},
    {'name': "Potatoes", 'qty': 1, 'unit': "quintel", 'price': 100, 'isVerified': True, 'desc': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nesciunt sit nobis ab est voluptatum nisi non numquam earum quis praesentium.'},
    {'name': "Potatoes", 'qty': 1, 'unit': "quintel", 'price': 100, 'isVerified': True, 'desc': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nesciunt sit nobis ab est voluptatum nisi non numquam earum quis praesentium.'},
    {'name': "Onions", 'qty': 2, 'unit': "quintel", 'price': 200, 'isVerified': False, 'desc': 'Lorem ipsum.Lorem ipsum dolor sit ab est voluptatum nisi amet consectetur adipi dolor sit amet ur adiisicing elit. Nesciunt sit nobis ab est voluptatum nisi non numquam earum quis praesentium.'},
    {'name': "Onions", 'qty': 2, 'unit': "quintel", 'price': 200, 'isVerified': True, 'desc': 'Lorem ipsum.Lorem ipsum dolor sit ab est voluptatum nisi amet consectetur adipi dolor sit amet ur adiisicing elit. Nesciunt sit nobis ab est voluptatum nisi non numquam earum quis praesentium.'}
]

import package.routes