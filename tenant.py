import psycopg2
from fluent import event
from fluent import sender


class Tenant:
    tenant_id = int
    users_id = ()
    devices = ()
    admin_user_id = str
    apps_id = ()
    rules = ()
    _users_ = ()
    _devices_ = ()
    _apps_ = ()
    _rul_ = ()
    conn = psycopg2
    sender.setup('fluentd.test', host='localhost', port=24224)
    event.Event('follow', {'function': 'tenant_constructor', 'status': 'Object initialized'})

    def __init__(self, tenant_id, users_id, devices, admin_user_id, apps_id, rules):
        self.tenant_id = tenant_id
        self.users_id = users_id
        self.devices = devices
        self.admin_user_id = admin_user_id
        self.rules = rules
        self.apps_id = apps_id
        self._users_ = ()
        self._devices_ = ()
        self._apps_ = ()
        self._rul_ = ()
        self.sender.setup('fluentd.test', host='localhost', port=24224)
        self.event.Event('follow', {'function': 'tenant_constructor', 'status': 'Object initialized'})

    def create_tenant(self, tenant_id, users_id, devices, admin_user_id, apps_id, rules):
        conn = psycopg2
        try:
            conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                                    port="5432")
            self.logger_event('follow', {'function': 'create_tenant', 'status': 'DB_conn_opened'})
            cur = self.conn.cursor()
            cur.execute("INSERT INTO USEMGMNT (TENANT_ID, USERS_ID, DEVICES, ADMIN_USER_ID, APPS_ID, RULES) \
                                          VALUES (" + tenant_id + ", '" + users_id + "', '" + devices + "', '" + admin_user_id + "', '" + apps_id + "', '" + rules + "') ;")
            print("Records created successfully")
            conn.commit()
            sender.setup('fluentd.test', host='localhost', port=24224)
            event.Event('follow', {'function': 'create_tenant', 'status': 'successful'})
        except:
            self.event.Event('follow', {'function': 'create_tenant', 'status': 'exception occurred'})
        finally:
            conn.close()
            self.event.Event('follow', {'function': 'create_tenant', 'status': 'DB_conn_closed'})

    def retrieve_tenant(self, tenant_id):
        conn: psycopg2.connect()
        tn: Tenant
        try:
            conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                                    port="5432")
            self.event.Event('follow', {'function': 'retrieve_tenant', 'status': 'DB_conn_opened'})
            tn_id = str(tenant_id)
            cur = conn.cursor()
            cur.execute(
                "SELECT TENANT_ID, USERS_ID, DEVICES, ADMIN_USER_ID, APPS_ID, RULES  from USEMGMNT WHERE TENANT_ID = " + tn_id + ";")
            rows = cur.fetchall()
            for row in rows:
                tn = Tenant(row[0], row[0], row[0], row[0], row[0], row[0])
                print(tn.tenant_id)
                print(tn.users_id)
                print(tn.devices)
                print(tn.admin_user_id)
                print(tn.apps_id)
                print(tn.rules)
            conn.commit()
            return tn
            self.event.Event('follow', {'function': 'retrieve_tenant', 'status': 'successful'})
        except:
            self.event.Event('follow', {'function': 'retrieve_tenant', 'status': 'exception occurred'})
        finally:
            conn.close()
            self.event.Event('follow', {'function': 'retrieve_tenant', 'status': 'DB_conn_closed'})

    def add_tenant_user(self, user_id, tenant_id):
        conn: psycopg2.connect()
        try:
            conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                                    port="5432")
            self.event.Event('follow', {'function': 'add_tenant_user', 'status': 'DB_conn_opened'})
            tn_id = str(tenant_id)
            cur = self.conn.cursor()
            cur.execute("SELECT USERS_ID from USEMGMNT WHERE TENANT_ID=" + tn_id + " ;")
            rows = cur.fetchall()
            for row in rows:
                self._users_ = list(row[0])
                self._users_.append(user_id)
            cur.execute("UPDATE USEMGMNT set USERS_ID = " + str(self._users_) + " where TENANT_ID = " + tn_id + " ;")
            self.conn.commit()
            self.event.Event('follow', {'function': 'add_tenant_user', 'status': 'successful'})
        except:
            self.event.Event('follow', {'function': 'add_tenant_user', 'status': 'exception occurred'})
        finally:
            conn.close()
            self.event.Event('follow', {'function': 'add_tenant_user', 'status': 'DB_conn_closed'})

    def add_tenant_device(self, device_id, tenant_id):

        self.conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                                     port="5432")
        tn_id = str(tenant_id)
        cur = self.conn.cursor()
        cur.execute("SELECT DEVICES from USEMGMNT WHERE TENANT_ID=" + tn_id + " ;")
        rows = cur.fetchall()
        for row in rows:
            self._devices_ = list(row[0])
            self._devices_.append(device_id)
        cur.execute("UPDATE USEMGMNT set DEVICES = " + str(self._devices_) + " where TENANT_ID = " + tn_id + " ;")
        self.conn.commit()
        self.conn.close()
        print("Operation done successfully")

    def update_tenant_admin(self, admin_user_id, tenant_id):
        self.conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                                     port="5432")
        tn_id = str(tenant_id)
        cur = self.conn.cursor()
        cur.execute("UPDATE USEMGMNT set ADMIN_USER_ID = " + str(admin_user_id) + " where TENANT_ID = " + tn_id + " ;")
        self.conn.commit()
        self.conn.close()
        print("Operation done successfully")

    def add_tenant_app(self, app_id, tenant_id):
        self.conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                                     port="5432")
        tn_id = str(tenant_id)
        cur = self.conn.cursor()
        cur.execute("SELECT APPS_ID from USEMGMNT WHERE TENANT_ID=" + tn_id + " ;")
        rows = cur.fetchall()
        for row in rows:
            self._apps_ = list(row[0])
            self._apps_.append(app_id)
        cur.execute("UPDATE USEMGMNT set APPS_ID = " + str(self._apps_) + " where TENANT_ID = " + tn_id + " ;")
        self.conn.commit()
        self.conn.close()
        print("Operation done successfully")

    def add_tenant_rule(self, rule_id, tenant_id):
        self.conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                                     port="5432")
        tn_id = str(tenant_id)
        cur = self.conn.cursor()
        cur.execute("SELECT RULES from USEMGMNT WHERE TENANT_ID=" + tn_id + " ;")
        rows = cur.fetchall()
        for row in rows:
            self._rul_ = list(row[0])
            self._rul_.append(rule_id)
        cur.execute("UPDATE USEMGMNT set APPS_ID = " + str(self._rul_) + " where TENANT_ID = " + tn_id + " ;")
        self.conn.commit()
        self.conn.close()
        print("Operation done successfully")
