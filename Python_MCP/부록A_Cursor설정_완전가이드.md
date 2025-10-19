# Cursor MCP 설정 통합 예제

Python과 Node.js MCP 서버를 모두 Cursor에 등록하는 완전한 가이드입니다.

> **💡 설정 방법**: Cursor에서 `Ctrl+Shift+P` → "MCP Settings" 검색하여 직접 입력

## 🔧 완전한 설정 예제

### Python + Node.js 통합 설정

```json
{
  "mcpServers": {
    "python-hello": {
      "command": "python",
      "args": [
        "C:/Users/82104/Desktop/lecture/lecture-portfolio/Python_MCP/02_FastMCP_기본사용법.py"
      ],
      "disabled": false,
      "alwaysAllow": []
    },
    "python-file-manager": {
      "command": "python",
      "args": [
        "C:/Users/82104/Desktop/lecture/lecture-portfolio/Python_MCP/예제1_파일관리_MCP서버.py"
      ],
      "disabled": false
    },
    "python-web-scraper": {
      "command": "python",
      "args": [
        "C:/Users/82104/Desktop/lecture/lecture-portfolio/Python_MCP/예제2_웹검색_MCP서버.py"
      ],
      "disabled": false
    },
    "nodejs-example": {
      "command": "node",
      "args": [
        "C:/Users/82104/Desktop/lecture/lecture-portfolio/Python_MCP/예제3_NPM_서버예제/server.js"
      ],
      "disabled": false
    }
  }
}
```

## 📝 설정 요소 설명

### 기본 구조

```json
{
  "mcpServers": {
    "서버이름": {
      "command": "실행 명령어",
      "args": ["인자 배열"],
      "disabled": false,
      "alwaysAllow": [],
      "env": {}
    }
  }
}
```

### 각 필드 설명

| 필드 | 필수 | 설명 |
|------|------|------|
| `command` | ✅ | 실행할 명령어 (`python`, `node`, `npx` 등) |
| `args` | ✅ | 명령어에 전달할 인자 배열 |
| `disabled` | ❌ | true면 비활성화 (기본값: false) |
| `alwaysAllow` | ❌ | 항상 허용할 tool 목록 |
| `env` | ❌ | 환경변수 설정 |

## 🐍 Python 서버 설정 예제

### 방법 1: Python 직접 실행

```json
{
  "mcpServers": {
    "my-python-server": {
      "command": "python",
      "args": [
        "C:/full/path/to/server.py"
      ]
    }
  }
}
```

### 방법 2: 가상환경 Python 사용

```json
{
  "mcpServers": {
    "my-python-server": {
      "command": "C:/path/to/venv/Scripts/python.exe",
      "args": [
        "C:/full/path/to/server.py"
      ]
    }
  }
}
```

### 방법 3: FastMCP CLI 사용

```json
{
  "mcpServers": {
    "my-python-server": {
      "command": "fastmcp",
      "args": [
        "run",
        "C:/full/path/to/server.py"
      ]
    }
  }
}
```

## 🟢 Node.js 서버 설정 예제 (HTTP 방식)

### ⭐ 권장 방식: HTTP 서버 실행 + URL 연동

#### 1단계: HTTP 서버 실행

**Windows CMD/PowerShell:**
```bash
# 프로젝트 디렉토리로 이동
cd C:/path/to/your-mcp-project

# Express 설치 (최초 1회)
npm install express cors

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

**✅ 브라우저 테스트:**
- http://localhost:3000 접속
- 서버 정보 JSON 확인

**💡 팁:**
- HTTP 서버이므로 브라우저에서도 접속 가능
- API 테스트 도구(Postman, curl)로 테스트 가능
- 자동 재시작: `npm install -g nodemon` → `npm run dev`

#### 2단계: Cursor 설정 (URL 방식)

**Cursor에서 설정** (`Ctrl+Shift+P` → "MCP Settings"):

```json
{
  "mcpServers": {
    "my-node-server": {
      "url": "http://localhost:3000",
      "transport": "http"
    }
  }
}
```

**⚠️ 중요:**
- ✅ `url` 필드 사용 (command/args 아님!)
- ✅ HTTP 서버를 먼저 로컬에서 실행
- ✅ 포트 번호 확인 (기본: 3000)
- ✅ Cursor 재시작

### 🔄 개발 워크플로우

```bash
# 1. HTTP 서버 실행
cd your-mcp-project
npm start               # 서버 실행 (localhost:3000)

# 2. Cursor에서 URL 설정
# {"url": "http://localhost:3000", "transport": "http"}

# 3. 코드 수정 시
# Ctrl+C → npm start (재시작)
# 또는 nodemon으로 자동 재시작
```

### 📡 HTTP vs stdio 비교

| 항목 | stdio (Python) | HTTP (Node.js) |
|------|---------------|----------------|
| **설정** | command + args | url + transport |
| **통신** | 프로세스 직접 실행 | HTTP 요청/응답 |
| **테스트** | 어려움 | 브라우저/curl로 쉬움 |
| **디버깅** | 제한적 | 네트워크 도구 활용 |
| **확장성** | 단일 클라이언트 | 다중 클라이언트 |

## 🌍 환경변수 설정

### API 키 등 민감한 정보 전달

```json
{
  "mcpServers": {
    "api-server": {
      "command": "python",
      "args": [
        "C:/path/to/api_server.py"
      ],
      "env": {
        "API_KEY": "your-api-key-here",
        "DEBUG": "true",
        "DATABASE_URL": "sqlite:///data.db"
      }
    }
  }
}
```

### Python에서 환경변수 사용

```python
import os

