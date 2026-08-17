CREATE TABLE reservation_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    Member_ID INT,
    seat_number VARCHAR(10) NOT NULL,
    action VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT FK_log_member FOREIGN KEY (Member_ID) REFERENCES Member_Information(Member_ID)
) DEFAULT CHARSET=utf8mb4;