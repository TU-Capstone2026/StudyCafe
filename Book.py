class Book:
    def __init__(self, cursor):
        self.cursor = cursor

    def check_in(self, seat_number):
        """[입실] 상태를 '이용중'으로 최신화"""
        # 상태를 '이용중' 문자열로 업데이트합니다.
        sql = "UPDATE seats SET status = '이용중' WHERE seat_number = ?"
        self.cursor.execute(sql, (seat_number,))
        print(f"{seat_number}번 좌석 상태가 '이용중'으로 변경되었습니다.")

    def check_out(self, seat_number):
        """[퇴실] 상태를 '이용가능'으로 최신화"""
        # 상태를 다시 '이용가능' 문자열로 업데이트합니다.
        sql = "UPDATE seats SET status = '이용가능' WHERE seat_number = ?"
        self.cursor.execute(sql, (seat_number,))
        print(f"{seat_number}번 좌석 상태가 '이용가능'으로 변경되었습니다.")