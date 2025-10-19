# MCP 서버 개발 교육 자료

> **Cursor와 함께하는 AI 기반 개발 혁신**  
> Python FastMCP와 Node.js로 나만의 AI 도구를 만들어보세요!

<div align="center">

**개발 환경**: Windows 10/11 + Python 3.10+ / Node.js 18+ + Cursor

---

### 🎯 교육 목적

현대 개발 환경에서 **Cursor**는 AI 기반 코딩 도구로 많은 개발자들이 사용하고 있습니다.  
하지만 Cursor의 진정한 잠재력은 **MCP(Model Context Protocol)**를 통해 발휘됩니다.

본 교육은 다음을 목표로 합니다:
- 🚀 **개발 효율성 극대화**: AI가 반복 작업을 자동으로 처리
- 🔧 **맞춤형 도구 제작**: 프로젝트에 특화된 AI 도구 개발
- 🎨 **워크플로우 혁신**: 파일 관리, 데이터 수집, API 호출 등 자동화
- 💡 **AI 활용 확장**: Cursor + MCP로 개발 생산성 10배 향상

**"Cursor로 코딩하고 있다면, MCP는 필수입니다!"**

</div>

---

## 📜 MCP의 역사

### MCP란?

**MCP (Model Context Protocol)**은 AI 모델이 외부 도구와 데이터에 접근할 수 있게 하는 **개방형 프로토콜**입니다.

### 탄생 배경

<div align="center">

```
2023년 11월 → Anthropic이 MCP 발표
         ↓
      2024년 초 → 오픈 소스로 공개
         ↓
      2024년 중 → Cursor, Claude Desktop 공식 지원
         ↓
      현재 → 수백 개의 커뮤니티 서버 개발 중
```

</div>

#### 🏢 **Anthropic의 비전**
- Claude를 만든 Anthropic이 2023년 11월에 공식 발표
- AI가 "읽기만" 하던 시대에서 "행동하는" AI로의 진화
- 안전하고 표준화된 방식으로 AI가 도구를 사용할 수 있게 함

#### 🌍 **커뮤니티 성장**
- **2024년 1월**: Python SDK, TypeScript SDK 공개
- **2024년 3월**: Cursor 공식 MCP 지원 시작
- **2024년 6월**: 500개 이상의 커뮤니티 MCP 서버 등장
- **현재**: 파일 시스템, GitHub, Google Drive, 데이터베이스 등 다양한 영역 지원

#### 🚀 **왜 Cursor + MCP인가?**

| 기존 Cursor | Cursor + MCP |
|------------|--------------|
| 코드 작성만 도움 | 코드 작성 + 실행 + 데이터 수집 |
| 제한된 정보 접근 | 파일, API, DB 모두 접근 |
| 일반적인 답변 | 프로젝트 맞춤형 작업 |
| 수동 복사-붙여넣기 | AI가 직접 파일 수정 |

### MCP가 해결하는 문제

**Before MCP:**
```
개발자: "이 폴더의 모든 Python 파일을 분석해줘"
AI: "파일을 업로드하거나 내용을 붙여넣어 주세요"
개발자: (수동으로 하나씩 복사...) 😓
```

**After MCP:**
```
개발자: "이 폴더의 모든 Python 파일을 분석해줘"
AI: [자동으로 파일 읽기 → 분석 → 결과 제공] ✨
개발자: (커피 한 잔 마시는 중) ☕
```

---

## 📚 MCP 핵심 개념

### 주요 개념
- 🔧 **Tools**: AI가 실행할 수 있는 함수
- 📦 **Resources**: AI가 접근할 수 있는 데이터  
- 📝 **Prompts**: 미리 정의된 프롬프트 템플릿

### 개발 방식

이 교육 자료는 **두 가지 방식**의 MCP 서버 개발을 다룹니다:

#### 🐍 Python (FastMCP)
- 간단한 데코레이터 기반
- 빠른 프로토타이핑
- Python 생태계 활용

#### 🟢 Node.js (MCP SDK)
- 공식 TypeScript SDK
- 높은 성능
- NPM 생태계 활용

---

---

## 📚 강의 커리큘럼

본 교육은 **이론 → 실습 → 응용** 순서로 진행됩니다.

