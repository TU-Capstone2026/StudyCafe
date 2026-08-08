from backend.db import get_connection
import mysql.connector

def cancel_seat(seat_number):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = "UPDATE seats SET status = 'available' WHERE seat_number = %s"
        cursor.execute(sql,(seat_number,))

        conn.commit()
        if cursor.rowcount == 0:
            print("⚠️ 좌석 %s 을(를) 찾을 수 없습니다." %(seat_number))
        else:
            print("✅ 좌석 %s 취소 성공" %(seat_number))

    except mysql.connector.Error as e:
        print("DB 오류발생 %s" %(e))
        if conn:
            conn.rollback()

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


