"""
Chapter 1: MCP 소개, 개념, 히스토리
- MCP의 역사와 Anthropic
- MCP란 무엇인가?
- Cursor + MCP의 시너지
- 개발 환경 설정
- FastMCP 소개
"""

print("=" * 80)
print("  Chapter 1: MCP 소개, 개념, 히스토리")
print("  " + "=" * 76)
print("  Cursor와 함께하는 AI 기반 개발 혁신")
print("=" * 80)

# ============================================
# 1. MCP의 역사와 탄생 배경
# ============================================
"""
📜 MCP의 역사

2023년 11월
  └─> Anthropic이 MCP (Model Context Protocol) 공식 발표
      ├─ Claude를 만든 Anthropic의 새로운 도전
      ├─ "읽기만 하는 AI"에서 "행동하는 AI"로의 진화
      └─ 안전하고 표준화된 AI 도구 사용 프로토콜

2024년 1월
  └─> Python SDK, TypeScript SDK 오픈 소스 공개
      └─ 개발자 커뮤니티에 공개

2024년 3월
  └─> Cursor가 공식 MCP 지원 시작
      └─ AI 코딩 도구의 새로운 시대 개막

2024년 6월
  └─> 500개 이상의 커뮤니티 MCP 서버 등장
      ├─ 파일 시스템, GitHub, Google Drive
      ├─ 데이터베이스, 웹 검색
      └─ API 통합, 자동화 도구

현재 (2024년 말~2025년)
  └─> 글로벌 개발자들이 Cursor + MCP로 생산성 혁신 중
      └─ 수동 작업 → AI 자동화로 패러다임 전환
"""

# ============================================
# 2. 왜 Cursor + MCP인가?
# ============================================
"""
🎯 교육 목적: Cursor를 통한 개발 효율성 극대화

현대 개발 환경에서 Cursor는 AI 기반 코딩의 중심입니다.
하지만 기본 Cursor는 "조언"만 할 뿐, "행동"하지 못합니다.
MCP는 Cursor에게 실제로 작업을 수행할 수 있는 능력을 부여합니다.

Before MCP (기존 Cursor):
  개발자: "이 폴더의 모든 Python 파일을 분석해줘"
  AI: "파일을 업로드하거나 내용을 붙여넣어 주세요"
  개발자: (수동으로 하나씩 복사...) 😓

After MCP (Cursor + MCP):
  개발자: "이 폴더의 모든 Python 파일을 분석해줘"
  AI: [자동으로 파일 읽기 → 분석 → 결과 제공] ✨
  개발자: (커피 한 잔 마시는 중) ☕

Cursor + MCP의 장점:
├─ 🚀 생산성 10배 향상: 반복 작업 자동화
├─ 🔧 맞춤형 도구: 프로젝트별 특화 기능
├─ 🎨 워크플로우 혁신: 파일, DB, API 자동 처리
└─ 💡 실시간 통합: 코딩과 동시에 도구 실행
"""

# ============================================
# 3. MCP란?
# ============================================
"""
MCP (Model Context Protocol)란?
- AI 모델(Claude, Cursor 등)이 외부 도구와 데이터에 접근할 수 있게 하는 프로토콜
- Anthropic이 개발한 오픈 소스 표준
- AI 에이전트가 다양한 리소스와 상호작용할 수 있게 함

핵심 구성 요소:
1. Server: 도구와 리소스를 제공하는 MCP 서버
2. Client: AI가 실행되는 환경 (Cursor, Claude Desktop 등)
3. Tools: AI가 실행할 수 있는 함수들
4. Resources: AI가 접근할 수 있는 데이터
5. Prompts: 미리 정의된 프롬프트 템플릿

실무 활용 사례:
├─ 파일 관리: 자동 읽기/쓰기/수정
├─ 웹 크롤링: 실시간 데이터 수집
├─ API 호출: 외부 서비스 통합
├─ 데이터베이스: SQL 쿼리 자동 실행
└─ Git 작업: 커밋, 푸시, PR 자동화
"""

# ============================================
# 2. FastMCP란?
# ============================================
"""
FastMCP란?
- MCP 서버를 빠르고 쉽게 만들 수 있는 Python 라이브러리
- 최소한의 코드로 강력한 MCP 서버 구축
- 자동으로 타입 검증 및 문서화
- 간단한 데코레이터 기반 API

FastMCP의 특징:
- 🚀 빠른 개발: 몇 줄의 코드로 서버 생성
- 📝 자동 문서화: 타입 힌트로 자동 문서 생성
- 🔧 간편한 디버깅: 내장 개발 서버
- 🎯 타입 안전성: Pydantic 기반 검증

설치:
pip install fastmcp
"""

