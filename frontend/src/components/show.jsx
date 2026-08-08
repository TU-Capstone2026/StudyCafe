import { useEffect, useState } from 'react'

function Show() {
  const [seats, setSeats] = useState([])

  // 컴포넌트가 마운트될 때 FastAPI (/show) 호출
  useEffect(() => {
    fetch('http://127.0.0.1:8000/show')
      .then((res) => res.json())
      .then((data) => {
        if (data.status === 'success') {
          setSeats(data.seats)
        }
      })
      .catch((err) => console.error("좌석 목록 조회 실패:", err))
  }, [])

  return (
    <div style={{ marginTop: '20px' }}>
      <h2>전체 좌석 현황</h2>
      <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap', marginTop: '10px' }}>
        {seats.map((seat) => (
          <div
            key={seat.seat_id}
            style={{
              border: '1px solid #ddd',
              padding: '15px',
              borderRadius: '8px',
              minWidth: '120px',
              backgroundColor: seat.status === 'available' ? '#e6fffa' : '#ffe3e3'
            }}
          >
            <p><strong>좌석:</strong> {seat.seat_number}</p>
            <p><strong>상태:</strong> {seat.status}</p>
          </div>
        ))}
      </div>
    </div>
  )
}

export default Show