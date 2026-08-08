import mysql.connector
from db import get_connection

def show_all_seats():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        # dictionary=True로 설정하면 결과를 dict 형태로 받아올 수 있어서 API 응답에 유리함
        cursor = conn.cursor(dictionary=True)
        
        # 1. 전체 좌석 목록 조회
        sql = "SELECT seat_id, seat_number, status FROM seats ORDER BY seat_id;"
        cursor.execute(sql)
        
        seats = cursor.fetchall()
        return seats

    except mysql.connector.Error as e:
        print(f"DB 오류 발생: {e}")
        return []
        
    finally:
        # 자원 해제
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    print(show_all_seats())