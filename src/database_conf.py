import sqlite3



connection = sqlite3.connect('database.db')

# get a cursor to execute sql statemants
Cursor = connection.cursor()

#Create a table

Cursor.execute( '''CREATE TABLE IF NOT EXISTS members(member_id INTEGER PRIMARY KEY AUTOINCREMENT,NAME VARCHAR(100) NOT NULL, PASSWORD VARCHAR (100) NOT NULL,MAIL_ADDRESS VARCHAR(100) NOT NULL)''')

#sql = "INSERT INTO teszt (NAME,USERNAME) VALUES ('Maci','huba11')"
#sql = "Delete FROM teszt WHERE PID='7'"
##connection.commit()


def check_if_an_user_is_registrated():
    counter=0
    print('Hello we are the TeachYourself team, please login!')
    print('Name:')
    myname = input()
    print('Password:')
    mypass = input()

    Cursor.execute("Select name from members where name = ? and password = ?", (myname,mypass))
    rows = Cursor.fetchall()
    for row in rows:
        counter+=1
       #print(row)
    if counter>0 :
        print("Welcome back!")
    else:

        print('To use our application first you should register first! Type yes to registrate now or yes to do it later!')
        registrate_status=input()
        if registrate_status == 'yes':
            registrate_a_new_member()
        else:
            print("Have a nice day and come back later!")
            return 0




def registrate_a_new_member():
    print('Hello! Now the first step is to give us your name!')
    future_member_name = input()
    print('Hey '+ future_member_name+' second step is to give us your password!')
    future_member_password = input()
    future_member_pid = the_size_of_database() + 1
    print('At last but not least, please give us your mail address to keep in touch!')
    future_member_mail=input()
    Cursor.execute("""INSERT INTO members(member_id, NAME, PASSWORD,MAIL_ADDRESS) VALUES (?,?,?,?) """, (future_member_pid, future_member_name, future_member_password,future_member_mail))
    print('Data entered successfully.')
    connection.commit()

def the_size_of_database():
    count = 0
    Cursor.execute("Select member_id,name,password from members ")
    rows = Cursor.fetchall()
    for row in rows:
        count += 1
        print(row)

    return count

###################################################Class###############################################################
#Create a table teszt
Cursor.execute( '''CREATE TABLE IF NOT EXISTS Classes(CLASS_ID INTEGER PRIMARY KEY AUTOINCREMENT,CLASS_NAME VARCHAR(100) NOT NULL,CLASS_THEMATIC VARCHAR (100) NOT NULL,member_id INTEGER, FOREIGN KEY (member_id) REFERENCES members(member_id))''')

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




###################################################Question###############################################################

#Create a table teszt
Cursor.execute( '''CREATE TABLE Questions(Question_ID INTEGER PRIMARY KEY AUTOINCREMENT,Question VARCHAR(1000),Question_answer VARCHAR(5000),CLS_ID INTEGER, FOREIGN KEY (CLS_ID) REFERENCES Classes(CLASS_ID))''')

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

















