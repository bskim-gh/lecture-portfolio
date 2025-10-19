#!/usr/bin/env node

/**
 * MCP HTTP 서버 - Express 기반
 * 
 * 실행: node server_http.js
 * 접속: http://localhost:3000
 * 
 * Cursor 설정에서 URL로 연결
 */

import express from 'express';
import cors from 'cors';
import fs from 'fs/promises';

const app = express();
const PORT = process.env.PORT || 3000;

// 미들웨어
app.use(cors());
app.use(express.json());

// 서버 정보
const SERVER_INFO = {
  name: "mcp-http-server",
  version: "1.0.0",
  description: "MCP HTTP Server with Express",
  protocol: "http",
};

// ============================================
// 루트 - 서버 정보
// ============================================
app.get('/', (req, res) => {
  res.json({
    ...SERVER_INFO,
    status: 'running',
    port: PORT,
    endpoints: {
      info: 'GET /',
      tools: 'GET /tools',
      execute: 'POST /execute'
    }
  });
});

// ============================================
// Tools 목록
// ============================================
app.get('/tools', (req, res) => {
  res.json({
    tools: [
      {
        name: "greet",
        description: "사용자에게 인사하는 도구",
        parameters: {
          name: { type: "string", required: true },
          greeting: { type: "string", required: false, default: "안녕하세요" }
        }
      },
      {
        name: "calculate",
        description: "두 숫자를 계산하는 도구",
        parameters: {
          operation: { type: "string", required: true, enum: ["+", "-", "*", "/"] },
          a: { type: "number", required: true },
          b: { type: "number", required: true }
        }
      },
      {
        name: "get_current_time",
        description: "현재 시간을 반환하는 도구",
        parameters: {}
      },
      {
        name: "read_file",
        description: "파일 내용을 읽는 도구",
        parameters: {
          filepath: { type: "string", required: true }
        }
      },
      {
        name: "write_file",
        description: "파일에 내용을 쓰는 도구",
        parameters: {
          filepath: { type: "string", required: true },
          content: { type: "string", required: true }
        }
      },
      {
        name: "list_directory",
        description: "디렉토리 내용을 나열하는 도구",
        parameters: {
          directory: { type: "string", required: true }
        }
      }
    ]
  });
});

// ============================================
// Tool 실행
// ============================================
app.post('/execute', async (req, res) => {
  const { tool, arguments: args } = req.body;

  if (!tool) {
    return res.status(400).json({
      success: false,
      error: 'Tool name is required'
    });
  }

  try {
    let result;

    switch (tool) {
      case "greet": {
        const greeting = args.greeting || "안녕하세요";
        result = `${greeting}, ${args.name}님! 👋`;
        break;
      }

      case "calculate": {
        const { operation, a, b } = args;
        let calcResult;
        
        switch (operation) {
          case "+": calcResult = a + b; break;
          case "-": calcResult = a - b; break;
          case "*": calcResult = a * b; break;
          case "/": 
            if (b === 0) throw new Error("0으로 나눌 수 없습니다");
            calcResult = a / b;
            break;
          default:
            throw new Error(`지원하지 않는 연산자: ${operation}`);
        }
        
        result = `${a} ${operation} ${b} = ${calcResult}`;
        break;
      }

      case "get_current_time": {
        const now = new Date();
        result = now.toLocaleString("ko-KR", {
          year: "numeric",
          month: "2-digit",
          day: "2-digit",
          hour: "2-digit",
          minute: "2-digit",
          second: "2-digit",
          hour12: false,
        });
        break;
      }

      case "read_file": {
        try {
          const content = await fs.readFile(args.filepath, "utf-8");
          result = `파일: ${args.filepath}\n\n${content}`;
        } catch (error) {
          throw new Error(`파일 읽기 실패: ${error.message}`);
        }
        break;
      }

      case "write_file": {
        try {
          await fs.writeFile(args.filepath, args.content, "utf-8");
          result = `✅ 파일 저장 완료: ${args.filepath}`;
        } catch (error) {
          throw new Error(`파일 쓰기 실패: ${error.message}`);
        }
        break;
      }

      case "list_directory": {
        try {
          const files = await fs.readdir(args.directory, { withFileTypes: true });
          const fileList = files
            .map((file) => {
              const icon = file.isDirectory() ? "📁" : "📄";
              return `${icon} ${file.name}`;
            })
            .join("\n");
          
          result = `디렉토리: ${args.directory}\n\n${fileList}`;
        } catch (error) {
          throw new Error(`디렉토리 읽기 실패: ${error.message}`);
        }
        break;
      }

      default:
        return res.status(404).json({
          success: false,
          error: `알 수 없는 도구: ${tool}`
        });
    }

    res.json({
      success: true,
      tool,
      result
    });

  } catch (error) {
    res.status(500).json({
      success: false,
      tool,
      error: error.message
    });
  }
});

// ============================================
// 서버 시작
// ============================================
app.listen(PORT, () => {
  console.log("=".repeat(60));
  console.log("  MCP HTTP Server");
  console.log("=".repeat(60));
  console.log(`Server: ${SERVER_INFO.name} v${SERVER_INFO.version}`);
  console.log(`Status: Running`);
  console.log(`URL: http://localhost:${PORT}`);
  console.log(`Tools: 6개 등록됨`);
  console.log("=".repeat(60));
  console.log("\nCursor 설정에 다음 URL을 입력하세요:");
  console.log(`  http://localhost:${PORT}`);
  console.log("\n종료: Ctrl+C");
  console.log("=".repeat(60));
});

// 에러 처리
process.on('SIGINT', () => {
  console.log('\n\n서버를 종료합니다...');
  process.exit(0);
});

