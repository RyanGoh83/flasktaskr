from views import db
from models import Task
from datetime import date

# create new database and the db table
db.create_all()

# insert data
db.session.add(Task("Finish the tutorial", date(2017,11,15), 2, 1))
db.session.add(Task("Finish Real Python Book 2", date(2017,12,31), 10, 1))

# commit the data
db.session.commit()		
