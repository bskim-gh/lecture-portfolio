"""
Section 2: FastMCP 기본 사용법
- MCP 인스턴스 생성
- Tool(도구) 추가
- 타입 힌트와 검증
- 에러 처리
"""

from fastmcp import FastMCP
from typing import Optional

print("=" * 60)
print("  Section 2: FastMCP 기본 사용법")
print("=" * 60)

# ============================================
# 1. MCP 인스턴스 생성
# ============================================
"""
FastMCP 인스턴스 생성:

from fastmcp import FastMCP

# 기본 생성
mcp = FastMCP("서버이름")

# 설정과 함께 생성
mcp = FastMCP(
    name="My MCP Server",
    version="1.0.0",
    description="나만의 MCP 서버"
)

주요 매개변수:
- name: 서버 이름 (필수)
- version: 버전 정보
- description: 서버 설명
"""

# 예제: MCP 서버 생성
mcp = FastMCP(
    name="학습용 MCP 서버",
    version="1.0.0"
)

# ============================================
# 2. Tool(도구) 추가 - 기본
# ============================================
"""
Tool이란?
- AI가 실행할 수 있는 함수
- 데코레이터로 간단하게 등록
- 자동으로 타입 검증

기본 문법:
@mcp.tool()
def function_name(param: type) -> return_type:
    '''도구 설명 (독스트링)'''
    return result
"""

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """두 숫자를 더하는 도구"""
    return a + b

@mcp.tool()
def multiply_numbers(a: float, b: float) -> float:
    """두 숫자를 곱하는 도구"""
    return a * b

# ============================================
# 3. Tool - 문자열 처리
# ============================================

@mcp.tool()
def reverse_string(text: str) -> str:
    """문자열을 거꾸로 뒤집는 도구"""
    return text[::-1]

@mcp.tool()
def count_words(text: str) -> int:
    """텍스트의 단어 개수를 세는 도구"""
    return len(text.split())

@mcp.tool()
def uppercase_text(text: str) -> str:
    """텍스트를 대문자로 변환하는 도구"""
    return text.upper()

# ============================================
# 4. Tool - 선택적 매개변수
# ============================================

@mcp.tool()
def greet(name: str, greeting: Optional[str] = "안녕하세요") -> str:
    """
    사용자에게 인사하는 도구
    
    Args:
        name: 사용자 이름
        greeting: 인사말 (기본값: "안녕하세요")
    
    Returns:
        인사 메시지
    """
    return f"{greeting}, {name}님!"

# ============================================
# 5. Tool - 복잡한 반환 타입
# ============================================

from typing import Dict, List

@mcp.tool()
def get_user_info(name: str, age: int) -> Dict[str, any]:
    """
    사용자 정보를 딕셔너리로 반환하는 도구
    """
    return {
        "name": name,
        "age": age,
        "is_adult": age >= 18,
        "category": "성인" if age >= 18 else "미성년자"
    }

@mcp.tool()
def split_text(text: str, delimiter: str = " ") -> List[str]:
    """
    텍스트를 구분자로 분리하는 도구
    """
    return text.split(delimiter)

# ============================================
# 6. Tool - 데이터 처리
# ============================================

@mcp.tool()
def calculate_average(numbers: List[float]) -> float:
    """
    숫자 리스트의 평균을 계산하는 도구
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

@mcp.tool()
def find_max(numbers: List[int]) -> int:
    """
    리스트에서 최댓값을 찾는 도구
    """
    if not numbers:
        raise ValueError("빈 리스트입니다")
    return max(numbers)

# ============================================
# 7. Tool - 에러 처리
# ============================================

@mcp.tool()
def safe_divide(a: float, b: float) -> float:
    """
    안전한 나눗셈 도구 (0으로 나누기 방지)
    """
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다")
    return a / b

@mcp.tool()
def validate_email(email: str) -> bool:
    """
    이메일 형식을 검증하는 도구
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# ============================================
# 8. Tool - 파일 작업
# ============================================

