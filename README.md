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

#Frontend 실행법

cd frontend
npm install

이후, 터미널 2개를 열기.

첫 번째 터미널: 서버 열기
cd backend
source ../venv/bin/activate
uvicorn main:app --reload

(테스트 주소는 127.0.0.1:8000)

두 번째 터미널: React/Vite 실행
cd frontend
npm run dev

접속 주소는 localhost:5173
