"""
Section 2: BeautifulSoup 기초
- BeautifulSoup 소개 및 설치
- HTML 파싱 기초
- 태그 선택 및 탐색
- 데이터 추출
- CSS 선택자 사용
"""

import requests
from bs4 import BeautifulSoup
from pprint import pprint

print("=" * 50)
print("  Section 2: BeautifulSoup 기초")
print("=" * 50)

# ============================================
# 1. BeautifulSoup 소개
# ============================================
"""
BeautifulSoup이란?
- HTML과 XML을 파싱하는 Python 라이브러리
- 웹 페이지에서 원하는 데이터를 쉽게 추출
- 강력한 탐색 기능 제공

설치 방법:
pip install beautifulsoup4
pip install lxml  # 빠른 파서

주요 파서:
- html.parser: Python 기본 파서
- lxml: 빠르고 유연한 파서 (추천)
- html5lib: 느리지만 관대한 파서
"""

# ============================================
# 2. BeautifulSoup 기본 사용법
# ============================================
def beautifulsoup_basics():
    print("\n" + "=" * 50)
    print("BeautifulSoup 기본 사용법")
    print("=" * 50)
    
    # HTML 샘플
    html_doc = """
    <html>
        <head>
            <title>BeautifulSoup 예제</title>
        </head>
        <body>
            <h1>웹 크롤링 학습</h1>
            <p class="intro">BeautifulSoup으로 HTML을 파싱합니다.</p>
            <p class="content">데이터를 쉽게 추출할 수 있습니다.</p>
            <ul id="features">
                <li>간단한 사용법</li>
                <li>강력한 기능</li>
                <li>유연한 탐색</li>
            </ul>
        </body>
    </html>
    """
    
    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    print("\n[예제 1] BeautifulSoup 객체 생성")
    print(f"타입: {type(soup)}")
    
    # 전체 HTML 출력 (예쁘게)
    print("\n예쁘게 출력된 HTML:")
    print(soup.prettify())

# ============================================
# 3. 태그 선택하기
# ============================================
def select_tags():
    print("\n" + "=" * 50)
    print("태그 선택하기")
    print("=" * 50)
    
    html_doc = """
    <html>
        <body>
            <h1>제목</h1>
            <p>첫 번째 문단</p>
            <p>두 번째 문단</p>
            <div>
                <span>텍스트1</span>
                <span>텍스트2</span>
            </div>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    print("\n[예제 2] 태그 선택")
    
    # 첫 번째 태그 찾기
    print("\n1) 첫 번째 태그 찾기:")
    h1_tag = soup.find('h1')
    print(f"h1 태그: {h1_tag}")
    print(f"h1 텍스트: {h1_tag.text}")
    
    # 특정 태그 하나 찾기
    print("\n2) find() 메서드:")
    p_tag = soup.find('p')
    print(f"첫 번째 p 태그: {p_tag}")
    
    # 모든 태그 찾기
    print("\n3) find_all() 메서드:")
    all_p_tags = soup.find_all('p')
    print(f"모든 p 태그 개수: {len(all_p_tags)}")
    for i, tag in enumerate(all_p_tags, 1):
        print(f"  {i}. {tag.text}")
    
    # 여러 태그 동시에 찾기
    print("\n4) 여러 태그 찾기:")
    tags = soup.find_all(['h1', 'p'])
    for tag in tags:
        print(f"{tag.name}: {tag.text}")

# ============================================
# 4. 클래스와 ID로 선택하기
# ============================================
def select_by_class_id():
    print("\n" + "=" * 50)
    print("클래스와 ID로 선택하기")
    print("=" * 50)
    
    html_doc = """
    <html>
        <body>
            <div id="header">헤더</div>
            <p class="intro">소개 문단</p>
            <p class="content">내용 문단</p>
            <p class="content highlight">중요 내용</p>
            <div id="footer" class="bottom">푸터</div>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    print("\n[예제 3] 클래스와 ID로 선택")
    
    # ID로 선택
    print("\n1) ID로 선택:")
    header = soup.find(id="header")
    print(f"ID='header': {header.text}")
    
    footer = soup.find(id="footer")
    print(f"ID='footer': {footer.text}")
    
    # 클래스로 선택
    print("\n2) 클래스로 선택:")
    intro = soup.find(class_="intro")
    print(f"class='intro': {intro.text}")
    
    # 같은 클래스를 가진 모든 태그
    print("\n3) 같은 클래스 모두 찾기:")
    content_tags = soup.find_all(class_="content")
    for i, tag in enumerate(content_tags, 1):
        print(f"  {i}. {tag.text}")
    
    # 여러 클래스 중 하나라도 포함
    print("\n4) 특정 클래스 포함:")
    highlight = soup.find(class_="highlight")
    print(f"class='highlight' 포함: {highlight.text}")

