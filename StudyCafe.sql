CREATE TABLE seats (
    seat_id     INT AUTO_INCREMENT PRIMARY KEY,
    seat_number VARCHAR(10) NOT NULL,
    status      VARCHAR(10) NOT NULL DEFAULT 'available',

    CONSTRAINT UQ_seats_seat_number UNIQUE (seat_number)
) DEFAULT CHARSET=utf8mb4;

-- 아래는 Oracle용
CREATE TABLE seats (
    seat_id     NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    seat_number VARCHAR2(10 CHAR) NOT NULL,
    status      VARCHAR2(10 CHAR) DEFAULT '이용가능' NOT NULL,

    CONSTRAINT UQ_seats_seat_number UNIQUE (seat_number)
);