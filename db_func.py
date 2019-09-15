import psycopg2

from tenant import Tenant


class Dbfunc:
    conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                            port="5432")

    def __int__(self):
        print("Opened database successfully")

    def create_tenant(self):
        cur = self.conn.cursor()
        cur.execute('''INSERT INTO USEMGMNT (TENANT_ID, USERS_ID, DEVICES, ADMIN_USER_ID, APPS_ID, RULES) \
                          VALUES (111, '(0001,00002)', '(11,22)', '(0001)', '(999)' '(1234)');''')
        print("Records created successfully")
        self.conn.commit()
        self.conn.close()

    def retrieve_tenant(self, tenant_id):
        tn_id = str(tenant_id)
        cur = self.conn.cursor()
        cur.execute("SELECT "+tn_id+", USERS_ID, DEVICES, ADMIN_USER_ID, APPS_ID, RULES  from USEMGMNT")
        rows = cur.fetchall()
        for row in rows:
            tn = Tenant(row[0], row[0], row[0], row[0], row[0], row[0])
            print(tn.tenant_id)
            print(tn.users_id)
            print(tn.devices)
            print(tn.admin_user_id)
            print(tn.apps_id)
            print(tn.rules)
        print("Operation done successfully")
        self.conn.close()
