import sqlite3




connection = sqlite3.connect('Classes.db')

# get a cursor to execute sql statemants
Cursor = connection.cursor()

#Create a table teszt
Cursor.execute( '''CREATE TABLE Classes(CLASS_ID INTEGER PRIMARY KEY AUTOINCREMENT,CLASS_NAME VARCHAR(100) NOT NULL,CLASS_THEMATIC VARCHAR (100) NOT NULL, FOREIGN KEY (member_id) REFERENCES members(member_id))''')

###connection.commit()


##sql = "INSERT INTO Classes(CLASS_NAME,CLASS_THEMATIC) VALUES ('Szamtech3','Phyton')"
##Cursor.execute(sql)
##sql = "INSERT INTO Classes(CLASS_NAME,CLASS_THEMATIC) VALUES ('Szamtech3','Numerikus')"
##Cursor.execute(sql)
##sql = "INSERT INTO Classes(CLASS_NAME,CLASS_THEMATIC) VALUES ('Szamtech3','Oprendszerek1')"
##Cursor.execute(sql)
##connection.commit()

def registrate_a_new_Class():
    print("Give us the name of the Class you would like to create: ")
    future_class_name = input()
    print('Now what is the thematic of the '+future_class_name+' named class! This select it below!')
    future_class_thematic = input()
    Cursor.execute("""INSERT INTO Classes( CLASS_NAME, CLASS_THEMATIC) VALUES (?,?) """, (future_class_name, future_class_thematic))
    print('Data entered successfully.')
    connection.commit()


def show_our_database():
    Cursor.execute("Select class_id,class_name,class_thematic from Classes order by class_thematic")
    rows = Cursor.fetchall()
    for row in rows:
        print(row)

def search_a_class_by_its_name():
    counter=0
    print("Type the name of the Class you are searching for!")
    class_tehem_example=input()
    Cursor.execute("Select class_id,class_name,class_thematic from Classes where class_thematic = ?",(class_tehem_example,))
    rows = Cursor.fetchall()
    for row in rows:
        counter=counter+1
        print(row)
    if counter ==0:
        print("There is no class with this thematic! Would like to create one? If you want type yes!")
    answer=input()
    if answer == "yes":
        registrate_a_new_Class()
    else:
        return 0

