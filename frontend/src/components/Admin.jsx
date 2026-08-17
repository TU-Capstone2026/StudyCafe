import { useEffect, useState } from 'react'

function Admin() {
  const [logs, setLogs] = useState([])

  // 화면이 켜질 때 백엔드(/admin/logs)에 로그 데이터 요청
  useEffect(() => {
    fetch('http://127.0.0.1:8000/admin/logs')
      .then((res) => res.json())
      .then((data) => {
        if (data.status === 'success') {
          setLogs(data.logs)
        }
      })
      .catch((err) => console.error("로그 조회 실패:", err))
  }, [])

  return (
    <div style={{ marginTop: '20px' }}>
      <h2>스터디카페 관리자 대시보드</h2>
      <p>실시간 예약 및 취소 현황을 확인합니다.</p>
      
      <table border="1" cellPadding="10" style={{ width: '100%', marginTop: '20px', borderCollapse: 'collapse', textAlign: 'center' }}>
        <thead style={{ backgroundColor: '#f4f4f4' }}>
          <tr>
            <th>로그 번호</th>
            <th>회원 번호</th>
            <th>좌석 번호</th>
            <th>동작 (Action)</th>
            <th>발생 시간</th>
          </tr>
        </thead>
        <tbody>
          {logs.map((log) => (
            <tr key={log.log_id}>
              <td>{log.log_id}</td>
              <td>{log.Member_ID ? `${log.Member_ID}번 회원` : '비회원'}</td>
              <td><strong>{log.seat_number}</strong></td>
              <td style={{ 
                color: log.action === 'RESERVE' ? '#007bff' : '#dc3545', 
                fontWeight: 'bold' 
              }}>
                {log.action === 'RESERVE' ? '예약' : '취소'}
              </td>
              <td>{new Date(log.created_at).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default Admin