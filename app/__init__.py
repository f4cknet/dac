from flask import Flask
from app.models import db
from flask_migrate import  Migrate
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://dac:dac_qa_passw0rd@localhost:3306/dac"
app.secret_key = "1234567890abc"
db.init_app(app)
migrate = Migrate(app,db)



if __name__ == '__main__':
    app.run(debug=True)
