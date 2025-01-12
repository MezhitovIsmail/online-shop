import os

PER_PAGE = 4
SECRET_KEY = os.environ.get('SECRET_KEY') or '46b74dc7229cda8e0de864283dd32b07ed850f59f97aa1e209fedabf28c81283'

#SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://std_2438_game:12345678@std-mysql.ist.mospolytech.ru/std_2438_game'
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:admin@db:5432/shop'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media', 'images')

