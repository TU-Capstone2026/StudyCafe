## requirement 적용방법

설치시
터미널에
pip install -r requirements.txt

실행시
uvicorn backend.fastapi_app:app --reload

fastapi 사용예시 -> backend.fastapi_app.py참고

# main 실행시:

    1. 터미널에서 cd backend 로 백엔드 이동
    2. uvicorn main:app --reload 실행

## 사이트 접속:

docs:
http://127.0.0.1:8000/docs
Redoc:
http://127.0.0.1:8000/redoc
