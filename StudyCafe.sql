CREATE TABLE seats (
    seat_id     INT AUTO_INCREMENT PRIMARY KEY,
    seat_number VARCHAR(10) NOT NULL,
    status      VARCHAR(10) NOT NULL DEFAULT '이용가능',

    CONSTRAINT UQ_seats_seat_number UNIQUE (seat_number)
) DEFAULT CHARSET=utf8mb4;