### 📘 Chapter 1: MCP 소개 및 개념 (01_MCP소개_개념_히스토리.py)
**주요 학습 내용:**
- MCP와 FastMCP 소개
- MCP 서버 구조 이해
- 개발 환경 설정
- Hello World MCP 서버

**학습 시간:** 1-2시간

---

### 📗 Chapter 2: Python FastMCP 기초 (02_Python_FastMCP_기초.py)
**주요 학습 내용:**
- MCP 인스턴스 생성
- Tool(도구) 추가 방법
- 타입 힌트와 검증
- 에러 처리
- 다양한 Tool 예제
  - 계산기
  - 문자열 처리
  - 파일 작업
  - JSON 처리

**학습 시간:** 2-3시간

---

### 📙 Chapter 3: Cursor 연동 실습 (03_Cursor연동_설정_가이드.md)
**주요 학습 내용:**
- MCP 서버 로컬 실행 방법
- Cursor MCP 설정 파일 작성
- Cursor에 MCP 서버 등록
- 테스트 및 디버깅
- 실전 사용 가이드

**학습 시간:** 2-3시간

---

### 📕 Chapter 4: Node.js MCP 개발 (04_NodeJS_MCP_가이드.md)
**주요 학습 내용:**
- Node.js 설치 및 환경 설정
- MCP TypeScript SDK 사용
- JavaScript로 MCP 서버 만들기
- Python vs Node.js 비교
- NPM 생태계 활용

**학습 시간:** 2-3시간

---

## 🎯 실전 프로젝트

### 💼 Project 1: 파일 관리 시스템 (실습01_파일관리시스템.py)
**난이도:** ⭐⭐  
**언어:** Python  
**학습 목표:**
- 파일 시스템 자동화
- Cursor에서 AI로 파일 관리
- 실무 적용 가능한 도구 제작

**제공 기능:**
- 📄 파일 읽기/쓰기/추가
- 📁 디렉토리 탐색
- 🔍 파일 검색
- ℹ️ 파일 정보 조회
- 📋 파일 복사/삭제

**실습 시나리오:**
```
개발자: "현재 프로젝트의 모든 Python 파일 목록을 보여줘"
AI: [list_directory + search_files 실행]

개발자: "README.md 파일을 수정해서 새 섹션을 추가해줘"
AI: [read_file → 분석 → write_file]
```

---

### 🌐 Project 2: 웹 데이터 수집 (실습02_웹데이터수집.py)
**난이도:** ⭐⭐⭐  
**언어:** Python  
**학습 목표:**
- 웹 스크래핑 자동화
- BeautifulSoup과 MCP 통합
- 데이터 수집 파이프라인 구축

**제공 기능:**
- 🌍 웹 페이지 가져오기
- 📊 HTML 파싱
- 🔗 링크/이미지 추출
- 📝 메타데이터 추출
- 🔎 키워드 검색

**실습 시나리오:**
```
개발자: "경쟁사 홈페이지의 최신 뉴스를 분석해줘"
AI: [fetch_url → extract_links → 내용 분석]

개발자: "이 기술 블로그에서 'Python' 관련 글을 찾아줘"
AI: [search_in_page → 결과 정리]
```

---

### 🟢 Project 3: Node.js 다목적 도구 (실습03_NodeJS통합도구/)
**난이도:** ⭐⭐  
**언어:** Node.js  
**학습 목표:**
- TypeScript/JavaScript로 MCP 개발
- 고성능 서버 구축
- Python과 Node.js 통합 활용

**제공 기능:**
- 👋 인사 및 대화 도구
- 🔢 고급 계산기
- ⏰ 시간/날짜 유틸리티
- 💾 파일 시스템 접근
- 📂 디렉토리 관리

**실습 시나리오:**
```
개발자: "오늘 날짜로 폴더를 만들고 작업 로그를 저장해줘"
AI: [get_current_time → create_directory → write_file]
```

---

## 📖 보충 학습 자료

### 📘 부록 A: Cursor 통합 설정 완전 가이드
**파일:** `부록A_Cursor설정_완전가이드.md`

Python과 Node.js 서버를 동시에 Cursor에 등록:
- 🔧 통합 설정 파일 템플릿
- 🌍 환경변수 관리
- 🚀 여러 서버 동시 운영
- 🐛 문제 해결 가이드
- ⚡ 성능 최적화 팁

### 📗 부록 B: Node.js MCP 완전 정복
**파일:** `부록B_NodeJS_MCP_완전정복.md`

