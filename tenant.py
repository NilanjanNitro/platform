import psycopg2


class Tenant:
    conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                            port="5432")
    tenant_id = None
    users_id = ()
    devices = ()
    admin_user_id = ""
    apps_id = ()
    rules = ()
    b_user = ()
    b_devices = ()

    def __init__(self, tenant_id, users_id, devices, admin_user_id, apps_id, rules):
        self.tenant_id = tenant_id
        self.users_id = users_id
        self.devices = devices
        self.admin_user_id = admin_user_id
        self.rules = rules
        self.apps_id = apps_id
        self.b_usr = ()
        self.b_devices = ()

    def create_tenant(self, tenant_id, users_id, devices, admin_user_id, apps_id, rules):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO USEMGMNT (TENANT_ID, USERS_ID, DEVICES, ADMIN_USER_ID, APPS_ID, RULES) \
                              VALUES ("+tenant_id+", '"+users_id+"', '"+devices+"', '"+admin_user_id+"', '"+apps_id+"', '"+rules+"') ;")
        print("Records created successfully")
        self.conn.commit()
        self.conn.close()

    def retrieve_tenant(self, tenant_id):
        tn_id = str(tenant_id)
        cur = self.conn.cursor()
        cur.execute("SELECT " + tn_id + ", USERS_ID, DEVICES, ADMIN_USER_ID, APPS_ID, RULES  from USEMGMNT ;")
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

    def add_tenant_users(self, users_id, tenant_id):
        tn_id = str(tenant_id)
        cur = self.conn.cursor()
        cur.execute("SELECT USERS_ID from USEMGMNT WHERE TENANT_ID="+tenant_id+" ;")
        rows = cur.fetchall()
        for row in rows:
            self.b_usr = list(row[0])
            self.b_usr.append(users_id)
        print("Operation done successfully")
        cur.execute("UPDATE USEMGMNT set USERS_ID = "+str(self.b_usr)+" where TENANT_ID = "+tenant_id+" ;")
        self.conn.commit()
        self.conn.close()

    def add_tenant_device(self, device_id, tenant_id):
        tn_id = str(tenant_id)
        cur = self.conn.cursor()
        cur.execute("SELECT DEVICES from USEMGMNT WHERE TENANT_ID="+tn_id+" ;")
        rows = cur.fetchall()
        for row in rows:
            self.b_devices = list(row[0])
            self.b_devices.append(device_id)
        print("Operation done successfully")
        cur.execute("UPDATE USEMGMNT set USERS_ID = "+str(self.b_devices)+" where TENANT_ID = "+tn_id+" ;")
        self.conn.commit()
        self.conn.close()

    def update_tenant_admin(self, admin_user_id, tenant_id):

