CREATE TABLE Member_Information (
    Member_ID INT AUTO_INCREMENT,
    Member_Name VARCHAR(16) NOT NULL,
    Member_Address VARCHAR(50) DEFAULT NULL,
    Member_Email VARCHAR(12) DEFAULT NULL,
    Member_Phone VARCHAR(10) DEFAULT NULL,
    seat_id INT NOT NULL UNIQUE,

    PRIMARY KEY (Member_ID),
    CONSTRAINT FK_member_seat
        FOREIGN KEY (seat_id)
        REFERENCES seats(seat_id)
);
//비번 칼럼 수정
ALTER TABLE Member_Information
ADD COLUMN password_hash VARCHAR(255) NOT NULL;

//로그인 이메일 칼럼 수정
ALTER TABLE Member_Information
MODIFY Member_Email VARCHAR(100);
//좌석 낫널 수정
ALTER TABLE Member_Information
MODIFY seat_id INT NULL;
ALTER TABLE Member_Information
MODIFY Member_Phone VARCHAR(20);

