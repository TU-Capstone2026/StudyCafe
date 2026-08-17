import mysql.connector
from db import get_connection

# 매개변수에 member_id를 추가
def add_seat(seat_number, member_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # 좌석 추가 쿼리 (status는 DEFAULT값인 '이용가능'으로 자동 들어감)
        sql = "UPDATE seats SET status = 'reserved' WHERE seat_number = %s;"
        cursor.execute(sql, (seat_number,))

        # 관리자 로그 테이블에 예약 기록 남기기
        log_sql = """
            INSERT INTO reservation_logs (Member_ID, seat_number, action) 
            VALUES (%s, %s, %s)
        """
        cursor.execute(log_sql, (member_id, seat_number, 'RESERVE'))
        
        # 데이터 변경사항 저장 (COMMIT 필수)
        conn.commit()
        print(f"✅ 좌석 '{seat_number}' 추가 성공!")

    except mysql.connector.Error as e:
        print(f"DB 오류 발생: {e}")
        if conn:
            conn.rollback() # 오류 시 복구
        
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    add_seat('A-101')
