import sqlite3

conn = sqlite3.connect('db.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   username TEXT,
   name TEXT,
   admin BOOL);
""")
conn.commit()


def insert(user_id: int, user_name: str, name: str, admin: bool):
	cur.execute('INSERT INTO users (userid, username, name, admin) VALUES (?, ?, ?, ?)', (user_id, user_name, name, admin))
	conn.commit()


def select(id):
	result = cur.execute('SELECT * FROM users WHERE userid = ?', (id,))
	for i in result:
		return len(i) > 0


# if __name__ == '__main__':
# 	insert_mes(725455605, 111, datetime.time)



