"""
실전 예제 1: 뉴스 수집 프로그램
- 뉴스 사이트에서 기사 제목, 링크, 날짜 수집
- 여러 페이지 순회
- CSV 파일로 저장
"""

import requests
from bs4 import BeautifulSoup
import csv
import time
from datetime import datetime
from urllib.parse import urljoin

class NewsCrawler:
    """
    뉴스 크롤러 클래스
    """
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.articles = []
    
    def fetch_page(self, url):
        """
        페이지 가져오기
        """
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"❌ 페이지 로드 실패: {url}")
            print(f"   에러: {e}")
            return None
    
    def parse_article_list(self, html):
        """
        기사 목록 파싱 (예제)
        실제 사이트에 맞게 수정 필요
        """
        soup = BeautifulSoup(html, 'html.parser')
        
        # 예제 HTML 구조 (실제 사이트에 맞게 수정)
        articles = []
        
        # 가상의 기사 리스트 (실제로는 soup.find_all()로 찾기)
        # article_divs = soup.find_all('div', class_='article-item')
        
        # 데모용 데이터
        for i in range(5):
            article = {
                'title': f'뉴스 제목 {i+1}',
                'link': f'{self.base_url}/article/{i+1}',
                'date': datetime.now().strftime('%Y-%m-%d'),
                'summary': f'뉴스 요약 내용 {i+1}...'
            }
            articles.append(article)
        
        return articles
    
    def crawl_page(self, page_num):
        """
        특정 페이지 크롤링
        """
        url = f"{self.base_url}?page={page_num}"
        print(f"\n📰 페이지 {page_num} 크롤링 중...")
        print(f"   URL: {url}")
        
        html = self.fetch_page(url)
        if not html:
            return []
        
        articles = self.parse_article_list(html)
        print(f"   ✅ {len(articles)}개 기사 수집")
        
        return articles
    
    def crawl_multiple_pages(self, start_page, end_page):
        """
        여러 페이지 크롤링
        """
        print("=" * 60)
        print("  뉴스 크롤링 시작")
        print("=" * 60)
        
        for page in range(start_page, end_page + 1):
            articles = self.crawl_page(page)
            self.articles.extend(articles)
            
            # 서버 부하 방지
            if page < end_page:
                time.sleep(1)
        
        print(f"\n📊 총 {len(self.articles)}개 기사 수집 완료")
    
    def save_to_csv(self, filename):
        """
        CSV 파일로 저장
        """
        if not self.articles:
            print("❌ 저장할 데이터가 없습니다.")
            return
        
        with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
            fieldnames = ['title', 'link', 'date', 'summary']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(self.articles)
        
        print(f"✅ CSV 저장 완료: {filename}")
    
    def print_summary(self):
        """
        수집 결과 요약
        """
        print("\n" + "=" * 60)
        print("  수집 결과 요약")
        print("=" * 60)
        
        if not self.articles:
            print("수집된 기사가 없습니다.")
            return
        
        print(f"\n총 기사 수: {len(self.articles)}개")
        print("\n최근 5개 기사:")
        for i, article in enumerate(self.articles[:5], 1):
            print(f"\n{i}. {article['title']}")
            print(f"   날짜: {article['date']}")
            print(f"   링크: {article['link']}")
    
    def close(self):
        """
        세션 종료
        """
        self.session.close()


# ============================================
# 실행 예제
# ============================================
def main():
    """
    메인 실행 함수
    """
    print("\n" + "=" * 60)
    print("  뉴스 수집 프로그램")
    print("=" * 60)
    
    # 크롤러 생성
    base_url = "https://news.example.com"  # 실제 뉴스 사이트로 변경
    crawler = NewsCrawler(base_url)
    
    try:
        # 1~3페이지 크롤링
        crawler.crawl_multiple_pages(start_page=1, end_page=3)
        
        # 결과 요약 출력
        crawler.print_summary()
        
        # CSV 저장
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'news_{timestamp}.csv'
        crawler.save_to_csv(filename)
        
    finally:
        crawler.close()
    
    print("\n" + "=" * 60)
    print("  프로그램 종료")
    print("=" * 60)


if __name__ == "__main__":
    main()


"""
실제 사용 예시:

1. 네이버 뉴스 크롤링:
   - URL 패턴 분석
   - 기사 제목: div.news_tit 또는 a.news_tit
   - 날짜: span.info
   - robots.txt 확인 필수

2. 다음 뉴스 크롤링:
   - URL: https://news.daum.net/...
   - 기사 구조 분석
   - CSS 선택자 찾기

주의사항:
- 반드시 robots.txt 확인
- 저작권 준수
- 적절한 대기 시간 설정 (서버 부하 방지)
- User-Agent 설정
- 이용약관 확인

커스터마이징:
1. parse_article_list() 함수를 실제 사이트 구조에 맞게 수정
2. CSS 선택자 또는 XPath 사용
3. 추가 정보 수집 (작성자, 조회수 등)
4. 데이터 정제 로직 추가
"""