@mcp.tool()
def read_text_file(filepath: str) -> str:
    """
    텍스트 파일을 읽는 도구
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"파일을 찾을 수 없습니다: {filepath}"
    except Exception as e:
        return f"파일 읽기 오류: {str(e)}"

@mcp.tool()
def write_text_file(filepath: str, content: str) -> str:
    """
    텍스트 파일에 쓰는 도구
    """
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"파일 저장 완료: {filepath}"
    except Exception as e:
        return f"파일 쓰기 오류: {str(e)}"

# ============================================
# 9. Tool - JSON 처리
# ============================================

import json

@mcp.tool()
def parse_json(json_string: str) -> Dict:
    """
    JSON 문자열을 파싱하는 도구
    """
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON 파싱 오류: {str(e)}")

@mcp.tool()
def create_json(data: Dict) -> str:
    """
    딕셔너리를 JSON 문자열로 변환하는 도구
    """
    return json.dumps(data, ensure_ascii=False, indent=2)

# ============================================
# 10. 실전 예제 - 계산기
# ============================================

@mcp.tool()
def calculator(operation: str, a: float, b: float) -> float:
    """
    기본 계산기 도구
    
    Args:
        operation: 연산자 ('+', '-', '*', '/')
        a: 첫 번째 숫자
        b: 두 번째 숫자
    
    Returns:
        계산 결과
    """
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else None
    }
    
    if operation not in operations:
        raise ValueError(f"지원하지 않는 연산자: {operation}")
    
    result = operations[operation](a, b)
    if result is None:
        raise ValueError("0으로 나눌 수 없습니다")
    
    return result

# ============================================
# Main 실행
# ============================================
if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  등록된 Tool 목록")
    print("=" * 60)
    
    tools = [
        "add_numbers - 두 숫자 더하기",
        "multiply_numbers - 두 숫자 곱하기",
        "reverse_string - 문자열 뒤집기",
        "count_words - 단어 개수 세기",
        "greet - 인사하기",
        "get_user_info - 사용자 정보 반환",
        "calculate_average - 평균 계산",
        "safe_divide - 안전한 나눗셈",
        "validate_email - 이메일 검증",
        "read_text_file - 파일 읽기",
        "write_text_file - 파일 쓰기",
        "parse_json - JSON 파싱",
        "calculator - 계산기"
    ]
    
    for i, tool in enumerate(tools, 1):
        print(f"{i:2d}. {tool}")
    
    print("\n" + "=" * 60)
    print("  Tool 사용 예시")
    print("=" * 60)
    
    # 도구 테스트
    print("\n1. 숫자 더하기:")
    print(f"   add_numbers(10, 20) = {add_numbers(10, 20)}")
    
    print("\n2. 문자열 뒤집기:")
    print(f'   reverse_string("Hello") = {reverse_string("Hello")}')
    
    print("\n3. 인사하기:")
    print(f'   greet("김철수") = {greet("김철수")}')
    
    print("\n4. 평균 계산:")
    print(f"   calculate_average([10, 20, 30]) = {calculate_average([10, 20, 30])}")
    
    print("\n5. 계산기:")
    print(f"   calculator('+', 10, 5) = {calculator('+', 10, 5)}")
    print(f"   calculator('*', 10, 5) = {calculator('*', 10, 5)}")
    
    print("\n" + "=" * 60)
    print("  Section 2 완료!")
    print("=" * 60)
    
    print("\n📝 서버 실행 방법:")
    print("   1. 이 파일을 저장")
    print("   2. 터미널에서 실행:")
    print("      python 02_FastMCP_기본사용법.py")
    print("   또는")
    print("      fastmcp dev 02_FastMCP_기본사용법.py")

"""
학습 정리:

1. @mcp.tool() 데코레이터로 도구 등록
2. 타입 힌트로 자동 검증
3. 독스트링으로 도구 설명 추가
4. Optional 타입으로 선택적 매개변수
5. 에러 처리로 안전한 도구 작성
6. 다양한 타입 지원 (int, str, List, Dict 등)

다음 섹션에서는:
- Resources 추가하기
- Prompts 만들기
- 실제 서버 실행하기
- Cursor에 연동하기
"""

