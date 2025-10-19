"""
Section 3: BeautifulSoup 실습
- 실제 웹사이트 크롤링
- 뉴스 기사 수집
- 표(Table) 데이터 추출
- 페이지네이션 처리
- 데이터 정제 및 저장
"""

import requests
from bs4 import BeautifulSoup
import time
import csv
import json
from datetime import datetime

print("=" * 50)
print("  Section 3: BeautifulSoup 실습")
print("=" * 50)

# ============================================
# 1. 여러 페이지 크롤링
# ============================================
def crawl_multiple_pages():
    print("\n" + "=" * 50)
    print("여러 페이지 크롤링 (페이지네이션)")
    print("=" * 50)
    
    """
    페이지네이션(Pagination) 처리
    - 여러 페이지에 걸쳐 있는 데이터 수집
    - URL 패턴 파악이 중요
    - 예: page=1, page=2, page=3...
    """
    
    print("\n[예제 1] 페이지 번호로 순회하기")
    
    def crawl_page(page_num):
        """
        페이지별 크롤링 함수
        """
        # 실제 크롤링 시뮬레이션
        print(f"\n페이지 {page_num} 크롤링 중...")
        
        # URL 패턴 예시
        url = f"https://example.com/list?page={page_num}"
        print(f"URL: {url}")
        
        # 실제로는 여기서 requests.get() 사용
        # response = requests.get(url)
        # soup = BeautifulSoup(response.text, 'html.parser')
        
        # 데이터 추출 예시
        items = [f"아이템{page_num}-{i}" for i in range(1, 6)]
        return items
    
    # 1~3페이지 크롤링
    all_items = []
    for page in range(1, 4):
        items = crawl_page(page)
        all_items.extend(items)
        
        # 서버 부하 방지를 위한 대기
        time.sleep(1)
        print(f"✅ 페이지 {page} 완료: {len(items)}개 아이템")
    
    print(f"\n총 수집된 아이템: {len(all_items)}개")
    print(f"아이템 목록: {all_items[:10]}...")  # 처음 10개만

# ============================================
# 2. 표(Table) 데이터 추출
# ============================================
def extract_table_data():
    print("\n" + "=" * 50)
    print("표(Table) 데이터 추출")
    print("=" * 50)
    
    html_doc = """
    <html>
        <body>
            <table id="students">
                <thead>
                    <tr>
                        <th>이름</th>
                        <th>나이</th>
                        <th>점수</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>홍길동</td>
                        <td>20</td>
                        <td>85</td>
                    </tr>
                    <tr>
                        <td>김철수</td>
                        <td>22</td>
                        <td>90</td>
                    </tr>
                    <tr>
                        <td>이영희</td>
                        <td>21</td>
                        <td>88</td>
                    </tr>
                </tbody>
            </table>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    print("\n[예제 2] 테이블 데이터 추출")
    
    # 테이블 찾기
    table = soup.find('table', id='students')
    
    # 헤더 추출
    headers = []
    thead = table.find('thead')
    for th in thead.find_all('th'):
        headers.append(th.text.strip())
    
    print(f"\n헤더: {headers}")
    
    # 데이터 추출
    rows = []
    tbody = table.find('tbody')
    for tr in tbody.find_all('tr'):
        row = []
        for td in tr.find_all('td'):
            row.append(td.text.strip())
        rows.append(row)
    
    print("\n데이터:")
    for i, row in enumerate(rows, 1):
        print(f"{i}. {dict(zip(headers, row))}")
    
    return headers, rows

# ============================================
# 3. 리스트 아이템 수집
# ============================================
def collect_list_items():
    print("\n" + "=" * 50)
    print("리스트 아이템 수집")
    print("=" * 50)
    
    html_doc = """
    <html>
        <body>
            <div class="products">
                <div class="product">
                    <h3 class="name">상품 A</h3>
                    <p class="price">10,000원</p>
                    <span class="stock">재고: 50</span>
                </div>
                <div class="product">
                    <h3 class="name">상품 B</h3>
                    <p class="price">20,000원</p>
                    <span class="stock">재고: 30</span>
                </div>
                <div class="product">
                    <h3 class="name">상품 C</h3>
                    <p class="price">15,000원</p>
                    <span class="stock">재고: 0</span>
                </div>
            </div>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    print("\n[예제 3] 상품 리스트 추출")
    
    products = []
    product_divs = soup.find_all('div', class_='product')
    
    for div in product_divs:
        product = {
            'name': div.find('h3', class_='name').text,
            'price': div.find('p', class_='price').text,
            'stock': div.find('span', class_='stock').text
        }
        products.append(product)
    
    print(f"\n총 {len(products)}개 상품:")
    for i, product in enumerate(products, 1):
        print(f"{i}. {product['name']} - {product['price']} - {product['stock']}")
    
    return products

