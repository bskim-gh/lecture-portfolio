"""
실전 예제 2: 웹 검색 및 데이터 수집 MCP 서버
- 웹 페이지 가져오기
- HTML 파싱
- 간단한 데이터 추출
- API 호출
"""

from fastmcp import FastMCP
from typing import Dict, List
import json

# MCP 서버 생성
mcp = FastMCP(
    name="웹 검색 MCP 서버",
    version="1.0.0"
)

# ============================================
# 1. 웹 페이지 가져오기
# ============================================

@mcp.tool()
def fetch_url(url: str) -> str:
    """
    URL의 HTML 내용을 가져오는 도구
    
    Args:
        url: 가져올 웹 페이지 URL
    
    Returns:
        HTML 내용 (처음 1000자)
    """
    try:
        import requests
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # 처음 1000자만 반환
        content = response.text[:1000]
        return f"✅ 페이지 가져오기 성공\n\n내용 (처음 1000자):\n{content}..."
    
    except requests.RequestException as e:
        return f"❌ 페이지 가져오기 실패: {str(e)}"
    except Exception as e:
        return f"❌ 오류: {str(e)}"

@mcp.tool()
def get_page_title(url: str) -> str:
    """
    웹 페이지의 제목을 가져오는 도구
    
    Args:
        url: 웹 페이지 URL
    
    Returns:
        페이지 제목
    """
    try:
        import requests
        from bs4 import BeautifulSoup
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('title')
        
        if title:
            return f"📄 페이지 제목: {title.text.strip()}"
        else:
            return "제목을 찾을 수 없습니다."
    
    except Exception as e:
        return f"❌ 오류: {str(e)}"

# ============================================
# 2. 데이터 추출
# ============================================

@mcp.tool()
def extract_links(url: str) -> str:
    """
    웹 페이지에서 모든 링크를 추출하는 도구
    
    Args:
        url: 웹 페이지 URL
    
    Returns:
        링크 목록
    """
    try:
        import requests
        from bs4 import BeautifulSoup
        from urllib.parse import urljoin
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        
        result = f"🔗 발견된 링크 ({len(links)}개):\n\n"
        
        for i, link in enumerate(links[:20], 1):  # 최대 20개
            href = urljoin(url, link['href'])
            text = link.text.strip() or "(텍스트 없음)"
            result += f"{i}. {text}\n   {href}\n\n"
        
        if len(links) > 20:
            result += f"... 외 {len(links) - 20}개 더"
        
        return result
    
    except Exception as e:
        return f"❌ 오류: {str(e)}"

@mcp.tool()
def extract_images(url: str) -> str:
    """
    웹 페이지에서 이미지 URL을 추출하는 도구
    
    Args:
        url: 웹 페이지 URL
    
    Returns:
        이미지 URL 목록
    """
    try:
        import requests
        from bs4 import BeautifulSoup
        from urllib.parse import urljoin
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.find_all('img', src=True)
        
        result = f"🖼️ 발견된 이미지 ({len(images)}개):\n\n"
        
        for i, img in enumerate(images[:15], 1):  # 최대 15개
            src = urljoin(url, img['src'])
            alt = img.get('alt', '(설명 없음)')
            result += f"{i}. {alt}\n   {src}\n\n"
        
        if len(images) > 15:
            result += f"... 외 {len(images) - 15}개 더"
        
        return result
    
    except Exception as e:
        return f"❌ 오류: {str(e)}"

# ============================================
# 3. API 호출
# ============================================

@mcp.tool()
def get_json_data(url: str) -> Dict:
    """
    JSON API에서 데이터를 가져오는 도구
    
    Args:
        url: API URL
    
    Returns:
        JSON 데이터
    """
    try:
        import requests
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        return {"success": True, "data": data}
    
    except Exception as e:
        return {"success": False, "error": str(e)}

