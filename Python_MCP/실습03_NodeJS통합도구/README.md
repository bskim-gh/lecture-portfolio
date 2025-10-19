# MCP HTTP 서버 예제 (Node.js)

Node.js와 Express를 사용한 **HTTP 방식 MCP 서버**입니다.

## 📦 설치

### 1. Node.js 설치 확인

```bash
node --version  # v18 이상
npm --version
```

### 2. 의존성 설치

```bash
npm install
```

**설치되는 패키지:**
- `express`: HTTP 서버
- `cors`: CORS 처리
- `nodemon`: 자동 재시작 (개발용)

## 🚀 서버 실행

### 방법 1: 일반 실행

```bash
npm start
```

또는

```bash
node server_http.js
```

**서버 실행 확인:**
```
============================================================
  MCP HTTP Server
============================================================
Server: mcp-http-server v1.0.0
Status: Running
URL: http://localhost:3000
Tools: 6개 등록됨
============================================================

Cursor 설정에 다음 URL을 입력하세요:
  http://localhost:3000
```

### 방법 2: 개발 모드 (자동 재시작)

```bash
npm run dev
```

코드를 수정하면 서버가 자동으로 재시작됩니다.

### 포트 변경

```bash
# Windows
set PORT=8080 && npm start

# Mac/Linux
PORT=8080 npm start
```

## 🔧 Cursor 연동 가이드

### ⭐ HTTP 방식 연동 (권장)

#### 1단계: 로컬에서 HTTP 서버 실행

**터미널 (CMD/PowerShell):**
```bash
# 프로젝트 디렉토리로 이동
cd C:/Users/82104/Desktop/lecture/lecture-portfolio/Python_MCP/실습03_NodeJS통합도구

# 의존성 설치 (최초 1회)
npm install

# HTTP 서버 실행
npm start
```

**서버 실행 확인:**
```
============================================================
  MCP HTTP Server
============================================================
Server: mcp-http-server v1.0.0
Status: Running
URL: http://localhost:3000
Tools: 6개 등록됨
============================================================

Cursor 설정에 다음 URL을 입력하세요:
  http://localhost:3000
```

**✅ 브라우저에서 확인:**
- http://localhost:3000 접속
- 서버 정보 JSON 출력 확인

#### 2단계: Cursor MCP 설정

**Cursor에서** (`Ctrl+Shift+P` → "MCP Settings" 검색):

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

**⚠️ 중요:**
- ✅ `url` 필드 사용 (command/args 아님!)
- ✅ 서버를 먼저 로컬에서 실행
- ✅ Cursor 완전 재시작
- ✅ 터미널은 서버 실행 중에 계속 유지

#### 3단계: 테스트

**API 테스트 (선택사항):**
```bash
# Tools 목록 확인
curl http://localhost:3000/tools

# Tool 실행 테스트
curl -X POST http://localhost:3000/execute \
  -H "Content-Type: application/json" \
  -d '{"tool": "greet", "arguments": {"name": "김철수"}}'
```

**Cursor 채팅에서:**
```
"안녕하세요라고 인사해줘"
→ AI가 HTTP로 greet tool 호출

"현재 시간 알려줘"
→ AI가 HTTP로 get_current_time tool 호출

"10 더하기 20 계산해줘"
→ AI가 HTTP로 calculate tool 호출
```

### 🔄 개발 워크플로우

```
┌─────────────────────────────┐
│ 터미널: HTTP 서버 실행       │
│ $ npm start                 │
│ Server running on :3000     │
│ (이 창은 계속 유지)          │
└──────────────┬──────────────┘
               │
               │ HTTP 통신
               │
┌──────────────▼──────────────┐
│ Cursor                      │
│ - URL: http://localhost:3000│
│ - 채팅에서 Tool 사용         │
│ - HTTP POST로 Tool 실행      │
└──────────────┬──────────────┘
               │
               │ 코드 수정 시
               ▼
┌─────────────────────────────┐
│ 1. Ctrl+C (서버 중지)        │
│ 2. 코드 수정                 │
│ 3. npm start (재시작)        │
│ 4. Cursor 자동 재연결        │
└─────────────────────────────┘
```

**💡 자동 재시작 (개발 편의):**
```bash
npm run dev
# nodemon이 파일 변경 감지하여 자동 재시작
```

## 🛠️ 제공되는 Tools

1. **greet** - 사용자에게 인사
2. **calculate** - 계산기 (+, -, *, /)
3. **get_current_time** - 현재 시간
4. **read_file** - 파일 읽기
5. **write_file** - 파일 쓰기
6. **list_directory** - 디렉토리 탐색

## 💬 Cursor에서 사용 예시

```
사용자: "안녕하세요라고 인사해줘"
AI: [greet tool 호출]

사용자: "10 곱하기 5를 계산해줘"
AI: [calculate tool 호출]

사용자: "현재 시간은?"
AI: [get_current_time tool 호출]

사용자: "현재 디렉토리의 파일 목록을 보여줘"
AI: [list_directory tool 호출]
```

## 📝 파일 구조

```
예제3_NPM_서버예제/
├── package.json    # NPM 설정
├── server.js       # MCP 서버 코드
└── README.md       # 이 파일
```

## 🔍 디버깅

서버가 실행되면 다음과 같은 로그가 표시됩니다:

```
============================================================
  Example MCP Server (Node.js)
============================================================
Server: example-mcp-server v1.0.0
Status: Running on stdio
Tools: 6개 등록됨
============================================================
```

## ⚙️ package.json 주요 설정

- `"type": "module"` - ES6 모듈 사용
- `"bin"` - 실행 파일 설정
- `"scripts"` - npm 명령어
- `"engines"` - Node.js 버전 요구사항

## 🌐 관련 자료

- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [MCP 공식 문서](https://modelcontextprotocol.io/)
- [Node.js 문서](https://nodejs.org/docs/)

