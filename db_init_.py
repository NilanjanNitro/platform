import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                        port="5432")
print("Opened database successfully")
cur = conn.cursor()
cur.execute('''CREATE TABLE USEMGMNT
                  (TENANT_ID INT PRIMARY KEY        NOT NULL,
                  USERS_ID           TEXT    NOT NULL,
                  DEVICES            TEXT,
                  ADMIN_USER_ID      TEXT    NOT  NULL,
                  APPS_ID            TEXT
                  RULES              TEXT              );''')
print("Table created successfully")
conn.commit()
conn.close()
