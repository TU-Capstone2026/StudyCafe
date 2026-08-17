from show import show_all_seats
from cancel_seat import cancel_seat
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware # CORS 설정
from fastapi import FastAPI, Response
from pydantic import BaseModel
from reserve_seat import reserve_seat
from member_auth import register_member, login_member
from auth import decode_access_token
from db import get_connection

from fastapi import FastAPI, Response, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware # CORS 설정
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# FastAPI 인스턴스 생성
from pydantic import BaseModel

# Pydantic 모델 정의 및 seat_number 형식 정의
class SeatCreate(BaseModel):
    seat_number: str

app = FastAPI(
    title="StudyCafe API",
    description="스터디카페 예약 시스템 백엔드 API"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # 나중에 실제 주소로 변경 가능
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers=["*"],
)

##로그인 부분
class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str
    phone: str | None = None
    address: str | None = None
    seat_id: int | None = None   # 위 ALTER TABLE 적용 후 이렇게 Optional로

class LoginRequest(BaseModel):
    email: str
    password: str

def get_current_member(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="로그인이 필요하거나 토큰이 만료되었습니다")
    return payload["member_id"]

@app.get("/")
def read_root():
    return {
        "status":"success",
        "message":"스터디카페 예약 시스템 API 서버가 정상 작동 중입니다."
    }

@app.post("/register")
def register(req: RegisterRequest, response: Response):
    result = register_member(req.name, req.email, req.password, req.phone, req.address, req.seat_id)
    if result == 1:
        response.status_code = 201
        return {"status": "success"}
    elif result == 409:
        response.status_code = 409
        return {"status": "fail", "message": "이미 가입된 이메일입니다"}
    else:
        response.status_code = 500
        return {"status": "fail"}

@app.post("/login")
def login(req: LoginRequest, response: Response):
    result, token = login_member(req.email, req.password)
    if result == 1:
        return {"access_token": token, "token_type": "bearer"}
    elif result == 404:
        response.status_code = 404
        return {"status": "fail", "message": "가입되지 않은 이메일입니다"}
    elif result == 401:
        response.status_code = 401
        return {"status": "fail", "message": "비밀번호가 일치하지 않습니다"}
    else:
        response.status_code = 500
        return {"status": "fail"}

@app.get("/show")
def get_seats():
    seats = show_all_seats()
    return {
        "status": "success",
        "seats": seats
    }

# @app.post("/create")
# def create_seat(seat: SeatCreate, response: Response, member_id: int = Depends(get_current_member)):
#     result = reserve_seat(seat.seat_number, member_id)

#     if result == 1:
#         response.status_code = 201
#         return {"status": "success", "message": f"좌석 '{seat.seat_number}' 예약 성공!"}
#     elif result == 404:
#         response.status_code = 404
#         return {"statuscode": 404, "status": "fail", "message": "좌석을 찾을 수 없습니다"}
#     elif result == 400:
#         response.status_code = 400
#         return {"statuscode": 400, "status": "fail", "message": "이미 예약된 좌석입니다"}
#     else:
#         response.status_code = 500
#         return {"statuscode": 500, "status": "fail"}

# 1. 예약 요청시 전달받을 데이터 스키마 정의 (필요에 따라 user_id 등 추가)
class SeatBook(BaseModel):
    seat_number: str
    user_id: str  # 사용자 식별 정보가 필요하다면 추가

# 2. 좌석 예약 엔드포인트 추가
@app.post("/reserve")
def reserve(seat: SeatCreate, response: Response, member_id: int = Depends(get_current_member)):
    # 기존 Book.py의 함수/클래스 실행 (인자값은 Book.py 구조에 맞게 전달)
    result = reserve_seat(seat.seat_number, member_id)

    if result == 1:
        response.status_code = 200
        return {"status": "success", "message": f"좌석 '{seat.seat_number}' 예약 성공!"}
    elif result == 404:
        response.status_code = 404
        return {"status": "fail", "message": "좌석을 찾을 수 없습니다"}
    elif result == 400:
        response.status_code = 400
        return {"status": "fail", "message": "이미 예약된 좌석입니다."}
    else:
        response.status_code = 500
        return {"status": "fail", "message": "서버 오류가 발생했습니다."}

@app.delete("/cancel/{seat_number}/")
def cancel_seats(seat_number: str, response: Response, member_id: int = Depends(get_current_member)):
    result = cancel_seat(seat_number, member_id)

    if result == 1:
        response.status_code = 200
        return {
            "status": "success"
            }
    elif result == 404:
        response.status_code = 404
        return {"statuscode": 404, 
                "status": "fail", 
                "message": "좌석을 찾을 수 없습니다"
                }
    elif result == 400:
        response.status_code = 400
        return {"statuscode": 400, 
                "status": "fail", 
                "message": "예약되지 않은 좌석입니다"
                }
    else:  # 500
        response.status_code = 500
        return {"statuscode": 500, 
                "status": "fail"
                }

# 관리자 로그 조회 라우터
@app.get("/admin/logs")
def get_reservation_logs():
    """reservation_logs 테이블의 모든 기록을 최신순으로 조회하여 반환"""
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        # 가장 최근에 생성된 로그가 맨 위로 오도록 내림차순 정렬
        sql = "SELECT * FROM reservation_logs ORDER BY created_at DESC;"
        cursor.execute(sql)
        logs = cursor.fetchall()
        
        return {
            "status": "success",
            "logs": logs
        }
    except Exception as e:
        return {
            "status": "fail",
            "message": str(e)
        }
    finally:
        cursor.close()
        conn.close()
