# MCP 서버 개발 가이드 - Node.js/NPM 버전

Node.js와 NPM을 사용하여 MCP(Model Context Protocol) 서버를 만드는 완전한 가이드입니다.

## 📦 Node.js 설치

### Windows 환경에서 Node.js 설치

#### 방법 1: 공식 설치 프로그램 (권장)

1. **Node.js 다운로드**
   - 공식 사이트: https://nodejs.org/
   - LTS 버전 다운로드 (현재 20.x 권장)
   - Windows Installer (.msi) 다운로드

2. **설치 진행**
   ```
   - Next 클릭
   - 라이선스 동의
   - 설치 경로 선택 (기본값 권장)
   - "Automatically install necessary tools" 체크
   - Install 클릭
   ```

3. **설치 확인**
   ```bash
   # 터미널(PowerShell 또는 CMD)에서 실행
   node --version
   # 출력 예: v20.10.0
   
   npm --version
   # 출력 예: 10.2.3
   ```

#### 방법 2: Chocolatey 사용

```powershell
# PowerShell (관리자 권한)
choco install nodejs-lts
```

#### 방법 3: Winget 사용

```powershell
# PowerShell
winget install OpenJS.NodeJS.LTS
```

---

## 🚀 MCP SDK 설치

### 공식 MCP SDK for TypeScript

```bash
# 새 프로젝트 디렉토리 생성
mkdir my-mcp-server
cd my-mcp-server

# package.json 초기화
npm init -y

# MCP SDK 설치
npm install @modelcontextprotocol/sdk

# TypeScript 설치 (선택사항이지만 권장)
npm install -D typescript @types/node

# 추가 유용한 패키지
npm install zod  # 데이터 검증
```

---

## 📝 MCP 서버 만들기

### 예제 1: Hello World MCP 서버

**server.js 생성:**

```javascript
#!/usr/bin/env node

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

// MCP 서버 생성
const server = new Server(
  {
    name: "hello-mcp-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Tools 목록 반환
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "greet",
        description: "사용자에게 인사하는 도구",
        inputSchema: {
          type: "object",
          properties: {
            name: {
              type: "string",
              description: "사용자 이름",
            },
          },
          required: ["name"],
        },
      },
      {
        name: "calculate",
        description: "두 숫자를 더하는 계산기",
        inputSchema: {
          type: "object",
          properties: {
            a: {
              type: "number",
              description: "첫 번째 숫자",
            },
            b: {
              type: "number",
              description: "두 번째 숫자",
            },
          },
          required: ["a", "b"],
        },
      },
    ],
  };
});

// Tool 실행
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  switch (name) {
    case "greet":
      return {
        content: [
          {
            type: "text",
            text: `안녕하세요, ${args.name}님!`,
          },
        ],
      };

    case "calculate":
      const result = args.a + args.b;
      return {
        content: [
          {
            type: "text",
            text: `${args.a} + ${args.b} = ${result}`,
          },
        ],
      };

    default:
      throw new Error(`Unknown tool: ${name}`);
  }
});

// 서버 시작
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("MCP Server running on stdio");
}

main().catch((error) => {
  console.error("Server error:", error);
  process.exit(1);
});
```

### package.json 수정

```json
{
  "name": "hello-mcp-server",
  "version": "1.0.0",
  "type": "module",
  "description": "Hello World MCP Server",
  "main": "server.js",
  "bin": {
    "hello-mcp-server": "./server.js"
  },
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "^0.5.0"
  },
  "engines": {
    "node": ">=18"
  }
}
```

### 서버 실행

```bash
# 직접 실행
node server.js

# 또는 npm script 사용
npm start
```

---

## 🔧 Cursor에 MCP 서버 연동 (HTTP 방식)

### HTTP 서버로 실행

#### 1단계: HTTP 서버 실행

**Windows CMD/PowerShell:**
```bash
# 프로젝트 디렉토리로 이동
cd C:/full/path/to/my-mcp-server

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
URL: http://localhost:3000
Tools: 6개 등록됨
============================================================
```

#### 2단계: Cursor MCP 설정 (URL 방식)

**Cursor에서** (`Ctrl+Shift+P` → "MCP Settings"):

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

**💡 워크플로우:**
1. 터미널에서 `npm start` 실행 (HTTP 서버)
2. Cursor에 URL 설정 추가
3. Cursor 재시작
4. 브라우저에서도 테스트 가능!

