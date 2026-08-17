import { Routes, Route, Link } from 'react-router-dom'
import Show from './components/Show'
import Admin from './components/Admin'

function Home() {
  return (
    <div style={{ textAlign: 'center', padding: '40px 20px' }}>
      <h2 style={{ fontSize: '24px', marginBottom: '10px' }}>☕ 스터디카페 메인 홈</h2>
      <p style={{ color: '#6c757d', marginBottom: '30px' }}>원하는 기능을 선택해 주세요.</p>
      
      <div style={{ display: 'flex', justifyContent: 'center', gap: '20px' }}>
        <Link to="/show" style={{ textDecoration: 'none' }}>
          <div style={{ 
            padding: '20px 40px', 
            backgroundColor: '#f8f9fa', 
            border: '1px solid #dee2e6', 
            borderRadius: '8px',
            color: '#212529',
            fontWeight: 'bold',
            boxShadow: '0 4px 6px rgba(0,0,0,0.05)',
            transition: 'all 0.2s'
          }}>
            🪑 좌석 현황 보러가기
          </div>
        </Link>
      </div>
    </div>
  )
}

function App() {
  // 2. 상단 네비게이션 버튼 공통 스타일 지정
  const navButtonStyle = {
    padding: '8px 16px',
    backgroundColor: '#ffffff',
    border: '1px solid #ced4da',
    borderRadius: '6px',
    cursor: 'pointer',
    fontWeight: '600',
    color: '#495057',
    fontSize: '14px'
  };

  const adminButtonStyle = {
    ...navButtonStyle,
    backgroundColor: '#343a40',
    color: '#ffffff',
    border: 'none',
  };

  return (
    <div style={{ maxWidth: '900px', margin: '0 auto', padding: '20px', fontFamily: '"Pretendard", sans-serif' }}>
      
      {/* 헤더 부분 */}
      <header style={{ borderBottom: '3px solid #212529', paddingBottom: '15px', marginBottom: '20px' }}>
        <h1 style={{ margin: 0, color: '#212529' }}>스터디카페 예약 시스템</h1>
      </header>

      {/* 네비게이션 바 */}
      <nav style={{ display: 'flex', gap: '10px', alignItems: 'center', marginBottom: '20px' }}>
        <Link to="/"><button style={navButtonStyle}>🏠 홈으로</button></Link>
        <Link to="/show"><button style={navButtonStyle}>📋 전체 좌석 조회</button></Link>
        
        {/* 관리자 버튼은 우측 끝으로 밀어냅니다 (marginLeft: 'auto') */}
        <Link to="/admin" style={{ marginLeft: 'auto', textDecoration: 'none' }}>
          <button style={adminButtonStyle}>🛠️ 관리자 대시보드</button>
        </Link>
      </nav>

      {/* 라우터 화면이 렌더링되는 메인 영역 */}
      <main style={{ 
        minHeight: '400px', 
        backgroundColor: '#ffffff', 
        border: '1px solid #e9ecef',
        borderRadius: '12px',
        padding: '20px',
        boxShadow: '0 2px 10px rgba(0,0,0,0.02)'
      }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/show" element={<Show />} />
          <Route path="/admin" element={<Admin />} />
        </Routes>
      </main>

    </div>
  )
}

export default App