@mcp.tool()
def check_url_status(url: str) -> Dict:
    """
    URL의 상태를 확인하는 도구
    
    Args:
        url: 확인할 URL
    
    Returns:
        상태 정보
    """
    try:
        import requests
        
        response = requests.head(url, timeout=10, allow_redirects=True)
        
        info = {
            "url": url,
            "status_code": response.status_code,
            "status": "정상" if response.status_code == 200 else "문제 발생",
            "content_type": response.headers.get('Content-Type', 'Unknown'),
            "server": response.headers.get('Server', 'Unknown')
        }
        
        return info
    
    except Exception as e:
        return {"url": url, "error": str(e)}

# ============================================
# 4. 유용한 도구들
# ============================================

@mcp.tool()
def search_in_page(url: str, keyword: str) -> str:
    """
    웹 페이지에서 키워드를 검색하는 도구
    
    Args:
        url: 웹 페이지 URL
        keyword: 검색할 키워드
    
    Returns:
        검색 결과
    """
    try:
        import requests
        from bs4 import BeautifulSoup
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        
        count = text.lower().count(keyword.lower())
        
        if count > 0:
            # 키워드가 포함된 문장 찾기
            sentences = text.split('.')
            matches = [s.strip() for s in sentences if keyword.lower() in s.lower()]
            
            result = f"🔍 '{keyword}' 검색 결과: {count}회 발견\n\n"
            result += "관련 문장:\n"
            
            for i, match in enumerate(matches[:5], 1):
                result += f"{i}. {match[:100]}...\n\n"
            
            return result
        else:
            return f"'{keyword}'를 찾을 수 없습니다."
    
    except Exception as e:
        return f"❌ 오류: {str(e)}"

@mcp.tool()
def get_page_metadata(url: str) -> Dict:
    """
    웹 페이지의 메타데이터를 가져오는 도구
    
    Args:
        url: 웹 페이지 URL
    
    Returns:
        메타데이터 정보
    """
    try:
        import requests
        from bs4 import BeautifulSoup
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        metadata = {
            "url": url,
            "title": soup.find('title').text if soup.find('title') else "없음",
            "description": "",
            "keywords": "",
            "author": ""
        }
        
        # 메타 태그 추출
        for meta in soup.find_all('meta'):
            name = meta.get('name', '').lower()
            property_attr = meta.get('property', '').lower()
            content = meta.get('content', '')
            
            if name == 'description' or property_attr == 'og:description':
                metadata['description'] = content
            elif name == 'keywords':
                metadata['keywords'] = content
            elif name == 'author':
                metadata['author'] = content
        
        return metadata
    
    except Exception as e:
        return {"error": str(e)}

# ============================================
# Main 실행
# ============================================
if __name__ == "__main__":
    import os
    
    print("\n" + "=" * 60)
    print("  웹 검색 MCP 서버")
    print("=" * 60)
    
    print("\n등록된 Tools:")
    tools = [
        "fetch_url - URL 내용 가져오기",
        "get_page_title - 페이지 제목 가져오기",
        "extract_links - 링크 추출",
        "extract_images - 이미지 URL 추출",
        "get_json_data - JSON API 호출",
        "check_url_status - URL 상태 확인",
        "search_in_page - 페이지 내 키워드 검색",
        "get_page_metadata - 메타데이터 추출"
    ]
    
    for i, tool in enumerate(tools, 1):
        print(f"  {i}. {tool}")
    
    print("\n" + "=" * 60)
    print("  필수 라이브러리")
    print("=" * 60)
    
    print("\npip install requests beautifulsoup4")
    
    print("\n" + "=" * 60)
    print("  Cursor 설정")
    print("=" * 60)
    
    config = {
        "mcpServers": {
            "web-scraper": {
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
    - "example.com의 제목을 알려줘"
    - "이 페이지의 모든 링크를 추출해줘"
    - "페이지에서 'Python' 키워드를 검색해줘"
    - "URL 상태를 확인해줘"
    """
    
    print(examples)

"""
주의사항:
- robots.txt 확인 필수
- 웹사이트 이용약관 준수
- 과도한 요청 금지
- User-Agent 설정 권장

사용 예시:
사용자: "https://example.com의 제목을 알려줘"
AI: [get_page_title 호출] 제목: Example Domain
"""

