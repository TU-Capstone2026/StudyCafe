from db import get_connection
import mysql.connector

def cancel_seat(seat_number, member_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT status FROM seats WHERE seat_number = %s", (seat_number,))
        row = cursor.fetchone()

        if row is None:
            print("⚠️ 좌석 %s 을(를) 찾을 수 없습니다." %(seat_number))
            return 404
        current_status = row[0]

        if current_status != 'reserved':
            print("ℹ️ 좌석 %s은(는) 예약된 좌석이 아닙니다. (현재 상태: %s)" %(seat_number, current_status))
            return 400

        cursor.execute(
            "UPDATE seats SET status = 'available' WHERE seat_number = %s",
            (seat_number,)
        )

        # 관리자 로그 테이블에 취소 기록 남기기
        log_sql = """
            INSERT INTO reservation_logs (Member_ID, seat_number, action) 
            VALUES (%s, %s, %s)
        """
        # 취소 동작이므로 세 번째 자리에 CANCEL을 입력합니다.
        cursor.execute(log_sql, (member_id, seat_number, 'CANCEL'))

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


