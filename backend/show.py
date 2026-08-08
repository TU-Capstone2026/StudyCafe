import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="0.tcp.jp.ngrok.io",   # 지금 켜둔 ngrok 주소
        port=25818,                  # 지금 켜둔 ngrok 포트
        user="root",
        password="studycafe1234!",
        database="studycafe"
    )

def show_all_seats():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # 1. 전체 좌석 목록 조회
        sql = "SELECT seat_id, seat_number, status FROM seats ORDER BY seat_id;"
        cursor.execute(sql)
        
        seats = cursor.fetchall()
        
        print("=== 전체 좌석 상태 목록 ===")
        if not seats:
            print("등록된 좌석이 없습니다.")
            return
        
        # 2. 결과 출력
        for seat_id, seat_number, status in seats:
            print(f"[{seat_id}] 좌석 번호: {seat_number} | 상태: {status}")

    except mysql.connector.Error as e:
        print(f"DB 오류 발생: {e}")
        
    finally:
        # 자원 해제
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    show_all_seats()