from show import show_all_seats
from Book import Book
from add_seat import add_seat

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

