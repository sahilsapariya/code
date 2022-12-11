import sqlite3

connection = sqlite3.connect("C:\\Users\\jsk\\Desktop\\school project\\code\\code\\database.db")

with open("C:\\Users\\jsk\\Desktop\\school project\\code\\code\\schema.sql") as f:
    connection.executescript(f.read())

cur = connection.cursor()
cur.execute("INSERT INTO userlist (_name, _password, isAdmin) VALUES(?, ?, ?)", ('sahil', '12', 0))
cur.execute("INSERT INTO userlist (_name, _password, isAdmin) VALUES(?, ?, ?)", ('dipti', '45', 1))
cur.execute("INSERT INTO adminprofile (a_fname, a_mname, a_lname, gender, birthdate, permenent_id, cast_catagory) VALUES(?, ?, ?, ?, ?, ?, ?)", ('dipti', 'Ashvinbhai', 'Sapariya', 'Female', '01/05/1981', '18CETT120', 'OPEN'))

connection.commit()
connection.close()

