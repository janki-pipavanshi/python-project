from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

app.secret_key='sessionData'

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3306/pythondb'

app.config['SQLAlchemy_MAX_OVERFLOW'] = 0

db= SQLAlchemy(app)

import base.com.controller