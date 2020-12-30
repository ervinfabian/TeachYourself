import sqlite3


class Database():
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        # get a cursor to execute sql statements
        self.Cursor = self.connection.cursor()
        # self.Cursor.execute(
        #      'CREATE TABLE IF NOT EXISTS classes(class_name VARCHAR(100) PRIMARY KEY NOT NULL, username Varchar(100), FOREIGN KEY (username) REFERENCES members(users))')
        #
        # self.test1()
        # self.test2()
        self.counter = 0
        self.classname = ''
        self.all_classes = []
        self.own_classes = []
        self.Cursor.execute("Select class_name from classes")
        rows = self.Cursor.fetchall()
        for row in rows:
            self.all_classes.append(row[0])
        self.connection.commit()
        print(self.all_classes)

    def check_if_an_user_is_registered(self, name, password):
        counter = 0
        sqlite3.Cursor.execute("Select name from members where name = ? and password = ?", (name, password))
        rows = sqlite3.Cursor.fetchall()
        for row in rows:
            counter += 1
            # print(row)

        if counter > 0:
            print("Welcome back!")
        else:
            print(
                'To use our application first you should register first! Type yes to registrate now or yes to do it later!')
            register_status = input()
            if register_status == 'yes':
                self.register_a_new_member(name, password)
            else:
                print("Have a nice day and come back later!")
                return 0

    def register_a_new_member(self, future_member_name, future_member_password, future_member_mail):
        future_member_pid = self.the_size_of_database() + 1
        self.Cursor.execute('INSERT INTO members(member_id, NAME, PASSWORD,MAIL_ADDRESS) VALUES (?,?,?,?) ',
                            (future_member_pid, future_member_name, future_member_password, future_member_mail))
        print('Data entered successfully.')
        self.connection.commit()

    def the_size_of_database(self):
        count = 0
        self.Cursor.execute("Select member_id,name,password from members")
        rows = self.Cursor.fetchall()
        for row in rows:
            count += 1
            print(row)

        return count

    ###################################################Class###############################################################
    # Create a table teszt
    def test1(self):

        #self.connection.commit()

        sql = "INSERT INTO classes(class_name) VALUES ('Calculus')"
        self.Cursor.execute(sql)
        sql = "INSERT INTO classes(class_name) VALUES ('Software development')"
        self.Cursor.execute(sql)
        sql = "INSERT INTO classes(class_name) VALUES ('Operating system1')"
        self.Cursor.execute(sql)
        sql = "INSERT INTO classes(class_name) VALUES ('World Literature')"
        self.Cursor.execute(sql)

        self.connection.commit()

    def register_a_new_class(self, future_class_name, future_class_thematic):
        self.Cursor.execute("""INSERT INTO Classes( CLASS_NAME, CLASS_THEMATIC) VALUES (?,?) """,
                            (future_class_name, future_class_thematic))
        print('Data entered successfully.')
        self.connection.commit()

    def show_our_database(self):
        self.Cursor.execute("Select class_id,class_name,class_thematic from Classes order by class_thematic")
        rows = self.Cursor.fetchall()
        for row in rows:
            print(row)

    def search_a_class_by_its_name(self, class_example):
        counter = 0
        self.Cursor.execute("Select class_id,class_name,class_thematic from Classes where class_thematic = ?",
                            (class_example,))
        rows = self.Cursor.fetchall()
        for row in rows:
            counter = counter + 1
            print(row)
        if counter == 0:
            print("There is no class with this thematic! Would like to create one? If you want type yes!")
        answer = input()
        if answer == "yes":
            self.register_a_new_class()
        return 0

    ###################################################Question###############################################################

    def test2(self):

        # Create a table teszt
        self.Cursor.execute(
            'CREATE TABLE questions(question VARCHAR(1000) PRIMARY KEY NOT NULL,question_correct_answer VARCHAR(5000) NOT NULL, class_name VARCHAR(100) NOT NULL, FOREIGN KEY (class_name) REFERENCES classes(class_name))')

        sql = "INSERT INTO questions(question, question_correct_answer, class_name) VALUES ('Firstc?','Igen', 'Calculus')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Secondc?','Nem', 'Calculus')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Thirdc?','Nem','Calculus')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Fourthc?','Nem','Calculus')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Fifthc?','Nem','Calculus')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Sixthc?','Igen','Calculus')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Seventhc?','Nem','Calculus')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Eighthc?','Igen','Calculus')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Ninthc?','Nem','Calculus')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Tenthc?','Nem','Calculus')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO questions(question, question_correct_answer, class_name) VALUES ('Firsto?','Igen', 'Operating system1')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Secondo?','Nem', 'Operating system1')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Thirdo?','Nem','Operating system1')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Fourtho?','Nem','Operating system1')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Fiftho?','Nem','Operating system1')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Sixtho?','Igen','Operating system1')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Seventho?','Nem','Operating system1')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Eightho?','Igen','Operating system1')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Nintho?','Nem','Operating system1')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Tentho?','Nem','Operating system1')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO questions(question, question_correct_answer, class_name) VALUES ('Firsts?','Igen', 'Software development')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Seconds?','Nem', 'Software development')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Thirds?','Nem','Software development')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Fourths?','Nem','Software development')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Fifths?','Nem','Software development')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Sixths?','Igen','Software development')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Sevenths?','Nem','Software development')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Eighths?','Igen','Software development')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Ninths?','Nem','Software development')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Tenths?','Nem','Software development')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO questions(question, question_correct_answer, class_name) VALUES ('Firstw?','Igen', 'World Literature')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Secondw?','Nem', 'World Literature')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Thirdw?','Nem','World Literature')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Fourthw?','Nem','World Literature')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Fifthw?','Nem','World Literature')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Sixthw?','Igen','World Literature')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Seventhw?','Nem','World Literature')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Eighthw?','Igen','World Literature')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Ninthw?','Nem','World Literature')"
        self.Cursor.execute(sql)

        sql = "INSERT INTO Questions(question, question_correct_answer, class_name) VALUES ('Tenthw?','Nem','World Literature')"
        self.Cursor.execute(sql)
        self.connection.commit()

    def show_questions(self):
        self.Cursor.execute("Select * from Questions")
        rows = self.Cursor.fetchall()
        for row in rows:
            print(row)
