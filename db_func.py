import psycopg2


class Dbfunc:
    conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                            port="5432")

    def __int__(self):
        print("Opened database successfully")

    def create_tenant(self):
        cur = self.conn.cursor()
        cur.execute('''INSERT INTO COMPANY (ID, USERS_ID, DEVICES, ADMIN_USER_ID, RULES) \
                          VALUES (1, '(1,2)', '(1)', '(1)', '(1)');''')
        print("Records created successfully")
        self.conn.commit()
        self.conn.close()

    def retreive_tenant(self):
        cur = self.conn.cursor()
        cur.execute("SELECT ID, USERS_ID, DEVICES, ADMIN_USER_ID  from COMPANY")
        rows = cur.fetchall()
        for row in rows:
            print
            "ID = ", row[0]
            print
            "NAME = ", row[1]
            print
            "ADDRESS = ", row[2]
            print
            "SALARY = ", row[3], "\n"

        print
        "Operation done successfully";
        conn.close()