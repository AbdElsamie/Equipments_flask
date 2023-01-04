from flaskext.mysql import MySQL

from app import app

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'jobsdb'  # the name of your database
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
