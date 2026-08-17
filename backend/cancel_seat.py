from db import get_connection
import mysql.connector

def cancel_seat(seat_number, member_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT seat_id, status FROM seats WHERE seat_number = %s", (seat_number,))
        row = cursor.fetchone()

        if row is None:
            print("⚠️ 좌석 %s 을(를) 찾을 수 없습니다." %(seat_number))
            return 404
        seat_id, current_status = row

        if current_status != 'reserved':
            print("ℹ️ 좌석 %s은(는) 예약된 좌석이 아닙니다. (현재 상태: %s)" %(seat_number, current_status))
            return 400

        cursor.execute(
            "UPDATE seats SET status = 'available' WHERE seat_number = %s",
            (seat_number,)
        )
        
        cursor.execute(
            "UPDATE Member_Information SET seat_id = NULL WHERE Member_ID = %s AND seat_id = %s",
            (member_id, seat_id)
        )

        conn.commit()


        print("✅ 좌석 %s 취소 성공" %(seat_number))
        return 1

    except mysql.connector.Error as e:
        print("DB 오류발생 %s" %(e))
        if conn:
            conn.rollback()
        return 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