---

## 📚 실전 예제

### 예제 2: 파일 시스템 MCP 서버

**filesystem-server.js:**

```javascript
#!/usr/bin/env node

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import fs from "fs/promises";
import path from "path";

const server = new Server(
  {
    name: "filesystem-mcp-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Tools 정의
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "read_file",
        description: "파일 내용을 읽습니다",
        inputSchema: {
          type: "object",
          properties: {
            filepath: {
              type: "string",
              description: "읽을 파일 경로",
            },
          },
          required: ["filepath"],
        },
      },
      {
        name: "write_file",
        description: "파일에 내용을 씁니다",
        inputSchema: {
          type: "object",
          properties: {
            filepath: {
              type: "string",
              description: "저장할 파일 경로",
            },
            content: {
              type: "string",
              description: "저장할 내용",
            },
          },
          required: ["filepath", "content"],
        },
      },
      {
        name: "list_directory",
        description: "디렉토리 내용을 나열합니다",
        inputSchema: {
          type: "object",
          properties: {
            directory: {
              type: "string",
              description: "탐색할 디렉토리 경로",
            },
          },
          required: ["directory"],
        },
      },
    ],
  };
});

// Tool 실행
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  try {
    switch (name) {
      case "read_file": {
        const content = await fs.readFile(args.filepath, "utf-8");
        return {
          content: [
            {
              type: "text",
              text: `파일 내용:\n${content}`,
            },
          ],
        };
      }

      case "write_file": {
        await fs.writeFile(args.filepath, args.content, "utf-8");
        return {
          content: [
            {
              type: "text",
              text: `✅ 파일 저장 완료: ${args.filepath}`,
            },
          ],
        };
      }

      case "list_directory": {
        const files = await fs.readdir(args.directory, { withFileTypes: true });
        const fileList = files
          .map((file) => {
            const icon = file.isDirectory() ? "📁" : "📄";
            return `${icon} ${file.name}`;
          })
          .join("\n");

        return {
          content: [
            {
              type: "text",
              text: `디렉토리: ${args.directory}\n\n${fileList}`,
            },
          ],
        };
      }

      default:
        throw new Error(`Unknown tool: ${name}`);
    }
  } catch (error) {
    return {
      content: [
        {
          type: "text",
          text: `❌ 오류: ${error.message}`,
        },
      ],
      isError: true,
    };
  }
});

// 서버 시작
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Filesystem MCP Server running");
}

main().catch(console.error);
```

---

## 🆚 Python vs NPM 비교

| 항목 | Python (FastMCP) | Node.js (MCP SDK) |
|------|------------------|-------------------|
| **설치** | `pip install fastmcp` | `npm install @modelcontextprotocol/sdk` |
| **언어** | Python | JavaScript/TypeScript |
| **난이도** | 쉬움 (데코레이터 사용) | 중간 (이벤트 핸들러) |
| **타입 안전성** | Pydantic | Zod 또는 TypeScript |
| **성능** | 중간 | 빠름 (비동기 I/O) |
| **생태계** | Python 라이브러리 | NPM 패키지 |

### Cursor 설정 비교 (Python vs Node.js)

```json
{
  "mcpServers": {
    "python-server": {
      "command": "python",
      "args": ["C:/path/to/server.py"]
    },
    "nodejs-http-server": {
      "url": "http://localhost:3000",
      "transport": "http"
    }
  }
}
```

**로컬 개발:**
```bash
# Python (stdio 방식)
python server.py

# Node.js (HTTP 서버 방식)
cd C:/path/to/node-project
npm start
# 서버 실행: http://localhost:3000
```

**핵심 차이:**
- Python: `command` + `args` (프로세스 직접 실행)
- Node.js: `url` + `transport: "http"` (HTTP 통신)

---

## 🌐 GitHub MCP 서버 참고 자료

### 공식 저장소

1. **MCP 공식 GitHub**
   - https://github.com/modelcontextprotocol
   - MCP 프로토콜 사양 및 공식 SDK

2. **MCP TypeScript SDK**
   - https://github.com/modelcontextprotocol/typescript-sdk
   - 공식 TypeScript/JavaScript SDK
   - 예제 서버 포함

3. **MCP Python SDK**
   - https://github.com/modelcontextprotocol/python-sdk
   - 공식 Python SDK

