import sqlite3



connection = sqlite3.connect('Questions.db')

# get a cursor to execute sql statemants
Cursor = connection.cursor()

#Create a table teszt
Cursor.execute( '''CREATE TABLE Questions(Question_ID INTEGER PRIMARY KEY AUTOINCREMENT,Question VARCHAR(1000),Question_answer VARCHAR(5000),FOREIGN KEY (CLASS_ID) REFERENCES Classes(CLASS_ID))''')
"""
sql = "INSERT INTO Questions(question,question_answer) VALUES ('Hany eves vagy?','Ma 18 holnaputan 22.')"
Cursor.execute(sql)

sql = "INSERT INTO Questions(question,question_answer) VALUES ('Hogy hivnak?','Tibor vagyok, orvendek.')"
Cursor.execute(sql)

sql = "INSERT INTO Questions(question,question_answer) VALUES ('Miert nem vagy Monacoban?','Megbuktam tortenelembol.')"
Cursor.execute(sql)
"""
connection.commit()


def show_questions():
    Cursor.execute("Select * from Questions")
    rows = Cursor.fetchall()
    for row in rows:
        print(row)
