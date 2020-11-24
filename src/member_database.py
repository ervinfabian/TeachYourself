import sqlite3



connection = sqlite3.connect('members.db')

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



##!!!!!
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
