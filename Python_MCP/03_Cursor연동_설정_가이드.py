"""
Section 3: MCP 서버 실행 및 Cursor 연동
- MCP 서버 로컬 실행
- Cursor에 MCP 서버 등록
- 설정 파일 작성
- 테스트 및 디버깅
"""

from fastmcp import FastMCP

print("=" * 60)
print("  Section 3: MCP 서버 실행 및 Cursor 연동")
print("=" * 60)

# ============================================
# 1. MCP 서버 로컬 실행 방법
# ============================================
"""
MCP 서버 실행 방법:

방법 1: Python으로 직접 실행
---------------------------------
python your_mcp_server.py

장점: 간단함
단점: 재시작 필요, 로그 부족

방법 2: FastMCP CLI 개발 모드
---------------------------------
fastmcp dev your_mcp_server.py

장점:
- 코드 변경 시 자동 재시작
- 상세한 로그 출력
- 디버깅 용이

방법 3: FastMCP CLI 프로덕션 모드
---------------------------------
fastmcp run your_mcp_server.py

장점:
- 최적화된 성능
- 안정적인 실행

권장: 개발 시에는 'fastmcp dev' 사용
"""

# ============================================
# 2. 실행 가능한 MCP 서버 예제
# ============================================

# MCP 서버 생성
mcp = FastMCP(
    name="예제 MCP 서버",
    version="1.0.0"
)

@mcp.tool()
def get_current_time() -> str:
    """현재 시간을 반환하는 도구"""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@mcp.tool()
def calculate(expression: str) -> float:
    """
    수식을 계산하는 도구
    예: "10 + 20", "5 * 3"
    """
    try:
        # 안전한 계산을 위해 eval 대신 제한적 연산
        allowed_chars = set("0123456789+-*/(). ")
        if not all(c in allowed_chars for c in expression):
            return "허용되지 않은 문자가 포함되어 있습니다"
        
        result = eval(expression)
        return float(result)
    except Exception as e:
        return f"계산 오류: {str(e)}"

# ============================================
# 3. Cursor MCP 설정 파일 작성
# ============================================
"""
Cursor에서 MCP 서버를 사용하려면 설정 파일이 필요합니다.

설정 파일 위치:
Windows: %APPDATA%\\Cursor\\User\\globalStorage\\rooveterinaryinc.roo-cline\\settings\\cline_mcp_settings.json
Mac/Linux: ~/.config/Cursor/User/globalStorage/rooveterinaryinc.roo-cline/settings/cline_mcp_settings.json

또는 Cursor 설정에서:
Ctrl+Shift+P (Cmd+Shift+P on Mac) -> "MCP Settings" 검색

설정 파일 예시 (cline_mcp_settings.json):
{
  "mcpServers": {
    "my-mcp-server": {
      "command": "python",
      "args": [
        "C:/full/path/to/your_mcp_server.py"
      ],
      "disabled": false,
      "alwaysAllow": []
    }
  }
}

주의사항:
1. Python 경로는 절대 경로 사용 권장
2. Windows의 경우 \\ 또는 / 사용
3. 파일 경로도 절대 경로 사용
"""

# ============================================
# 4. Cursor MCP 설정 - 상세 예제
# ============================================
"""
예제 1: 기본 설정
-------------------
{
  "mcpServers": {
    "example-server": {
      "command": "python",
      "args": ["C:/Users/YourName/mcp_server.py"]
    }
  }
}

예제 2: 가상환경 사용
-------------------
{
  "mcpServers": {
    "example-server": {
      "command": "C:/Users/YourName/venv/Scripts/python.exe",
      "args": ["C:/Users/YourName/mcp_server.py"]
    }
  }
}

예제 3: 환경변수 포함
-------------------
{
  "mcpServers": {
    "example-server": {
      "command": "python",
      "args": ["C:/Users/YourName/mcp_server.py"],
      "env": {
        "API_KEY": "your-api-key",
        "DEBUG": "true"
      }
    }
  }
}

예제 4: 여러 서버 등록
-------------------
{
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["C:/mcp/calculator_server.py"]
    },
    "file-tools": {
      "command": "python",
      "args": ["C:/mcp/file_server.py"]
    },
    "web-scraper": {
      "command": "python",
      "args": ["C:/mcp/scraper_server.py"],
      "disabled": false
    }
  }
}
"""

# ============================================
# 5. Cursor에서 MCP 사용하기
# ============================================
"""
Cursor에서 MCP 서버 사용 단계:

1단계: MCP 설정 파일 작성
   - Ctrl+Shift+P -> "MCP Settings"
   - 또는 설정 파일 직접 수정

2단계: MCP 서버 등록
   - 서버 이름, command, args 설정
   - 저장

3단계: Cursor 재시작
   - Cursor 완전 종료 후 재시작
   - MCP 서버 자동 실행

4단계: 채팅에서 사용
   - Cursor 채팅 창 열기
   - AI에게 요청: "현재 시간 알려줘" (get_current_time tool 호출)
   - AI가 자동으로 MCP tool 사용

5단계: Tool 사용 확인
   - 채팅 창에서 "🔧 Using tool" 표시 확인
   - Tool 실행 결과 확인

사용 예시:
-----------
사용자: "10 + 20을 계산해줘"
AI: [calculate tool 호출] 결과: 30

사용자: "현재 시간은?"
AI: [get_current_time tool 호출] 2024-01-15 14:30:00
"""

