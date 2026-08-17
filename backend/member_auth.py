import mysql.connector
from db import get_connection
from auth import hash_password, verify_password, create_access_token

def register_member(name, email, password, phone=None, address=None, seat_id=None):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT Member_ID FROM Member_Information WHERE Member_Email = %s", (email,))
        if cursor.fetchone() is not None:
            return 409  # 이미 가입된 이메일

        hashed = hash_password(password)
        sql = """INSERT INTO Member_Information
                 (Member_Name, Member_Email, Member_Phone, Member_Address, password_hash, seat_id)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (name, email, phone, address, hashed, seat_id))
        conn.commit()
        return 1

    except mysql.connector.Error as e:
        print(f"DB 오류발생 {e}")
        if conn:
            conn.rollback()
        return 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def login_member(email, password):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT Member_ID, password_hash FROM Member_Information WHERE Member_Email = %s",
            (email,)
        )
        row = cursor.fetchone()

        if row is None:
            return 404, None  # 가입 안 된 이메일

        member_id, hashed = row
        if not verify_password(password, hashed):
            return 401, None  # 비밀번호 불일치

        token = create_access_token(member_id)
        return 1, token

    except mysql.connector.Error as e:
        print(f"DB 오류발생 {e}")
        return 500, None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()