"""
실전 예제 1: 파일 관리 MCP 서버
- 파일 읽기/쓰기
- 디렉토리 탐색
- 파일 검색
- 파일 정보 조회
"""

from fastmcp import FastMCP
from typing import List, Dict
import os
import json
from datetime import datetime
from pathlib import Path

# MCP 서버 생성
mcp = FastMCP(
    name="파일 관리 MCP 서버",
    version="1.0.0"
)

# ============================================
# 1. 파일 읽기/쓰기
# ============================================

@mcp.tool()
def read_file(filepath: str) -> str:
    """
    파일 내용을 읽는 도구
    
    Args:
        filepath: 읽을 파일 경로
    
    Returns:
        파일 내용
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        return f"파일 내용:\n{content}"
    except FileNotFoundError:
        return f"❌ 파일을 찾을 수 없습니다: {filepath}"
    except Exception as e:
        return f"❌ 파일 읽기 오류: {str(e)}"

@mcp.tool()
def write_file(filepath: str, content: str) -> str:
    """
    파일에 내용을 쓰는 도구
    
    Args:
        filepath: 저장할 파일 경로
        content: 저장할 내용
    
    Returns:
        성공 메시지
    """
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"✅ 파일 저장 완료: {filepath}"
    except Exception as e:
        return f"❌ 파일 쓰기 오류: {str(e)}"

@mcp.tool()
def append_to_file(filepath: str, content: str) -> str:
    """
    파일에 내용을 추가하는 도구
    
    Args:
        filepath: 파일 경로
        content: 추가할 내용
    
    Returns:
        성공 메시지
    """
    try:
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(content)
        return f"✅ 내용 추가 완료: {filepath}"
    except Exception as e:
        return f"❌ 파일 추가 오류: {str(e)}"

# ============================================
# 2. 디렉토리 탐색
# ============================================

@mcp.tool()
def list_directory(directory: str) -> str:
    """
    디렉토리 내용을 나열하는 도구
    
    Args:
        directory: 탐색할 디렉토리 경로
    
    Returns:
        파일 및 디렉토리 목록
    """
    try:
        if not os.path.exists(directory):
            return f"❌ 디렉토리를 찾을 수 없습니다: {directory}"
        
        items = os.listdir(directory)
        files = []
        dirs = []
        
        for item in items:
            full_path = os.path.join(directory, item)
            if os.path.isfile(full_path):
                files.append(f"📄 {item}")
            else:
                dirs.append(f"📁 {item}")
        
        result = f"디렉토리: {directory}\n\n"
        if dirs:
            result += "폴더:\n" + "\n".join(dirs) + "\n\n"
        if files:
            result += "파일:\n" + "\n".join(files)
        
        return result if (dirs or files) else "빈 디렉토리입니다."
    
    except Exception as e:
        return f"❌ 디렉토리 탐색 오류: {str(e)}"

@mcp.tool()
def get_file_info(filepath: str) -> Dict:
    """
    파일 정보를 조회하는 도구
    
    Args:
        filepath: 파일 경로
    
    Returns:
        파일 정보 (크기, 수정 날짜 등)
    """
    try:
        if not os.path.exists(filepath):
            return {"error": f"파일을 찾을 수 없습니다: {filepath}"}
        
        stat = os.stat(filepath)
        
        info = {
            "파일명": os.path.basename(filepath),
            "경로": os.path.abspath(filepath),
            "크기": f"{stat.st_size} bytes",
            "생성일": datetime.fromtimestamp(stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
            "수정일": datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
            "타입": "파일" if os.path.isfile(filepath) else "디렉토리"
        }
        
        return info
    
    except Exception as e:
        return {"error": str(e)}

# ============================================
# 3. 파일 검색
# ============================================

@mcp.tool()
def search_files(directory: str, pattern: str) -> str:
    """
    디렉토리에서 파일을 검색하는 도구
    
    Args:
        directory: 검색할 디렉토리
        pattern: 검색 패턴 (예: "*.py", "test_*")
    
    Returns:
        검색 결과
    """
    try:
        from pathlib import Path
        
        if not os.path.exists(directory):
            return f"❌ 디렉토리를 찾을 수 없습니다: {directory}"
        
        path = Path(directory)
        matches = list(path.rglob(pattern))
        
        if not matches:
            return f"'{pattern}' 패턴과 일치하는 파일을 찾을 수 없습니다."
        
        result = f"검색 결과 ({len(matches)}개):\n\n"
        for match in matches[:50]:  # 최대 50개
            result += f"📄 {match}\n"
        
        if len(matches) > 50:
            result += f"\n... 외 {len(matches) - 50}개 더"
        
        return result
    
    except Exception as e:
        return f"❌ 검색 오류: {str(e)}"

@mcp.tool()
def find_text_in_files(directory: str, search_text: str, extension: str = ".txt") -> str:
    """
    파일 내용에서 텍스트를 검색하는 도구
    
    Args:
        directory: 검색할 디렉토리
        search_text: 검색할 텍스트
        extension: 파일 확장자 (기본값: .txt)
    
    Returns:
        검색 결과
    """
    try:
        from pathlib import Path
        
        if not os.path.exists(directory):
            return f"❌ 디렉토리를 찾을 수 없습니다: {directory}"
        
        path = Path(directory)
        matches = []
        
        for file_path in path.rglob(f"*{extension}"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if search_text in content:
                        matches.append(str(file_path))
            except:
                continue
        
        if not matches:
            return f"'{search_text}'를 포함하는 파일을 찾을 수 없습니다."
        
        result = f"'{search_text}' 검색 결과 ({len(matches)}개):\n\n"
        for match in matches[:20]:
            result += f"📄 {match}\n"
        
        return result
    
    except Exception as e:
        return f"❌ 검색 오류: {str(e)}"

# ============================================
# 4. 파일 작업
# ============================================

@mcp.tool()
def create_directory(directory: str) -> str:
    """
    디렉토리를 생성하는 도구
    
    Args:
        directory: 생성할 디렉토리 경로
    
    Returns:
        성공 메시지
    """
    try:
        os.makedirs(directory, exist_ok=True)
        return f"✅ 디렉토리 생성 완료: {directory}"
    except Exception as e:
        return f"❌ 디렉토리 생성 오류: {str(e)}"

@mcp.tool()
def delete_file(filepath: str) -> str:
    """
    파일을 삭제하는 도구
    
    Args:
        filepath: 삭제할 파일 경로
    
    Returns:
        성공 메시지
    """
    try:
        if not os.path.exists(filepath):
            return f"❌ 파일을 찾을 수 없습니다: {filepath}"
        
        os.remove(filepath)
        return f"✅ 파일 삭제 완료: {filepath}"
    except Exception as e:
        return f"❌ 파일 삭제 오류: {str(e)}"

@mcp.tool()
def copy_file(source: str, destination: str) -> str:
    """
    파일을 복사하는 도구
    
    Args:
        source: 원본 파일 경로
        destination: 대상 파일 경로
    
    Returns:
        성공 메시지
    """
    try:
        import shutil
        
        if not os.path.exists(source):
            return f"❌ 원본 파일을 찾을 수 없습니다: {source}"
        
        shutil.copy2(source, destination)
        return f"✅ 파일 복사 완료: {source} -> {destination}"
    except Exception as e:
        return f"❌ 파일 복사 오류: {str(e)}"

# ============================================
# Main 실행
# ============================================
if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  파일 관리 MCP 서버")
    print("=" * 60)
    
    print("\n등록된 Tools:")
    tools = [
        "read_file - 파일 읽기",
        "write_file - 파일 쓰기",
        "append_to_file - 파일에 내용 추가",
        "list_directory - 디렉토리 탐색",
        "get_file_info - 파일 정보 조회",
        "search_files - 파일 검색",
        "find_text_in_files - 텍스트 검색",
        "create_directory - 디렉토리 생성",
        "delete_file - 파일 삭제",
        "copy_file - 파일 복사"
    ]
    
    for i, tool in enumerate(tools, 1):
        print(f"  {i:2d}. {tool}")
    
    print("\n" + "=" * 60)
    print("  서버 실행 방법")
    print("=" * 60)
    
    print("\n1. 개발 모드:")
    print("   fastmcp dev 예제1_파일관리_MCP서버.py")
    
    print("\n2. 프로덕션 모드:")
    print("   fastmcp run 예제1_파일관리_MCP서버.py")
    
    print("\n3. Cursor 설정:")
    config = {
        "mcpServers": {
            "file-manager": {
                "command": "python",
                "args": [os.path.abspath(__file__)]
            }
        }
    }
    print(json.dumps(config, indent=2, ensure_ascii=False))
    
    print("\n" + "=" * 60)
    print("  사용 예시 (Cursor 채팅)")
    print("=" * 60)
    
    examples = """
    - "현재 디렉토리의 파일 목록을 보여줘"
    - "test.txt 파일을 읽어줘"
    - "memo.txt 파일에 '안녕하세요'를 저장해줘"
    - "모든 Python 파일을 찾아줘"
    - "README 파일의 정보를 알려줘"
    """
    
    print(examples)

"""
Cursor 설정 예시:

{
  "mcpServers": {
    "file-manager": {
      "command": "python",
      "args": [
        "C:/full/path/to/예제1_파일관리_MCP서버.py"
      ],
      "disabled": false
    }
  }
}

사용 방법:
1. 위 설정을 Cursor MCP Settings에 추가
2. Cursor 재시작
3. 채팅에서 파일 관련 작업 요청

주의사항:
- 파일 경로는 절대 경로 사용 권장
- 민감한 파일 접근 시 주의
- 삭제 작업은 되돌릴 수 없음
"""

