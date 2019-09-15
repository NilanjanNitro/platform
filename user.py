import psycopg2


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

    def create_user(self, user_id: int, user_pwd: str, first_name: str, last_name: str, ph_number: int, api_acl: list,
                    tenant_id: int):
        conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                                port="5432")
        cur = conn.cursor()
        cur.execute("INSERT INTO USERS (USER_ID, USER_PWD, FIRST_NAME, LAST_NAME, PH_NUMBER, API_ACL, TENANT_ID) \
                                      VALUES (" + str(user_id) + ", '" + user_pwd + "', '"
                    + first_name + "', '" + last_name + "', '" + str(ph_number) + "', '" + str(api_acl) + "', '" + str(
            tenant_id) + "') ;")
        print("Records created successfully")
        conn.commit()
        conn.close()
        print("Operation done successfully")