API_KEY = os.getenv('API_KEY')
DEBUG = os.getenv('DEBUG', 'false') == 'true'
```

### Node.js에서 환경변수 사용

```javascript
const API_KEY = process.env.API_KEY;
const DEBUG = process.env.DEBUG === 'true';
```

## 🎯 실전 시나리오별 설정

### 시나리오 1: 개발 환경

```json
{
  "mcpServers": {
    "dev-tools": {
      "command": "python",
      "args": ["C:/dev/mcp/dev_tools.py"],
      "env": {
        "ENVIRONMENT": "development",
        "LOG_LEVEL": "DEBUG"
      }
    }
  }
}
```

### 시나리오 2: 프로덕션 환경

```json
{
  "mcpServers": {
    "prod-tools": {
      "command": "python",
      "args": ["C:/prod/mcp/tools.py"],
      "env": {
        "ENVIRONMENT": "production",
        "LOG_LEVEL": "ERROR"
      }
    }
  }
}
```

### 시나리오 3: 여러 서버 동시 사용

```json
{
  "mcpServers": {
    "file-tools": {
      "command": "python",
      "args": ["C:/mcp/file_server.py"]
    },
    "web-tools": {
      "command": "node",
      "args": ["C:/mcp/web_server.js"]
    },
    "db-tools": {
      "command": "python",
      "args": ["C:/mcp/db_server.py"],
      "env": {
        "DB_URL": "postgresql://localhost/mydb"
      }
    }
  }
}
```

## ✅ 설정 체크리스트

### 설정 전 확인사항

- [ ] Python 또는 Node.js 설치 확인
- [ ] MCP 서버 파일 경로 확인
- [ ] 절대 경로 사용
- [ ] 경로에 한글이 없는지 확인

### Python 서버 체크리스트

- [ ] `python --version` 실행 확인
- [ ] `pip install fastmcp` 설치 확인
- [ ] 서버 파일 단독 실행 테스트
- [ ] 경로를 역슬래시(\\) 또는 슬래시(/)로 통일

### Node.js 서버 체크리스트

- [ ] `node --version` 실행 확인
- [ ] `npm install` 완료
- [ ] `node server.js` 단독 실행 테스트
- [ ] package.json에 `"type": "module"` 설정

### Cursor 설정 체크리스트

- [ ] cline_mcp_settings.json 파일 찾기
- [ ] JSON 문법 오류 없는지 확인
- [ ] 설정 저장
- [ ] Cursor 완전 재시작
- [ ] 채팅에서 Tool 사용 확인

## 🐛 문제 해결

### 1. 서버가 시작되지 않음

**증상**: Cursor에서 MCP 서버를 찾을 수 없음

**해결**:
```bash
# 1. 명령어 경로 확인
where python  # Windows
where node

# 2. 서버 파일 직접 실행 테스트
python C:/path/to/server.py
node C:/path/to/server.js

# 3. 경로 확인
# 절대 경로 사용, 슬래시(/) 사용
```

### 2. Tool이 표시되지 않음

**증상**: 서버는 실행되지만 Tool이 보이지 않음

**해결**:
- Cursor Developer Tools 열기 (Help → Toggle Developer Tools)
- Console에서 에러 메시지 확인
- 서버 코드에서 Tool 등록 확인

### 3. JSON 문법 오류

**증상**: 설정 파일 저장 시 오류

**해결**:
```json
// 잘못된 예 - 마지막 쉼표
{
  "mcpServers": {
    "server1": {...},  // ❌ 마지막 항목에 쉼표
  }
}

// 올바른 예
{
  "mcpServers": {
    "server1": {...}   // ✅ 마지막 쉼표 없음
  }
}
```

### 4. 환경변수가 적용되지 않음

**해결**:
```json
{
  "mcpServers": {
    "server": {
      "command": "python",
      "args": ["server.py"],
      "env": {
        "KEY": "value"  // 문자열로 작성
      }
    }
  }
}
```

## 📚 추가 팁

### 1. 서버 비활성화

일시적으로 서버를 끄고 싶을 때:

```json
{
  "mcpServers": {
    "my-server": {
      "command": "python",
      "args": ["server.py"],
      "disabled": true  // ✅ 비활성화
    }
  }
}
```

### 2. 특정 Tool 항상 허용

매번 확인하지 않고 자동 실행:

```json
{
  "mcpServers": {
    "my-server": {
      "command": "python",
      "args": ["server.py"],
      "alwaysAllow": ["read_file", "list_directory"]
    }
  }
}
```

### 3. 여러 버전 테스트

```json
{
  "mcpServers": {
    "server-dev": {
      "command": "python",
      "args": ["C:/dev/server.py"]
    },
    "server-prod": {
      "command": "python",
      "args": ["C:/prod/server.py"],
      "disabled": true  // 평소엔 꺼두기
    }
  }
}
```

## 🎓 학습 순서

1. **단일 Python 서버 설정** → 기본 동작 확인
2. **단일 Node.js 서버 설정** → 두 방식 비교
3. **여러 서버 동시 설정** → 복합 사용
4. **환경변수 활용** → 고급 설정

---

<div align="center">

**"Python과 Node.js, 두 가지 모두 활용하세요!"**

*상황에 맞는 최적의 도구를 선택하세요!*

</div>