Node.js 기반 MCP 서버 마스터하기:
- Node.js 설치 (3가지 방법)
- TypeScript 설정
- 공식 MCP SDK 심화
- Python vs Node.js 성능 비교
- 12개 GitHub 참고 프로젝트

---

## 🚀 시작하기

### 1. 필수 준비물

#### Python 방식

**Python 3.10 이상**
```bash
python --version
```

**FastMCP 설치**
```bash
pip install fastmcp
```

**추가 라이브러리 (예제용)**
```bash
pip install requests beautifulsoup4
```

#### Node.js 방식

**Node.js 18 이상 설치**
- 다운로드: https://nodejs.org/
- LTS 버전 권장

**설치 확인**
```bash
node --version
npm --version
```

**MCP SDK 설치**
```bash
npm install @modelcontextprotocol/sdk
```

상세 설치 가이드: [MCP_NPM_가이드.md](MCP_NPM_가이드.md)

### 2. Hello World 실행

**hello_mcp.py 생성:**
```python
from fastmcp import FastMCP

mcp = FastMCP("Hello MCP")

@mcp.tool()
def greet(name: str) -> str:
    '''사용자에게 인사하는 도구'''
    return f"안녕하세요, {name}님!"

if __name__ == "__main__":
    mcp.run()
```

**실행:**
```bash
# 개발 모드 (자동 재시작)
fastmcp dev hello_mcp.py

# 또는 직접 실행
python hello_mcp.py
```

### 3. Cursor에 연동하기

#### Step 1: Cursor MCP 설정 열기
- `Ctrl+Shift+P` (Mac: `Cmd+Shift+P`)
- "MCP Settings" 검색 및 선택

#### Step 2: 설정 파일 작성

**cline_mcp_settings.json:**
```json
{
  "mcpServers": {
    "my-mcp-server": {
      "command": "python",
      "args": [
        "C:/full/path/to/hello_mcp.py"
      ],
      "disabled": false
    }
  }
}
```

**주의사항:**
- ✅ 절대 경로 사용
- ✅ Windows: `\\` 또는 `/` 사용
- ✅ Python 경로 확인

#### Step 3: Cursor 재시작
- Cursor 완전 종료
- 다시 실행

#### Step 4: 테스트
- Cursor 채팅 창 열기
- "안녕하세요"라고 인사해줘" 입력
- AI가 `greet` tool 사용하는지 확인

---

## 💻 실행 방법

### 로컬에서 실행

#### 방법 1: 직접 실행
```bash
python your_mcp_server.py
```

#### 방법 2: FastMCP CLI (개발 모드, 추천)
```bash
fastmcp dev your_mcp_server.py
```

**장점:**
- 코드 변경 시 자동 재시작
- 상세한 로그 출력
- 디버깅 용이

#### 방법 3: FastMCP CLI (프로덕션)
```bash
fastmcp run your_mcp_server.py
```

### Cursor 설정 예시

#### Python 서버 설정
```json
{
  "mcpServers": {
    "python-file-manager": {
      "command": "python",
      "args": ["C:/path/to/예제1_파일관리_MCP서버.py"]
    },
    "python-web-scraper": {
      "command": "python",
      "args": ["C:/path/to/예제2_웹검색_MCP서버.py"]
    }
  }
}
```

#### Node.js 서버 설정 (HTTP 방식) ⭐

**1단계: 로컬에서 HTTP 서버 실행**
```bash
# CMD/PowerShell에서
cd C:/path/to/실습03_NodeJS통합도구
npm install
npm start
# 서버 실행됨: http://localhost:3000
```

**2단계: Cursor MCP 설정 (URL 방식)**
```json
{
  "mcpServers": {
    "nodejs-http-server": {
      "url": "http://localhost:3000",
      "transport": "http"
    }
  }
}
```