# ============================================
# 5. 속성 값 가져오기
# ============================================
def get_attributes():
    print("\n" + "=" * 50)
    print("속성 값 가져오기")
    print("=" * 50)
    
    html_doc = """
    <html>
        <body>
            <a href="https://www.naver.com" id="naver" class="link">네이버</a>
            <img src="image1.jpg" alt="이미지1" width="100">
            <img src="image2.jpg" alt="이미지2" width="200">
            <div data-value="123" data-name="test">데이터</div>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    print("\n[예제 4] 태그 속성 가져오기")
    
    # 링크 URL 가져오기
    print("\n1) 링크 URL:")
    link = soup.find('a')
    print(f"href: {link.get('href')}")
    print(f"또는: {link['href']}")
    print(f"id: {link.get('id')}")
    print(f"class: {link.get('class')}")
    
    # 이미지 속성 가져오기
    print("\n2) 이미지 속성:")
    images = soup.find_all('img')
    for img in images:
        print(f"src: {img['src']}, alt: {img['alt']}, width: {img.get('width')}")
    
    # 모든 속성 가져오기
    print("\n3) 모든 속성:")
    div = soup.find('div')
    print(f"모든 속성: {div.attrs}")
    
    # 커스텀 데이터 속성
    print(f"data-value: {div.get('data-value')}")
    print(f"data-name: {div.get('data-name')}")

# ============================================
# 6. 텍스트 추출하기
# ============================================
def extract_text():
    print("\n" + "=" * 50)
    print("텍스트 추출하기")
    print("=" * 50)
    
    html_doc = """
    <html>
        <body>
            <div class="content">
                <h1>제목입니다</h1>
                <p>  공백이 많은   텍스트  </p>
                <div>
                    <span>내부1</span>
                    <span>내부2</span>
                </div>
            </div>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    print("\n[예제 5] 텍스트 추출 방법")
    
    # .text 사용
    print("\n1) .text 사용:")
    h1 = soup.find('h1')
    print(f"h1.text: '{h1.text}'")
    
    # .get_text() 사용
    print("\n2) .get_text() 사용:")
    p = soup.find('p')
    print(f"원본: '{p.text}'")
    print(f"strip=True: '{p.get_text(strip=True)}'")
    
    # 하위 요소 모두 포함
    print("\n3) 하위 요소 포함:")
    div = soup.find('div', class_='content')
    print(f"전체 텍스트:\n{div.get_text(strip=True)}")
    
    # 구분자 지정
    print("\n4) 구분자 지정:")
    inner_div = soup.find('div').find('div')
    print(f"구분자 ' | ': {inner_div.get_text(separator=' | ', strip=True)}")

# ============================================
# 7. CSS 선택자 사용하기
# ============================================
def use_css_selectors():
    print("\n" + "=" * 50)
    print("CSS 선택자 사용하기")
    print("=" * 50)
    
    html_doc = """
    <html>
        <body>
            <div id="container">
                <h1 class="title">메인 제목</h1>
                <div class="section">
                    <h2>섹션1</h2>
                    <p class="content">내용1</p>
                </div>
                <div class="section">
                    <h2>섹션2</h2>
                    <p class="content">내용2</p>
                </div>
                <ul id="menu">
                    <li class="item">메뉴1</li>
                    <li class="item active">메뉴2</li>
                    <li class="item">메뉴3</li>
                </ul>
            </div>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    print("\n[예제 6] CSS 선택자")
    
    # ID 선택자
    print("\n1) ID 선택자 (#):")
    container = soup.select_one('#container')
    print(f"#container: {container.name}")
    
    # 클래스 선택자
    print("\n2) 클래스 선택자 (.):")
    sections = soup.select('.section')
    print(f".section 개수: {len(sections)}")
    
    # 태그 선택자
    print("\n3) 태그 선택자:")
    h2_tags = soup.select('h2')
    for h2 in h2_tags:
        print(f"  h2: {h2.text}")
    
    # 자식 선택자
    print("\n4) 자식 선택자 (>):")
    direct_children = soup.select('#container > div')
    print(f"#container > div: {len(direct_children)}개")
    
    # 자손 선택자
    print("\n5) 자손 선택자 (공백):")
    descendants = soup.select('#container p')
    for p in descendants:
        print(f"  p: {p.text}")
    
    # 복합 선택자
    print("\n6) 복합 선택자:")
    active_item = soup.select_one('li.item.active')
    print(f"li.item.active: {active_item.text}")
    
    # 속성 선택자
    print("\n7) 속성 선택자:")
    items = soup.select('li[class="item"]')
    print(f'li[class="item"]: {len(items)}개')

# ============================================
# 8. 부모/형제 탐색
# ============================================
def navigate_tree():
    print("\n" + "=" * 50)
    print("부모/형제 탐색")
    print("=" * 50)
    
    html_doc = """
    <html>
        <body>
            <div id="parent">
                <h1>제목</h1>
                <p id="target">타겟</p>
                <span>형제</span>
            </div>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    print("\n[예제 7] 트리 탐색")
    
    target = soup.find(id="target")
    
    # 부모
    print("\n1) 부모 찾기:")
    print(f"부모 태그: {target.parent.name}")
    print(f"부모 ID: {target.parent.get('id')}")
    
    # 이전 형제
    print("\n2) 이전 형제:")
    prev = target.find_previous_sibling()
    print(f"이전 형제: {prev.name} - {prev.text}")
    
    # 다음 형제
    print("\n3) 다음 형제:")
    next_sib = target.find_next_sibling()
    print(f"다음 형제: {next_sib.name} - {next_sib.text}")
    
    # 모든 형제
    print("\n4) 모든 형제:")
    for sibling in target.parent.children:
        if sibling.name:  # 텍스트 노드 제외
            print(f"  {sibling.name}: {sibling.text}")

