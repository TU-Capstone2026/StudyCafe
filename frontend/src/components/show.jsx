import { useEffect, useState } from 'react'

function Show() {
  const [seats, setSeats] = useState([])

  // 1. 좌석 목록 불러오기 함수
  const fetchSeats = () => {
    fetch('http://127.0.0.1:8000/show')
      .then((res) => res.json())
      .then((data) => {
        if (data.status === 'success') {
          setSeats(data.seats)
        }
      })
      .catch((err) => console.error("좌석 목록 조회 실패:", err))
  }

  useEffect(() => {
    fetchSeats()
  }, [])

  // 2. 좌석 클릭 이벤트 처리 (입장 & 퇴실 분기)
  const handleSeatClick = (seat) => {
    // A. 이미 사용 중(reserved)인 좌석 클릭 시 -> 퇴실(취소) 처리
    if (seat.status === 'reserved') {
      const isConfirmed = window.confirm(`[퇴실 확인] ${seat.seat_number} 좌석을 퇴실하시겠습니까?`)
      if (!isConfirmed) return

      fetch(`http://127.0.0.1:8000/cancel/${seat.seat_number}/`, {
        method: 'DELETE',
      })
        .then((res) => {
          if (res.ok) {
            alert(`[퇴실 완료] ${seat.seat_number} 좌석이 퇴실 처리되었습니다.`)
            fetchSeats() // DB 변경 사항 반영을 위해 목록 새로고침
          } else {
            alert(`[퇴실 실패] 퇴실 처리에 실패했습니다.`)
          }
        })
        .catch((err) => {
          console.error("퇴실 요청 오류:", err)
          alert("서버 연결에 실패했습니다.")
        })
      return
    }

    // B. 빈 좌석(available) 클릭 시 -> 입장 처리
    const isConfirmed = window.confirm(`[입장 확인] ${seat.seat_number} 좌석에 입장하시겠습니까?`)
    if (!isConfirmed) return

    fetch('http://127.0.0.1:8000/add', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ seat_number: seat.seat_number }),
    })
      .then((res) => {
        if (res.ok) {
          alert(`[입장 성공] ${seat.seat_number} 좌석 처리가 완료되었습니다.`)
          fetchSeats() // DB 변경 사항 반영을 위해 목록 새로고침
        } else {
          alert(`[입장 실패] 요청 처리 중 오류가 발생했습니다.`)
        }
      })
      .catch((err) => {
        console.error("입장 요청 오류:", err)
        alert("서버 연결에 실패했습니다.")
      })
  }

  return (
    <div style={{ marginTop: '20px' }}>
      <h2>전체 좌석 현황</h2>
      <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap', marginTop: '10px' }}>
        {seats.map((seat) => (
          <div
            key={seat.seat_id || seat.seat_number}
            onClick={() => handleSeatClick(seat)}
            style={{
              border: '1px solid #ddd',
              padding: '15px',
              borderRadius: '8px',
              minWidth: '120px',
              backgroundColor: seat.status === 'available' ? '#e6fffa' : '#ffe3e3',
              cursor: 'pointer'
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