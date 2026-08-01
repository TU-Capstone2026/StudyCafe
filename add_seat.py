import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="0.tcp.jp.ngrok.io",   # 지금 켜둔 ngrok 주소
        port=14682,                  # 지금 켜둔 ngrok 포트
        user="root",
        password="studycafe1234!",
        database="studycafe"
    )

def add_seat(seat_number):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # 좌석 추가 쿼리 (status는 DEFAULT값인 '이용가능'으로 자동 들어감)
        sql = "INSERT INTO seats (seat_number) VALUES (%s);"
        cursor.execute(sql, (seat_number,))
        
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