# ============================================
# 9. 실전 예제: 실제 웹 페이지 파싱
# ============================================
def parse_real_page():
    print("\n" + "=" * 50)
    print("실전 예제: 실제 웹 페이지 파싱")
    print("=" * 50)
    
    print("\n[예제 8] example.com 파싱")
    
    try:
        # 웹 페이지 가져오기
        url = "http://example.com"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
        
        response = requests.get(url, headers=headers, timeout=5)
        
        if response.status_code == 200:
            # HTML 파싱
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 제목 추출
            title = soup.find('title')
            print(f"\n페이지 제목: {title.text}")
            
            # h1 태그 추출
            h1 = soup.find('h1')
            if h1:
                print(f"H1: {h1.text}")
            
            # 모든 링크 추출
            print("\n모든 링크:")
            links = soup.find_all('a')
            for link in links:
                href = link.get('href')
                text = link.text.strip()
                if href:
                    print(f"  {text}: {href}")
            
            # 모든 문단 추출
            print("\n모든 문단:")
            paragraphs = soup.find_all('p')
            for i, p in enumerate(paragraphs, 1):
                print(f"  {i}. {p.text.strip()}")
        
    except Exception as e:
        print(f"오류 발생: {e}")

# ============================================
# 10. 정규표현식과 함께 사용
# ============================================
def use_with_regex():
    print("\n" + "=" * 50)
    print("정규표현식과 함께 사용")
    print("=" * 50)
    
    import re
    
    html_doc = """
    <html>
        <body>
            <div class="item-1">아이템1</div>
            <div class="item-2">아이템2</div>
            <div class="item-3">아이템3</div>
            <div class="other">기타</div>
            <a href="page1.html">페이지1</a>
            <a href="page2.html">페이지2</a>
            <a href="image.jpg">이미지</a>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    print("\n[예제 9] 정규표현식 활용")
    
    # 클래스명 패턴 매칭
    print("\n1) 클래스명 패턴:")
    items = soup.find_all(class_=re.compile("item-"))
    for item in items:
        print(f"  {item.get('class')}: {item.text}")
    
    # href 패턴 매칭
    print("\n2) href 패턴 (HTML 파일만):")
    html_links = soup.find_all('a', href=re.compile(r'\.html$'))
    for link in html_links:
        print(f"  {link.text}: {link['href']}")

# ============================================
# Main 실행
# ============================================
if __name__ == "__main__":
    beautifulsoup_basics()
    select_tags()
    select_by_class_id()
    get_attributes()
    extract_text()
    use_css_selectors()
    navigate_tree()
    parse_real_page()
    use_with_regex()
    
    print("\n" + "=" * 50)
    print("  Section 2 완료!")
    print("=" * 50)

"""
실습 문제:

1. http://example.com 페이지에서 모든 태그의 이름과 개수를 세는
   프로그램을 작성하세요.

2. HTML 문서를 만들고 다음을 수행하세요:
   - 특정 클래스를 가진 모든 요소 찾기
   - 각 요소의 텍스트와 속성 출력하기

3. CSS 선택자를 사용하여 다음을 선택하세요:
   - ID가 'main'인 div 안의 모든 p 태그
   - 클래스가 'active'인 li 태그
   - href 속성이 있는 모든 a 태그

4. 웹 페이지를 크롤링하여 다음을 추출하세요:
   - 모든 이미지의 src 속성
   - 모든 링크의 href와 텍스트
   - 특정 클래스의 모든 텍스트

5. 정규표현식을 사용하여 전화번호 패턴이나 이메일 주소를
   포함하는 태그를 찾는 프로그램을 작성하세요.
"""

