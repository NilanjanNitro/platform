import psycopg2
from fluent import event
from fluent import sender


class User:
    user_id: int
    user_pwd: str
    first_name: str
    last_name: str
    ph_number: int
    api_acl: list
    tenant_id: int

    def __int__(self, user_id: int, user_pwd: str, first_name: str, last_name: str, ph_number: int, api_acl: list,
                tenant_id: int):
        self.user_id = user_id
        self.user_pwd = user_pwd
        self.first_name = first_name
        self.last_name = last_name
        self.ph_number = ph_number
        self.api_acl = api_acl
        self.tenant_id = tenant_id

    def create_user(self):
        conn: psycopg2.connect()
        sender.setup('fluentd.test', host='localhost', port=24224)
        try:
            conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                                    port="5432")
            event.Event('follow', {'function': 'create_user', 'status': 'DB_conn_opened'})
            cur = conn.cursor()
            cur.execute("INSERT INTO USERS (USER_ID, USER_PWD, FIRST_NAME, LAST_NAME, PH_NUMBER, API_ACL, TENANT_ID) \
                                                  VALUES (" + str(self.user_id) + ", '" + self.user_pwd + "', '"
                        + self.first_name + "', '" + self.last_name + "', '" + str(self.ph_number) + "', '" + str(
                self.api_acl) + "', '" + str(self.tenant_id) + "') ;")
            conn.commit()
            event.Event('follow', {'function': 'create_user', 'status': 'successful'})
        except:
            event.Event('follow', {'function': 'create_user', 'status': 'exception occurred'})
        finally:
            conn.close()
            event.Event('follow', {'function': 'create_user', 'status': 'DB_conn_closed'})
