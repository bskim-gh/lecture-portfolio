#!/usr/bin/env node

/**
 * 예제 MCP 서버 - HTTP 서버 방식
 * 
 * 실행 방법:
 * node server.js
 * 
 * 접속 주소:
 * http://localhost:3000
 */

import express from 'express';
import cors from 'cors';
import fs from 'fs/promises';

const app = express();
const PORT = 3000;

// 미들웨어 설정
app.use(cors());
app.use(express.json());

// 서버 정보
const SERVER_INFO = {
  name: "example-mcp-server",
  version: "1.0.0",
  description: "Node.js MCP HTTP Server",
  tools: [
    "greet",
    "calculate", 
    "get_current_time",
    "read_file",
    "write_file",
    "list_directory"
  ]
};

// ============================================
// 서버 정보 엔드포인트
// ============================================
app.get('/', (req, res) => {
  res.json({
    status: 'running',
    ...SERVER_INFO,
    port: PORT,
    message: 'MCP HTTP Server is running'
  });
});

// ============================================
// Tools 목록 조회
// ============================================
app.get('/tools', (req, res) => {
  res.json({
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
            greeting: {
              type: "string",
              description: "인사말 (선택사항)",
              default: "안녕하세요",
            },
          },
          required: ["name"],
        },
      },
      {
        name: "calculate",
        description: "두 숫자를 계산하는 도구",
        inputSchema: {
          type: "object",
          properties: {
            operation: {
              type: "string",
              description: "연산자 (+, -, *, /)",
              enum: ["+", "-", "*", "/"],
            },
            a: {
              type: "number",
              description: "첫 번째 숫자",
            },
            b: {
              type: "number",
              description: "두 번째 숫자",
            },
          },
          required: ["operation", "a", "b"],
        },
      },
      {
        name: "get_current_time",
        description: "현재 시간을 반환하는 도구",
        inputSchema: {
          type: "object",
          properties: {},
        },
      },
      {
        name: "read_file",
        description: "파일 내용을 읽는 도구",
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
        description: "파일에 내용을 쓰는 도구",
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
        description: "디렉토리 내용을 나열하는 도구",
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
      }
    ]
  });
});

// ============================================
// Tool 실행 엔드포인트
// ============================================
app.post('/execute', async (req, res) => {
  const { tool, arguments: args } = req.body;
  
  if (!tool) {
    return res.status(400).json({ error: 'Tool name is required' });
  }

  try {
    let result;
    
    switch (tool) {
      // 인사 도구
      case "greet": {
        const greeting = args.greeting || "안녕하세요";
        result = `${greeting}, ${args.name}님! 👋`;
        break;
      }

      // 계산기
      case "calculate": {
        let result;
        switch (args.operation) {
          case "+":
            result = args.a + args.b;
            break;
          case "-":
            result = args.a - args.b;
            break;
          case "*":
            result = args.a * args.b;
            break;
          case "/":
            if (args.b === 0) {
              throw new Error("0으로 나눌 수 없습니다");
            }
            result = args.a / args.b;
            break;
          default:
            throw new Error(`지원하지 않는 연산자: ${args.operation}`);
        }
        
        result = `${args.a} ${args.operation} ${args.b} = ${result}`;
        break;
      }

      // 현재 시간
      case "get_current_time": {
        const now = new Date();
        const timeString = now.toLocaleString("ko-KR", {
          year: "numeric",
          month: "2-digit",
          day: "2-digit",
          hour: "2-digit",
          minute: "2-digit",
          second: "2-digit",
          hour12: false,
        });

        return {
          content: [
            {
              type: "text",
              text: `현재 시간: ${timeString} ⏰`,
            },
          ],
        };
      }

      // 파일 읽기
      case "read_file": {
        try {
          const content = await fs.readFile(args.filepath, "utf-8");
          return {
            content: [
              {
                type: "text",
                text: `파일: ${args.filepath}\n\n${content}`,
              },
            ],
          };
        } catch (error) {
          throw new Error(`파일 읽기 실패: ${error.message}`);
        }
      }

      // 파일 쓰기
      case "write_file": {
        try {
          await fs.writeFile(args.filepath, args.content, "utf-8");
          return {
            content: [
              {
                type: "text",
                text: `✅ 파일 저장 완료: ${args.filepath}`,
              },
            ],
          };
        } catch (error) {
          throw new Error(`파일 쓰기 실패: ${error.message}`);
        }
      }

      // 디렉토리 나열
      case "list_directory": {
        try {
          const files = await fs.readdir(args.directory, {
            withFileTypes: true,
          });

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
        } catch (error) {
          throw new Error(`디렉토리 읽기 실패: ${error.message}`);
        }
      }

      default:
        throw new Error(`알 수 없는 도구: ${name}`);
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

// ============================================
// 서버 시작
// ============================================
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  
  // stderr로 로그 출력 (stdout은 MCP 프로토콜용)
  console.error("=".repeat(60));
  console.error("  Example MCP Server (Node.js)");
  console.error("=".repeat(60));
  console.error("Server: example-mcp-server v1.0.0");
  console.error("Status: Running on stdio");
  console.error("Tools: 6개 등록됨");
  console.error("=".repeat(60));
}

// 서버 실행
main().catch((error) => {
  console.error("Server error:", error);
  process.exit(1);
});

