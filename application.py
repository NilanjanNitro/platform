import psycopg2


class Apps:
    conn = psycopg2.connect(database="postgres", user="postgres", password="jio@Nilanjan", host="127.0.0.1",
                            port="5432")
    app_id = int
    callback_url = str
    auth_key = str
    auth_token = str
