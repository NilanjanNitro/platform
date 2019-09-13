import psycopg2

class Tenant:

    tenant_id = None
    users_id = ()
    devices = ()
    admin_user_id = ""
    rules = ()

    conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1", port="5432")
    print("Opened database successfully")
    cur = conn.cursor()
    cur.execute('''INSERT INTO COMPANY (ID, USERS_ID, DEVICES, ADMIN_USER_ID, RULES) \
          VALUES (1, '(1,2)', '(1)', '(1)', '(1)');''')
    print("Records created successfully")
    conn.commit()
    conn.close()

    def __init__(self, tenant_id, users_id, devices, admin_user_id, rules):
        self.tenant_id = tenant_id
        self.users_id = users_id
        self.devices = devices
        self.admin_user_id = admin_user_id
        self.rules = rules

    def getUsers_id(self):
        self.users_id = ()