# ============================================
# 6. MCP 서버 디버깅
# ============================================
"""
디버깅 팁:

1. 로그 확인
   - fastmcp dev로 실행하면 상세 로그 출력
   - print() 문으로 디버깅 정보 출력

2. 에러 처리
   - try-except로 예외 처리
   - 명확한 에러 메시지 반환

3. 테스트
   - 서버 실행 후 수동 테스트
   - 각 tool 개별 테스트

4. Cursor 로그 확인
   - Help -> Toggle Developer Tools
   - Console 탭에서 MCP 관련 로그 확인

5. 일반적인 문제 해결
   - 서버 실행 안됨: Python 경로 확인
   - Tool 호출 안됨: 설정 파일 문법 확인
   - 권한 문제: 파일 경로 확인
"""

# 디버깅을 위한 로그 함수
def log_debug(message: str):
    """디버깅 로그 출력"""
    from datetime import datetime
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[DEBUG {timestamp}] {message}")

@mcp.tool()
def test_tool(message: str) -> str:
    """테스트용 도구 (로그 포함)"""
    log_debug(f"test_tool 호출됨: {message}")
    return f"수신한 메시지: {message}"

# ============================================
# 7. 설정 파일 생성 헬퍼
# ============================================

import json
import os

def create_cursor_config(
    server_name: str,
    script_path: str,
    python_path: str = "python"
) -> dict:
    """
    Cursor MCP 설정 생성 헬퍼 함수
    
    Args:
        server_name: MCP 서버 이름
        script_path: Python 스크립트 절대 경로
        python_path: Python 실행 파일 경로
    
    Returns:
        설정 딕셔너리
    """
    config = {
        "mcpServers": {
            server_name: {
                "command": python_path,
                "args": [script_path],
                "disabled": False,
                "alwaysAllow": []
            }
        }
    }
    return config

def print_config_example():
    """설정 파일 예시 출력"""
    print("\n" + "=" * 60)
    print("  Cursor MCP 설정 예시")
    print("=" * 60)
    
    # 현재 스크립트 경로
    current_path = os.path.abspath(__file__)
    
    config = create_cursor_config(
        server_name="example-server",
        script_path=current_path,
        python_path="python"
    )
    
    print("\n설정 파일 내용:")
    print(json.dumps(config, indent=2, ensure_ascii=False))
    
    print("\n\n설정 파일 위치:")
    print("Windows:")
    print("  %APPDATA%\\Cursor\\User\\globalStorage\\")
    print("  rooveterinaryinc.roo-cline\\settings\\cline_mcp_settings.json")
    print("\nMac/Linux:")
    print("  ~/.config/Cursor/User/globalStorage/")
    print("  rooveterinaryinc.roo-cline/settings/cline_mcp_settings.json")

# ============================================
# 8. 실행 가이드
# ============================================

def print_execution_guide():
    """실행 가이드 출력"""
    print("\n" + "=" * 60)
    print("  MCP 서버 실행 가이드")
    print("=" * 60)
    
    guide = """
    📝 실행 단계:
    
    1️⃣  서버 파일 준비
       - 이 파일을 원하는 위치에 저장
       - 절대 경로 확인
    
    2️⃣  로컬에서 테스트
       - 터미널 열기
       - 실행: fastmcp dev 03_MCP서버실행_Cursor연동.py
       - 또는: python 03_MCP서버실행_Cursor연동.py
    
    3️⃣  Cursor 설정
       - Cursor 열기
       - Ctrl+Shift+P (Mac: Cmd+Shift+P)
       - "MCP Settings" 검색 및 선택
       - 설정 파일 작성 (위의 예시 참고)
    
    4️⃣  Cursor 재시작
       - Cursor 완전 종료
       - 다시 실행
    
    5️⃣  테스트
       - Cursor 채팅 창 열기
       - "현재 시간 알려줘" 입력
       - AI가 get_current_time tool 사용하는지 확인
    
    ✅ 성공 확인:
       - 채팅에서 "🔧 Using tool: get_current_time" 표시
       - 실제 시간 반환
    
    ❌ 문제 발생 시:
       - Developer Tools 열기 (Help -> Toggle Developer Tools)
       - Console에서 에러 메시지 확인
       - Python 경로, 파일 경로 재확인
    """
    
    print(guide)

# ============================================
# Main 실행
# ============================================
if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  MCP 서버 정보")
    print("=" * 60)
    
    print("\n서버 이름:", mcp.name)
    print("버전:", mcp.version)
    
    print("\n등록된 Tools:")
    tools = ["get_current_time", "calculate", "test_tool"]
    for i, tool in enumerate(tools, 1):
        print(f"  {i}. {tool}")
    
    # 설정 예시 출력
    print_config_example()
    
    # 실행 가이드 출력
    print_execution_guide()
    
    print("\n" + "=" * 60)
    print("  Section 3 완료!")
    print("=" * 60)
    
    print("\n🚀 다음 단계:")
    print("   1. 이 서버를 로컬에서 실행해보기")
    print("   2. Cursor 설정 파일 작성하기")
    print("   3. Cursor에서 테스트하기")

"""
학습 정리:

1. MCP 서버 실행: fastmcp dev script.py
2. Cursor 설정: cline_mcp_settings.json 파일 작성
3. 절대 경로 사용 필수
4. Cursor 재시작 필요
5. 채팅에서 tool 사용 확인

실습 체크리스트:
□ MCP 서버 로컬 실행 성공
□ Cursor 설정 파일 작성 완료
□ Cursor 재시작 완료
□ 채팅에서 tool 사용 확인
□ 에러 없이 정상 동작 확인

다음 섹션에서는:
- 실전 예제 (파일 관리, API 호출 등)
- Resources와 Prompts 활용
- 고급 기능
"""