### 커뮤니티 MCP 서버 예제

4. **Awesome MCP Servers**
   - https://github.com/punkpeye/awesome-mcp-servers
   - 다양한 MCP 서버 모음

5. **MCP Server Examples**
   - https://github.com/wong2/mcp-server-examples
   - 실전 예제 모음

6. **File System MCP Server**
   - https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
   - 파일 시스템 접근 MCP 서버

7. **GitHub MCP Server**
   - https://github.com/modelcontextprotocol/servers/tree/main/src/github
   - GitHub API 연동 서버

8. **Brave Search MCP Server**
   - https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search
   - 웹 검색 MCP 서버

9. **Google Drive MCP Server**
   - https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive
   - Google Drive 연동

10. **Postgres MCP Server**
    - https://github.com/modelcontextprotocol/servers/tree/main/src/postgres
    - PostgreSQL 데이터베이스 연동

### 유용한 도구

11. **MCP Inspector**
    - https://github.com/modelcontextprotocol/inspector
    - MCP 서버 테스트 및 디버깅 도구

12. **FastMCP (Python)**
    - https://github.com/jlowin/fastmcp
    - 간편한 Python MCP 서버 개발

---

## 🛠️ 개발 팁

### 1. TypeScript 사용 (권장)

```bash
npm install -D typescript @types/node
npx tsc --init
```

**tsconfig.json:**
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "Node16",
    "moduleResolution": "Node16",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true
  }
}
```

### 2. 디버깅

```javascript
// 서버에 로그 추가
console.error("Debug:", { name, args });

// Cursor Developer Tools에서 확인
// Help -> Toggle Developer Tools -> Console
```

### 3. 환경변수 사용

```bash
npm install dotenv
```

```javascript
import 'dotenv/config';

const API_KEY = process.env.API_KEY;
```

### 4. 에러 처리

```javascript
try {
  // 작업 수행
} catch (error) {
  return {
    content: [{
      type: "text",
      text: `오류: ${error.message}`
    }],
    isError: true
  };
}
```

---

## 📋 체크리스트

### Node.js 설치 확인
- [ ] Node.js 설치 완료 (`node --version`)
- [ ] NPM 설치 확인 (`npm --version`)
- [ ] MCP SDK 설치 (`npm install @modelcontextprotocol/sdk`)

### 서버 개발
- [ ] server.js 파일 생성
- [ ] package.json 설정
- [ ] Tools 정의
- [ ] 로컬 테스트 성공

### Cursor 연동
- [ ] Cursor MCP 설정 파일 작성
- [ ] 절대 경로 확인
- [ ] Cursor 재시작
- [ ] 채팅에서 Tool 사용 확인

---

## 🚀 빠른 시작

```bash
# 1. 프로젝트 생성
mkdir my-mcp-server && cd my-mcp-server

# 2. 초기화
npm init -y

# 3. SDK 설치
npm install @modelcontextprotocol/sdk

# 4. 서버 파일 생성 (위의 예제 코드 복사)
# server.js 파일 생성

# 5. package.json에 "type": "module" 추가

# 6. 서버 실행 테스트
node server.js

# 7. Cursor 설정 추가
# cline_mcp_settings.json에 서버 등록

# 8. Cursor 재시작 및 테스트
```

---

## 📞 문제 해결

### 1. "Cannot find module" 오류
```bash
# node_modules 재설치
rm -rf node_modules package-lock.json
npm install
```

### 2. "SyntaxError: Cannot use import" 오류
```json
// package.json에 추가
{
  "type": "module"
}
```

### 3. Cursor에서 서버 연결 안됨
- Node.js 경로 확인: `where node` (Windows) 또는 `which node` (Mac/Linux)
- 절대 경로 사용
- Cursor 완전 재시작

### 4. Tool 실행 오류
- Developer Tools (F12)에서 Console 확인
- server.js에 console.error로 디버깅 로그 추가

---

## 💡 추가 학습 자료

- [Node.js 공식 문서](https://nodejs.org/docs/)
- [NPM 공식 문서](https://docs.npmjs.com/)
- [MCP 공식 사이트](https://modelcontextprotocol.io/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)

---

<div align="center">

**"Python과 Node.js, 두 가지 방법으로 MCP 서버를 만들어보세요!"**

*자신에게 맞는 언어로 AI 도구를 개발하세요!*

</div>