# ============================================
# 4. 데이터 정제하기
# ============================================
def clean_data():
    print("\n" + "=" * 50)
    print("데이터 정제하기")
    print("=" * 50)
    
    print("\n[예제 4] 텍스트 정제")
    
    # 가격 정제 (문자열 -> 숫자)
    def clean_price(price_str):
        """
        "10,000원" -> 10000
        """
        import re
        numbers = re.sub(r'[^\d]', '', price_str)
        return int(numbers) if numbers else 0
    
    # 재고 정제
    def clean_stock(stock_str):
        """
        "재고: 50" -> 50
        """
        import re
        match = re.search(r'\d+', stock_str)
        return int(match.group()) if match else 0
    
    # 예제 데이터
    raw_data = [
        {'name': '상품 A', 'price': '10,000원', 'stock': '재고: 50'},
        {'name': '상품 B', 'price': '20,000원', 'stock': '재고: 30'},
        {'name': '상품 C', 'price': '15,000원', 'stock': '재고: 0'},
    ]
    
    print("\n원본 데이터:")
    for item in raw_data:
        print(f"  {item}")
    
    # 데이터 정제
    cleaned_data = []
    for item in raw_data:
        cleaned = {
            'name': item['name'].strip(),
            'price': clean_price(item['price']),
            'stock': clean_stock(item['stock'])
        }
        cleaned_data.append(cleaned)
    
    print("\n정제된 데이터:")
    for item in cleaned_data:
        print(f"  {item}")
    
    return cleaned_data

# ============================================
# 5. CSV 파일로 저장
# ============================================
def save_to_csv():
    print("\n" + "=" * 50)
    print("CSV 파일로 저장")
    print("=" * 50)
    
    print("\n[예제 5] CSV 저장")
    
    # 샘플 데이터
    data = [
        {'name': '상품A', 'price': 10000, 'stock': 50},
        {'name': '상품B', 'price': 20000, 'stock': 30},
        {'name': '상품C', 'price': 15000, 'stock': 0},
    ]
    
    filename = 'products.csv'
    
    # CSV 파일 작성
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'price', 'stock'])
        writer.writeheader()
        writer.writerows(data)
    
    print(f"✅ CSV 파일 저장 완료: {filename}")
    print(f"저장된 데이터: {len(data)}개")
    
    # 저장된 파일 읽기
    print("\n저장된 내용 확인:")
    with open(filename, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"  {row}")

