from show import show_all_seats
from cancel_seat import cancel_seat
from Book import Book
from add_seat import add_seat
from fastapi import FastAPI, Response

app = FastAPI(
    title="StudyCafe API",
    description="스터디카페 예약 시스템 백엔드 API"
)

@app.get("/")
def read_root():
    return {
        "status":"success",
        "message":"스터디카페 예약 시스템 API 서버가 정상 작동 중입니다."
    }

@app.get("/show")
def get_seats():
    seats = show_all_seats()
    return {
        "status": "success",
        "seats": seats
    }

@app.delete("/cancel/{seat_number}/")
def cancel_seats(seat_number:str, response: Response):
    result = cancel_seat(seat_number)
    if result == 1:
        return{
            "status": "success"
        }
    elif result == 404:
        response.status_code = 404
        return{
            "statuscode": 404,
            "status": "fail"
        }
    elif result == 500:
        response.status_code = 500
        return{
            "statuscode": 500,
            "status": "fail"
        }




def main():
    print("스터디카페 예약 시스템을 시작합니다.")
    show_all_seats()
    book = Book(None)
    add_seat("A-101")
    show_all_seats()
    book.check_in("1A")
    book.check_out("1A")
    print("작업이 완료되었습니다.")

if __name__ == "__main__":
    main()