# ============================================
# 3. MCP 서버의 구조
# ============================================
"""
MCP 서버 구조:

┌─────────────────────────────────────────┐
│          AI Client (Cursor)             │
│  - 사용자와 상호작용                      │
│  - MCP 서버에 요청 전송                   │
└────────────┬────────────────────────────┘
             │ MCP Protocol
             ↓
┌─────────────────────────────────────────┐
│         MCP Server (FastMCP)            │
│  ┌─────────────────────────────────┐   │
│  │ Tools (함수)                     │   │
│  │  - 계산기                        │   │
│  │  - 파일 읽기                     │   │
│  │  - API 호출                      │   │
│  └─────────────────────────────────┘   │
│  ┌─────────────────────────────────┐   │
│  │ Resources (데이터)               │   │
│  │  - 파일 시스템                   │   │
│  │  - 데이터베이스                  │   │
│  └─────────────────────────────────┘   │
│  ┌─────────────────────────────────┐   │
│  │ Prompts (템플릿)                 │   │
│  │  - 코드 리뷰                     │   │
│  │  - 문서 작성                     │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
"""

# ============================================
# 4. 개발 환경 설정
# ============================================
"""
1. Python 설치 확인:
   python --version  (3.10 이상 권장)

2. FastMCP 설치:
   pip install fastmcp

3. 추가 라이브러리 (필요 시):
   pip install httpx      # HTTP 요청
   pip install python-dotenv  # 환경변수 관리

4. IDE 설정:
   - VS Code 또는 Cursor 사용 권장
   - Python 확장 설치
"""

def print_installation_guide():
    """설치 가이드 출력"""
    print("\n" + "=" * 60)
    print("  FastMCP 설치 가이드")
    print("=" * 60)
    
    guide = """
    # 1. Python 버전 확인
    python --version
    
    # 2. 가상환경 생성 (권장)
    python -m venv venv
    
    # Windows
    venv\\Scripts\\activate
    
    # Mac/Linux
    source venv/bin/activate
    
    # 3. FastMCP 설치
    pip install fastmcp
    
    # 4. 설치 확인
    python -c "import fastmcp; print(fastmcp.__version__)"
    
    # 5. 개발 도구 설치 (선택)
    pip install httpx python-dotenv
    """
    
    print(guide)

# ============================================
# 5. Hello World MCP 서버
# ============================================
"""
가장 간단한 MCP 서버 예제:

```python
from fastmcp import FastMCP

# MCP 서버 인스턴스 생성
mcp = FastMCP("Hello MCP")

# 간단한 도구 추가
@mcp.tool()
def greet(name: str) -> str:
    '''사용자에게 인사하는 도구'''
    return f"안녕하세요, {name}님!"

# 서버 실행
if __name__ == "__main__":
    mcp.run()
```

실행 방법:
1. 파일 저장: hello_mcp.py
2. 실행: python hello_mcp.py
3. 또는: fastmcp dev hello_mcp.py
"""

# ============================================
# 6. MCP 서버 실행 방법
# ============================================
"""
MCP 서버 실행 방법 3가지:

1. 직접 실행:
   python your_server.py

2. FastMCP CLI 사용 (개발 모드):
   fastmcp dev your_server.py
   
   장점:
   - 자동 재시작
   - 상세한 로그
   - 디버깅 용이

3. 프로덕션 실행:
   fastmcp run your_server.py
   
   장점:
   - 최적화된 성능
   - 안정적인 실행

MCP 서버 테스트:
- fastmcp install your_server.py
- 클라이언트(Cursor)에서 테스트
"""

# ============================================
# Main 실행
# ============================================
if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  MCP 기초 개념")
    print("=" * 60)
    
    print("\n✅ MCP란?")
    print("   AI 모델이 외부 도구와 데이터에 접근할 수 있게 하는 프로토콜")
    
    print("\n✅ FastMCP란?")
    print("   MCP 서버를 쉽게 만들 수 있는 Python 라이브러리")
    
    print("\n✅ 주요 구성요소:")
    print("   1. Tools - AI가 실행할 수 있는 함수")
    print("   2. Resources - AI가 접근할 수 있는 데이터")
    print("   3. Prompts - 미리 정의된 프롬프트 템플릿")
    
    print_installation_guide()
    
    print("\n" + "=" * 60)
    print("  Section 1 완료!")
    print("=" * 60)

"""
학습 정리:

1. MCP는 AI 모델과 외부 도구를 연결하는 프로토콜
2. FastMCP로 간단하게 MCP 서버 구축 가능
3. Tools, Resources, Prompts 3가지 주요 개념
4. Python 3.10+ 환경에서 개발
5. fastmcp dev 명령으로 개발 서버 실행

다음 섹션에서는:
- 실제 MCP 서버 만들기
- Tools 추가하는 방법
- Cursor에 연동하기
"""

