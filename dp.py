import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="0.tcp.jp.ngrok.io",   # 지금 켜둔 ngrok 주소
        port=25818,                  # 지금 켜둔 ngrok 포트
        user="root",
        password="studycafe1234!",
        database="studycafe"
    )