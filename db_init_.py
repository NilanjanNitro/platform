import psycopg2

# Create Tenant Table
conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                        port="5432")
print("Opened database successfully")
cur = conn.cursor()
cur.execute('''CREATE TABLE USEMGMNT
                  (TENANT_ID INT PRIMARY KEY        NOT NULL,
                  TENANT_NAME        TEXT    NOT NULL,
                  USERS_ID           TEXT    NOT NULL,
                  DEVICES            TEXT,
                  ADMIN_USER_ID      TEXT    NOT  NULL,
                  APPS_ID            TEXT,
                  RULES              TEXT              );''')
print("USEMGMNT Table created successfully")
conn.commit()
conn.close()

# Create User Table
conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                        port="5432")
print("Opened database successfully")
cur = conn.cursor()
cur.execute('''CREATE TABLE USERS
                  (USER_ID INT PRIMARY KEY          NOT NULL,
                  USER_PWD                  TEXT    NOT NULL,
                  FIRST_NAME                TEXT    NOT NULL,
                  LAST_NAME                 TEXT    NOT NULL,
                  PH_NUMBER                 INT     NOT NULL,
                  API_ACL                   TEXT    NOT NULL, 
                  TENANT_ID                 INT     NOT NULL );''')
print("USERS Table created successfully")
conn.commit()
conn.close()

# Create Application Table
conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                        port="5432")
print("Opened database successfully")
cur = conn.cursor()
cur.execute('''CREATE TABLE APPS
                  (APP_ID INT PRIMARY KEY           NOT NULL,
                  CALLBACK_URL              TEXT    NOT NULL,
                  AUTH_KEY                  TEXT    NOT NULL,
                  AUTH_TOKEN                TEXT    NOT NULL,
                  SERVER_PKI                TEXT    NOT NULL,
                  CLIENT_PKI                TEXT    NOT NULL, 
                  HB_CHK_FRE                TEXT    NOT NULL,
                  COMM_CONF                 TEXT    NOT NULL,
                  TENANT_ID                 INT     NOT NULL );''')
print("USERS Table created successfully")
conn.commit()
conn.close()