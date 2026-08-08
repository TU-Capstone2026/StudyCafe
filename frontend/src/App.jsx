import { Routes, Route, Link } from 'react-router-dom'
import Show from './components/Show'

// 임시 홈 화면 컴포넌트
function Home() {
  return (
    <div>
      <h2>스터디카페 메인 홈</h2>
      <p>원하는 기능을 선택해 주세요.</p>
    </div>
  )
}

function App() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>스터디카페 예약 시스템</h1>

      {/* 상단 버튼 네비게이션 바 */}
      <nav style={{ display: 'flex', gap: '10px', margin: '20px 0' }}>
        <Link to="/">
          <button>홈으로</button>
        </Link>
        <Link to="/show">
          <button>전체 좌석 조회</button>
        </Link>
        {/* 나중에 다른 팀원들 기능도 주소 연결 가능 */}
        {/* <Link to="/book"><button>좌석 예약</button></Link> */}
      </nav>

      <hr />

      {/* 주소에 따라 변경되는 화면 영역 */}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/show" element={<Show />} />
      </Routes>
    </div>
  )
}

export default App