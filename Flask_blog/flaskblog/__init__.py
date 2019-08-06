
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)
app.config["SECRET_KEY"]="bfcde87158a097d9f35eb296443340f1"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)
b_c=Bcrypt(app)
l_manager=LoginManager(app)
l_manager.login_view='login'
l_manager.login_message_category='info'


from flaskblog import routes