**💡 핵심:**
- ✅ HTTP 서버로 실행 (`npm start`)
- ✅ Cursor 설정에서 **URL** 방식 사용
- ✅ 브라우저에서도 확인 가능 (http://localhost:3000)

#### Python + Node.js 통합 설정

**Node.js HTTP 서버 먼저 실행:**
```bash
# 터미널 1
cd C:/mcp/node-project
npm start
# HTTP 서버: http://localhost:3000
```

**Cursor 설정:**
```json
{
  "mcpServers": {
    "python-tools": {
      "command": "python",
      "args": ["C:/mcp/python_server.py"]
    },
    "nodejs-http-tools": {
      "url": "http://localhost:3000",
      "transport": "http"
    }
  }
}
```

**차이점:**
- Python: `command` + `args` (stdio 방식)
- Node.js: `url` + `transport: "http"` (HTTP 방식)

**완전한 설정 가이드**: [Cursor_MCP_설정_통합예제.md](Cursor_MCP_설정_통합예제.md)

---

## 📝 학습 가이드

### 권장 학습 순서

1. **Section 1** - MCP 기초 개념 이해
2. **Section 2** - FastMCP 사용법 익히기
3. **Section 3** - 서버 실행 및 Cursor 연동
4. **예제 1** - 파일 관리 서버 실습
5. **예제 2** - 웹 검색 서버 실습
6. **응용** - 나만의 MCP 서버 만들기

### 학습 팁

- 💡 **코드 실행**: 각 예제를 직접 실행해보세요
- 🔧 **Tool 수정**: 기존 Tool을 수정하며 동작 이해
- 🎯 **새 Tool 추가**: 필요한 Tool을 직접 만들어보세요
- 🐛 **디버깅 연습**: 에러 메시지를 읽고 해결
- 📚 **공식 문서 참고**: [FastMCP 문서](https://github.com/jlowin/fastmcp)

---

## 🔧 문제 해결

### 1. MCP 서버가 실행되지 않음
```bash
# Python 경로 확인
where python  # Windows
which python  # Mac/Linux

# FastMCP 설치 확인
pip show fastmcp
```

### 2. Cursor에서 Tool이 호출되지 않음
- Cursor 설정 파일 문법 확인
- 파일 경로가 절대 경로인지 확인
- Cursor 완전 재시작
- Developer Tools (Help → Toggle Developer Tools) 에서 Console 확인

### 3. Tool 실행 오류
```python
# 에러 처리 추가
@mcp.tool()
def safe_tool(param: str) -> str:
    try:
        # 실행 코드
        return "성공"
    except Exception as e:
        return f"오류: {str(e)}"
```

### 4. 일반적인 문제

| 문제 | 원인 | 해결 |
|------|------|------|
| 서버 실행 안됨 | Python 경로 오류 | 절대 경로 사용 |
| Tool 없음 | 설정 오류 | 설정 파일 확인 |
| 권한 오류 | 파일 접근 권한 | 관리자 권한 실행 |
| 모듈 없음 | 라이브러리 미설치 | pip install 실행 |

---

## 📚 추가 학습 자료

### 공식 문서
- [MCP 공식 사이트](https://modelcontextprotocol.io/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [FastMCP (Python)](https://github.com/jlowin/fastmcp)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Cursor Documentation](https://docs.cursor.com/)

### GitHub MCP 서버 모음

#### 공식 서버
1. **MCP 공식 GitHub** - https://github.com/modelcontextprotocol
2. **MCP TypeScript SDK** - https://github.com/modelcontextprotocol/typescript-sdk
3. **MCP Python SDK** - https://github.com/modelcontextprotocol/python-sdk

#### 커뮤니티 서버
4. **Awesome MCP Servers** - https://github.com/punkpeye/awesome-mcp-servers
5. **MCP Server Examples** - https://github.com/wong2/mcp-server-examples
6. **File System MCP** - https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
7. **GitHub MCP** - https://github.com/modelcontextprotocol/servers/tree/main/src/github
8. **Brave Search MCP** - https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search
9. **Google Drive MCP** - https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive
10. **Postgres MCP** - https://github.com/modelcontextprotocol/servers/tree/main/src/postgres

#### 도구
11. **MCP Inspector** - https://github.com/modelcontextprotocol/inspector
12. **FastMCP** - https://github.com/jlowin/fastmcp

### 참고 자료
- [Anthropic Claude](https://www.anthropic.com/)
- [Python 타입 힌팅](https://docs.python.org/3/library/typing.html)
- [Pydantic](https://docs.pydantic.dev/)
- [Node.js 공식 문서](https://nodejs.org/docs/)
- [TypeScript](https://www.typescriptlang.org/)

---

## 💡 프로젝트 아이디어

### 초급
1. **할일 관리 MCP** (Python/Node.js): 할일 추가/조회/완료
2. **메모 MCP** (Python): 텍스트 메모 저장/검색
3. **계산기 MCP** (Node.js): 다양한 수학 계산

### 중급
1. **코드 분석 MCP** (Node.js): 코드 파일 분석 및 리뷰
2. **Git MCP** (Python): Git 명령 자동화
3. **데이터베이스 MCP** (Node.js): SQLite 조회/수정

### 고급
1. **API 통합 MCP** (Node.js): 여러 API 통합
2. **자동화 MCP** (Python): 업무 자동화 워크플로우
3. **AI 에이전트 MCP** (Python + Node.js): 복잡한 작업 자동 처리

### 언어 선택 가이드
- **Python 권장**: 데이터 분석, 머신러닝, 간단한 스크립트
- **Node.js 권장**: 웹 서비스, 실시간 처리, 고성능 필요 시

---

## 🎓 학습 체크리스트

### 기초 과정 - Python
- [ ] MCP 개념 이해
- [ ] FastMCP 설치 완료
- [ ] Hello World 서버 실행 성공
- [ ] Tool 만들기 성공

### 기초 과정 - Node.js
- [ ] Node.js 설치 완료
- [ ] MCP SDK 설치
- [ ] Hello World 서버 실행 성공
- [ ] Tool 등록 및 실행

### Cursor 연동
- [ ] Cursor MCP 설정 파일 작성
- [ ] Python 서버 등록
- [ ] Node.js 서버 등록
- [ ] Cursor 재시작
- [ ] 채팅에서 Tool 사용 확인

### 실전 프로젝트
- [ ] 파일 관리 서버 실행 (Python)
- [ ] 웹 검색 서버 실행 (Python)
- [ ] NPM 서버 실행 (Node.js)
- [ ] 나만의 Tool 추가
- [ ] Python + Node.js 통합 활용

---

## ⚠️ 주의사항

### 보안
- 민감한 정보를 Tool에 하드코딩하지 마세요
- 환경변수로 API 키 관리
- 파일 접근 권한 확인

### 성능
- 무거운 작업은 비동기 처리 고려
- 적절한 타임아웃 설정
- 에러 처리 필수

### 법적/윤리적
- 웹 스크래핑 시 robots.txt 확인
- 저작권 및 이용약관 준수
- API 사용 제한 확인

---

## 📞 도움받기

학습 중 어려움이 있다면:
1. 에러 메시지를 Google에 검색
2. FastMCP GitHub Issues 확인
3. Cursor 커뮤니티에 질문
4. 공식 문서 참고

---

## 📄 라이센스

이 교육 자료는 학습 목적으로 자유롭게 사용 가능합니다.

---

<div align="center">

**"Python과 Node.js, 두 가지 방법으로 MCP 서버를 만들어보세요!"**

*FastMCP와 MCP SDK로 나만의 AI 도구를 개발하세요!*

🐍 Python + 🟢 Node.js + 🤖 AI = ∞ 가능성

---

### 📂 강의 자료 구조

```
Python_MCP/
│
├── 📚 이론 학습 (강의 순서대로)
│   ├── 01_MCP소개_개념_히스토리.py         # Chapter 1: MCP 소개
│   ├── 02_Python_FastMCP_기초.py          # Chapter 2: Python 기초
│   ├── 03_Cursor연동_설정_가이드.md        # Chapter 3: Cursor 연동
│   └── 04_NodeJS_MCP_가이드.md            # Chapter 4: Node.js 개발
│
├── 💼 실습 프로젝트
│   ├── 실습01_파일관리시스템.py            # Project 1: 파일 관리
│   ├── 실습02_웹데이터수집.py              # Project 2: 웹 크롤링
│   └── 실습03_NodeJS통합도구/             # Project 3: Node.js 도구
│       ├── server.js                     # Node.js MCP 서버
│       ├── package.json                  # NPM 설정
│       └── README.md                     # 실습 가이드
│
├── 📖 보충 자료
│   ├── 부록A_Cursor설정_완전가이드.md      # 통합 설정 가이드
│   └── 부록B_NodeJS_MCP_완전정복.md       # Node.js 심화
│
└── README.md                              # 📌 이 파일 (강의 전체 가이드)
```

**📝 학습 순서:**
1. 이론 학습 (01 → 02 → 03 → 04)
2. 실습 프로젝트 (실습01 → 실습02 → 실습03)
3. 보충 자료 (필요시 참고)

</div>

