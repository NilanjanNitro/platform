import psycopg2
from fluent import event
from fluent import sender


class Tenant:
    tenant_id: int
    tenant_name: str
    users_id: list
    devices: list
    admin_user_id: str
    apps_id: list
    rules: list

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

    def create_tenant(self):
        conn: psycopg2.connect()
        self.sender.setup('fluentd.test', host='localhost', port=24224)
        try:
            conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                                    port="5432")
            self.event.Event('follow', {'function': 'create_tenant', 'status': 'DB_conn_opened'})
            cur = conn.cursor()
            cur.execute("INSERT INTO USEMGMNT (TENANT_ID, USERS_ID, DEVICES, ADMIN_USER_ID, APPS_ID, RULES) \
                                          VALUES (" + str(self.tenant_id) + ", '" + str(self.users_id) + "', '" + str(
                self.devices) + "', '" + self.admin_user_id + "', '" + str(self.apps_id) + "', '" + str(
                self.rules) + "') ;")
            conn.commit()

            self.event.Event('follow', {'function': 'create_tenant', 'status': 'successful'})
        except:
            self.event.Event('follow', {'function': 'create_tenant', 'status': 'exception occurred'})
        finally:
            conn.close()
            self.event.Event('follow', {'function': 'create_tenant', 'status': 'DB_conn_closed'})

    @staticmethod
    def retrieve_tenant(tenant_id):
        conn: psycopg2.connect()
        tn_id = str(tenant_id)
        tn: Tenant
        sender.setup('fluentd.test', host='localhost', port=24224)
        try:
            conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                                    port="5432")
            event.Event('follow', {'function': 'retrieve_tenant', 'status': 'DB_conn_opened'})
            cur = conn.cursor()
            cur.execute(
                "SELECT TENANT_ID, USERS_ID, DEVICES, ADMIN_USER_ID, APPS_ID, RULES  from USEMGMNT WHERE TENANT_ID =" + tn_id + "  ;")
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
            event.Event('follow', {'function': 'retrieve_tenant', 'status': 'successful'})
        except:
            self.event.Event('follow', {'function': 'retrieve_tenant', 'status': 'exception occurred'})
        finally:
            conn.close()
            event.Event('follow', {'function': 'retrieve_tenant', 'status': 'DB_conn_closed'})

    @staticmethod
    def add_tenant_user(user_id: int, tenant_id: int):
        conn: psycopg2.connect()
        tn_id = str(tenant_id)
        sender.setup('fluentd.test', host='localhost', port=24224)
        try:
            conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                                    port="5432")
            event.Event('follow', {'function': 'add_tenant_user', 'status': 'DB_conn_opened'})
            cur = conn.cursor()
            cur.execute("SELECT USERS_ID from USEMGMNT WHERE TENANT_ID=" + tn_id + " ;")
            rows = cur.fetchall()
            _users_: list
            for row in rows:
                _users_ = list(row[0])
                _users_.append(str(user_id))
            cur.execute("UPDATE USEMGMNT set USERS_ID = " + str(_users_) + " where TENANT_ID = " + tn_id + " ;")
            conn.commit()
            event.Event('follow', {'function': 'add_tenant_user', 'status': 'successful'})
        except:
            event.Event('follow', {'function': 'add_tenant_user', 'status': 'exception occurred'})
        finally:
            conn.close()
            event.Event('follow', {'function': 'add_tenant_user', 'status': 'DB_conn_closed'})

    @staticmethod
    def add_tenant_device(device_id: int, tenant_id: int):
        conn: psycopg2.connect()
        _device_: list
        tn_id = str(tenant_id)
        sender.setup('fluentd.test', host='localhost', port=24224)
        try:
            conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                                    port="5432")
            event.Event('follow', {'function': 'add_tenant_device', 'status': 'DB_conn_opened'})
            cur = conn.cursor()
            cur.execute("SELECT DEVICES from USEMGMNT WHERE TENANT_ID=" + tn_id + " ;")
            rows = cur.fetchall()
            for row in rows:
                _devices_ = list(row[0])
                _devices_.append(str(device_id))
            cur.execute("UPDATE USEMGMNT set DEVICES = " + str(_devices_) + " where TENANT_ID = " + tn_id + " ;")
            conn.commit()
            event.Event('follow', {'function': 'add_tenant_device', 'status': 'successful'})
        except:
            event.Event('follow', {'function': 'add_tenant_device', 'status': 'exception occurred'})
        finally:
            conn.close()
            event.Event('follow', {'function': 'add_tenant_device', 'status': 'DB_conn_closed'})

    @staticmethod
    def update_tenant_admin(admin_user_id: int, tenant_id: int):
        conn: psycopg2.connect()
        tn_id = str(tenant_id)
        sender.setup('fluentd.test', host='localhost', port=24224)
        try:
            conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                                    port="5432")
            event.Event('follow', {'function': 'update_tenant_admin', 'status': 'DB_conn_opened'})
            cur = conn.cursor()
            cur.execute(
                "UPDATE USEMGMNT set ADMIN_USER_ID = " + str(admin_user_id) + " where TENANT_ID = " + tn_id + " ;")
            conn.commit()
            event.Event('follow', {'function': 'update_tenant_admin', 'status': 'successful'})
        except:
            event.Event('follow', {'function': 'update_tenant_admin', 'status': 'exception occurred'})
        finally:
            conn.close()
            event.Event('follow', {'function': 'update_tenant_admin', 'status': 'DB_conn_closed'})

    @staticmethod
    def add_tenant_app(app_id: int, tenant_id: int):
        conn: psycopg2.connect()
        _apps_: list
        tn_id = str(tenant_id)
        sender.setup('fluentd.test', host='localhost', port=24224)
        try:
            conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                                    port="5432")
            event.Event('follow', {'function': 'add_tenant_app', 'status': 'DB_conn_opened'})
            cur = conn.cursor()
            cur.execute("SELECT APPS_ID from USEMGMNT WHERE TENANT_ID=" + tn_id + " ;")
            rows = cur.fetchall()
            for row in rows:
                _apps_ = list(row[0])
                _apps_.append(str(app_id))
            cur.execute("UPDATE USEMGMNT set APPS_ID = " + str(_apps_) + " where TENANT_ID = " + tn_id + " ;")
            conn.commit()
            event.Event('follow', {'function': 'add_tenant_app', 'status': 'successful'})
        except:
            event.Event('follow', {'function': 'add_tenant_app', 'status': 'exception occurred'})
        finally:
            conn.close()
            event.Event('follow', {'function': 'add_tenant_app', 'status': 'DB_conn_closed'})

    @staticmethod
    def add_tenant_rule(rule_id: int, tenant_id: int):
        conn: psycopg2.connect()
        _rul_: list
        tn_id = str(tenant_id)
        sender.setup('fluentd.test', host='localhost', port=24224)
        try:
            conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                                    port="5432")
            event.Event('follow', {'function': 'add_tenant_rule', 'status': 'DB_conn_opened'})
            cur = conn.cursor()
            cur.execute("SELECT RULES from USEMGMNT WHERE TENANT_ID=" + tn_id + " ;")
            rows = cur.fetchall()
            for row in rows:
                _rul_ = list(row[0])
                _rul_.append(str(rule_id))
            cur.execute("UPDATE USEMGMNT set APPS_ID = " + str(_rul_) + " where TENANT_ID = " + tn_id + " ;")
            conn.commit()
            event.Event('follow', {'function': 'add_tenant_rule', 'status': 'successful'})
        except:
            event.Event('follow', {'function': 'add_tenant_rule', 'status': 'exception occurred'})
        finally:
            conn.close()
            event.Event('follow', {'function': 'add_tenant_rule', 'status': 'DB_conn_closed'})
