import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
	c = connection.cursor()
	
	c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY 
		AUTOINCREMENT, name TEXT NOT NULL, due_date TEXT NOT NULL,
		priority INTEGER NOT NULL, status INTEGER NOT NULL)""")
		
	c.execute('INSERT INTO tasks(name, due_date, priority, status)'
		'VALUES("Finish tutorial", "5/5/2017", 10, 1)')
	
	c.execute('INSERT INTO tasks(name, due_date, priority, status)'
		'VALUES("Buy food", "14/5/2017", 20, 1)')
		
	c.execute('INSERT INTO tasks(name, due_date, priority, status)'
		'VALUES("Drink water", "21/5/2017", 10, 0)')
		