# ============================================
# 6. JSON 파일로 저장
# ============================================
def save_to_json():
    print("\n" + "=" * 50)
    print("JSON 파일로 저장")
    print("=" * 50)
    
    print("\n[예제 6] JSON 저장")
    
    # 샘플 데이터
    data = {
        'crawled_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'products': [
            {'name': '상품A', 'price': 10000, 'stock': 50},
            {'name': '상품B', 'price': 20000, 'stock': 30},
            {'name': '상품C', 'price': 15000, 'stock': 0},
        ]
    }
    
    filename = 'products.json'
    
    # JSON 파일 작성
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ JSON 파일 저장 완료: {filename}")
    print(f"저장된 상품 수: {len(data['products'])}개")
    
    # 저장된 파일 읽기
    print("\n저장된 내용 확인:")
    with open(filename, 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
        print(f"  크롤링 시간: {loaded_data['crawled_at']}")
        for product in loaded_data['products']:
            print(f"  - {product}")

# ============================================
# 7. 링크 추출 및 순회
# ============================================
def extract_and_follow_links():
    print("\n" + "=" * 50)
    print("링크 추출 및 순회")
    print("=" * 50)
    
    html_doc = """
    <html>
        <body>
            <div class="articles">
                <article>
                    <h2><a href="/article/1">기사 제목 1</a></h2>
                    <p>기사 내용 요약...</p>
                </article>
                <article>
                    <h2><a href="/article/2">기사 제목 2</a></h2>
                    <p>기사 내용 요약...</p>
                </article>
                <article>
                    <h2><a href="/article/3">기사 제목 3</a></h2>
                    <p>기사 내용 요약...</p>
                </article>
            </div>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    print("\n[예제 7] 기사 링크 추출")
    
    base_url = "https://example.com"
    articles = soup.find_all('article')
    
    links = []
    for article in articles:
        link_tag = article.find('a')
        if link_tag:
            title = link_tag.text.strip()
            href = link_tag.get('href')
            full_url = base_url + href
            
            links.append({
                'title': title,
                'url': full_url
            })
    
    print(f"\n추출된 링크 {len(links)}개:")
    for i, link in enumerate(links, 1):
        print(f"{i}. {link['title']}")
        print(f"   URL: {link['url']}")

# ============================================
# 8. 상대 URL을 절대 URL로 변환
# ============================================
def convert_url():
    print("\n" + "=" * 50)
    print("URL 변환")
    print("=" * 50)
    
    from urllib.parse import urljoin
    
    print("\n[예제 8] 상대 URL -> 절대 URL")
    
    base_url = "https://example.com/page/"
    
    relative_urls = [
        "article.html",
        "/about.html",
        "../contact.html",
        "https://other.com/page.html"
    ]
    
    print(f"\n기준 URL: {base_url}")
    print("\n변환 결과:")
    for rel_url in relative_urls:
        abs_url = urljoin(base_url, rel_url)
        print(f"{rel_url:30s} -> {abs_url}")

# ============================================
# 9. 에러 처리 및 재시도
# ============================================
def retry_crawling():
    print("\n" + "=" * 50)
    print("에러 처리 및 재시도")
    print("=" * 50)
    
    print("\n[예제 9] 재시도 로직")
    
    def crawl_with_retry(url, max_retries=3):
        """
        재시도 로직이 포함된 크롤링 함수
        """
        for attempt in range(max_retries):
            try:
                print(f"\n시도 {attempt + 1}/{max_retries}: {url}")
                
                # 실제 요청 (여기서는 시뮬레이션)
                # response = requests.get(url, timeout=5)
                # response.raise_for_status()
                
                # 성공 시뮬레이션
                if attempt >= 1:  # 2번째 시도에 성공
                    print("✅ 성공!")
                    return True
                else:
                    raise Exception("시뮬레이션 에러")
                
            except Exception as e:
                print(f"❌ 실패: {e}")
                if attempt < max_retries - 1:
                    wait_time = (attempt + 1) * 2
                    print(f"⏳ {wait_time}초 후 재시도...")
                    time.sleep(wait_time)
                else:
                    print("❌ 최대 재시도 횟수 초과")
                    return False
    
    # 테스트
    url = "https://example.com/data"
    crawl_with_retry(url)

# ============================================
# 10. 실전 종합 예제
# ============================================
def comprehensive_example():
    print("\n" + "=" * 50)
    print("실전 종합 예제")
    print("=" * 50)
    
    print("\n[예제 10] 웹 크롤러 클래스")
    
    class WebCrawler:
        def __init__(self, base_url):
            self.base_url = base_url
            self.session = requests.Session()
            self.session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
            })
        
        def fetch_page(self, url):
            """페이지 가져오기"""
            try:
                response = self.session.get(url, timeout=10)
                response.raise_for_status()
                return response.text
            except Exception as e:
                print(f"에러: {e}")
                return None
        
        def parse_html(self, html):
            """HTML 파싱"""
            return BeautifulSoup(html, 'html.parser')
        
        def extract_data(self, soup):
            """데이터 추출 (구현 필요)"""
            pass
        
        def save_data(self, data, filename):
            """데이터 저장"""
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"✅ 저장 완료: {filename}")
        
        def close(self):
            """세션 종료"""
            self.session.close()
    
    # 사용 예시
    print("\nWebCrawler 클래스 구조:")
    print("- fetch_page(): 페이지 가져오기")
    print("- parse_html(): HTML 파싱")
    print("- extract_data(): 데이터 추출")
    print("- save_data(): 데이터 저장")
    print("- close(): 세션 종료")

# ============================================
# Main 실행
# ============================================
if __name__ == "__main__":
    crawl_multiple_pages()
    extract_table_data()
    collect_list_items()
    clean_data()
    save_to_csv()
    save_to_json()
    extract_and_follow_links()
    convert_url()
    retry_crawling()
    comprehensive_example()
    
    print("\n" + "=" * 50)
    print("  Section 3 완료!")
    print("=" * 50)

"""
실습 문제:

1. 다음 기능을 가진 웹 크롤러를 만드세요:
   - 5개 페이지 순회
   - 각 페이지에서 제목과 링크 추출
   - CSV 파일로 저장

2. 표 데이터를 추출하여 다음을 수행하세요:
   - 헤더와 모든 행 추출
   - 특정 열의 합계 계산
   - JSON 형식으로 저장

3. 상품 리스트 페이지에서 다음 정보를 추출하세요:
   - 상품명, 가격, 재고
   - 가격순으로 정렬
   - 재고가 있는 상품만 필터링

4. 재시도 로직을 포함한 크롤러를 만드세요:
   - 최대 3회 재시도
   - 지수 백오프(exponential backoff) 적용
   - 성공/실패 로그 기록

5. 여러 페이지의 링크를 추출하고 각 링크의 페이지를
   크롤링하는 프로그램을 작성하세요.
   (주의: 실제 사이트는 robots.txt 확인)
"""

