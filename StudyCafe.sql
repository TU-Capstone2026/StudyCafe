CREATE TABLE seats (
    seat_id       INT IDENTITY(1,1) PRIMARY KEY,      
    status        NVARCHAR(10)   NOT NULL DEFAULT '이용가능',

    CONSTRAINT UQ_seats_seat_number UNIQUE (seat_number)
);
