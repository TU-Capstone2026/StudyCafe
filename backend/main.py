from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector

app = FastAPI(title="스터디카페 예약 API")

# 1. DB 연결 함수 (ngrok 사용)
def get_db():
    return mysql.connector.connect(
        host="0.tcp.jp.ngrok.io",
        port=25818,
        user="root",
        password="studycafe1234!",
        database="studycafe"
    )

# 2. 프론트엔드에서 받을 데이터 구조 (좌석 번호)
class SeatAction(BaseModel):
    seat_number: str

# 3. API 엔드포인트

# (1) 전체 좌석 조회 (show_all_seats 대체) - GET 요청
@app.get("/seats")
def get_all_seats():
    conn = get_db()
    # dictionary=True 로 설정하면 데이터를 JSON으로 변환하기 편하게 딕셔너리로 가져옵니다.
    cursor = conn.cursor(dictionary=True) 
    
    cursor.execute("SELECT * FROM seats")
    seats = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return {"seats": seats}

# (2) 좌석 추가 (add_seat 대체) - POST 요청
@app.post("/seats")
def add_new_seat(request: SeatAction):
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        sql = "INSERT INTO seats (seat_number) VALUES (%s)"
        cursor.execute(sql, (request.seat_number,))
        conn.commit()
        return {"message": f"✅ 좌석 '{request.seat_number}' 추가 성공!"}
    except mysql.connector.Error as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=f"DB 오류 (이미 있는 좌석일 수 있습니다): {e}")
    finally:
        cursor.close()
        conn.close()

# (3) 체크인 (Book.check_in 대체) - POST 요청
@app.post("/checkin")
def seat_check_in(request: SeatAction):
    conn = get_db()
    cursor = conn.cursor()
    
    # 해당 좌석의 상태를 '사용중(occupied)'이나 1 등으로 변경하는 쿼리 (DB 구조에 맞게 status 값 수정 필요)
    sql = "UPDATE seats SET status = 'occupied' WHERE seat_number = %s AND status != 'occupied'"
    cursor.execute(sql, (request.seat_number,))
    
    if cursor.rowcount == 0: # 변경된 줄이 없다면 (이미 사용중이거나 없는 좌석)
        cursor.close()
        conn.close()
        raise HTTPException(status_code=400, detail="이미 사용중이거나 존재하지 않는 좌석입니다.")
        
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": f"'{request.seat_number}' 좌석 체크인 완료!"}

# (4) 체크아웃 (Book.check_out 대체) - POST 요청
@app.post("/checkout")
def seat_check_out(request: SeatAction):
    conn = get_db()
    cursor = conn.cursor()
    
    # 해당 좌석의 상태를 '빈자리(available)'나 0 등으로 복구하는 쿼리
    sql = "UPDATE seats SET status = 'available' WHERE seat_number = %s"
    cursor.execute(sql, (request.seat_number,))
    conn.commit()
    
    cursor.close()
    conn.close()
    return {"message": f"'{request.seat_number}' 좌석 퇴실 처리 완료!"}