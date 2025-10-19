"""
실전 예제 3: 동적 웹 페이지 크롤링 (Selenium)
- JavaScript로 생성되는 콘텐츠 수집
- 무한 스크롤 처리
- 로그인 자동화
- 데이터 수집 및 저장
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import json
from datetime import datetime

class DynamicWebCrawler:
    """
    동적 웹 페이지 크롤러
    """
    def __init__(self, headless=False):
        self.options = Options()
        
        if headless:
            self.options.add_argument('--headless')
        
        # 기본 옵션
        self.options.add_argument('--window-size=1920,1080')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--disable-notifications')
        self.options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)')
        
        # 자동화 감지 우회
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        
        self.driver = None
        self.wait = None
        self.collected_data = []
    
    def start(self):
        """
        드라이버 시작
        """
        print("\n🚀 브라우저 시작 중...")
        
        try:
            self.driver = webdriver.Chrome(options=self.options)
            self.driver.implicitly_wait(10)
            self.wait = WebDriverWait(self.driver, 15)
            print("✅ 브라우저 시작 완료")
        except Exception as e:
            print(f"❌ 브라우저 시작 실패: {e}")
            print("\n💡 해결 방법:")
            print("   1. ChromeDriver 설치 확인")
            print("   2. pip install webdriver-manager")
            print("   3. Chrome 브라우저 최신 버전 확인")
            raise
    
    def stop(self):
        """
        드라이버 종료
        """
        if self.driver:
            self.driver.quit()
            print("✅ 브라우저 종료")
    
    def login(self, login_url, username, password):
        """
        로그인 자동화 (예제)
        """
        print(f"\n🔐 로그인 시도: {login_url}")
        
        try:
            self.driver.get(login_url)
            time.sleep(2)
            
            # 아이디 입력 (실제 선택자로 변경 필요)
            username_input = self.wait.until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_input.clear()
            username_input.send_keys(username)
            
            # 비밀번호 입력
            password_input = self.driver.find_element(By.ID, "password")
            password_input.clear()
            password_input.send_keys(password)
            
            # 로그인 버튼 클릭
            login_button = self.driver.find_element(By.ID, "login-button")
            login_button.click()
            
            # 로그인 완료 대기
            time.sleep(3)
            
            print("✅ 로그인 완료")
            return True
            
        except Exception as e:
            print(f"❌ 로그인 실패: {e}")
            return False
    
    def scroll_to_bottom(self, pause_time=2):
        """
        페이지 끝까지 스크롤
        """
        print("\n📜 페이지 스크롤 중...")
        
        last_height = self.driver.execute_script(
            "return document.body.scrollHeight"
        )
        scroll_count = 0
        
        while True:
            # 스크롤 다운
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            scroll_count += 1
            print(f"   스크롤 {scroll_count}회")
            
            # 로딩 대기
            time.sleep(pause_time)
            
            # 새 높이 계산
            new_height = self.driver.execute_script(
                "return document.body.scrollHeight"
            )
            
            # 더 이상 스크롤할 수 없으면 종료
            if new_height == last_height:
                print(f"✅ 스크롤 완료 (총 {scroll_count}회)")
                break
            
            last_height = new_height
    
    def scroll_slowly(self, scroll_pause=0.5):
        """
        천천히 스크롤 (자연스러운 동작)
        """
        print("\n📜 천천히 스크롤 중...")
        
        # 전체 높이 가져오기
        total_height = self.driver.execute_script(
            "return document.body.scrollHeight"
        )
        
        # 단계별로 스크롤
        viewport_height = self.driver.execute_script(
            "return window.innerHeight"
        )
        
        current_position = 0
        while current_position < total_height:
            # 한 화면씩 스크롤
            current_position += viewport_height
            self.driver.execute_script(
                f"window.scrollTo(0, {current_position});"
            )
            time.sleep(scroll_pause)
        
        print("✅ 스크롤 완료")
    
    def wait_and_click(self, by, value):
        """
        요소 대기 후 클릭
        """
        try:
            element = self.wait.until(
                EC.element_to_be_clickable((by, value))
            )
            element.click()
            return True
        except Exception as e:
            print(f"❌ 클릭 실패: {e}")
            return False
    
    def extract_items(self, selector, max_items=None):
        """
        아이템 추출
        """
        print(f"\n📦 아이템 추출 중... (선택자: {selector})")
        
        try:
            # 요소 로딩 대기
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
            
            # 모든 요소 찾기
            elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
            
            if max_items:
                elements = elements[:max_items]
            
            items = []
            for i, element in enumerate(elements, 1):
                try:
                    item = {
                        'index': i,
                        'text': element.text,
                        'html': element.get_attribute('innerHTML')
                    }
                    items.append(item)
                except:
                    continue
            
            print(f"✅ {len(items)}개 아이템 추출 완료")
            return items
            
        except Exception as e:
            print(f"❌ 추출 실패: {e}")
            return []
    
    def extract_social_media_posts(self):
        """
        소셜 미디어 게시물 수집 예제 (가상)
        """
        print("\n" + "=" * 60)
        print("  소셜 미디어 게시물 수집")
        print("=" * 60)
        
        # 예제 URL (실제 사용 시 변경)
        url = "https://example-social.com"
        
        print(f"\n🌐 페이지 접속: {url}")
        self.driver.get(url)
        time.sleep(3)
        
        # 무한 스크롤로 더 많은 게시물 로드
        self.scroll_to_bottom(pause_time=2)
        
        # 게시물 추출 (실제 선택자로 변경 필요)
        posts = []
        
        # 데모 데이터
        for i in range(10):
            post = {
                'id': i + 1,
                'author': f'사용자{i+1}',
                'content': f'게시물 내용 {i+1}...',
                'likes': (i + 1) * 10,
                'comments': (i + 1) * 5,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            posts.append(post)
        
        self.collected_data.extend(posts)
        print(f"\n✅ {len(posts)}개 게시물 수집 완료")
        
        return posts
    
    def take_screenshot(self, filename=None):
        """
        스크린샷 저장
        """
        if not filename:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f'screenshot_{timestamp}.png'
        
        self.driver.save_screenshot(filename)
        print(f"📸 스크린샷 저장: {filename}")
    
    def save_to_json(self, filename):
        """
        JSON 파일로 저장
        """
        if not self.collected_data:
            print("❌ 저장할 데이터가 없습니다.")
            return
        
        data = {
            'crawled_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'total_count': len(self.collected_data),
            'data': self.collected_data
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ JSON 저장 완료: {filename}")
    
    def print_summary(self):
        """
        수집 결과 요약
        """
        print("\n" + "=" * 60)
        print("  수집 결과 요약")
        print("=" * 60)
        
        if not self.collected_data:
            print("수집된 데이터가 없습니다.")
            return
        
        print(f"\n📊 총 데이터 수: {len(self.collected_data)}개")
        
        print("\n최근 5개 데이터:")
        for item in self.collected_data[:5]:
            print(f"\n  • {item}")


# ============================================
# 실행 예제
# ============================================
def main():
    """
    메인 실행 함수
    """
    print("\n" + "=" * 60)
    print("  동적 웹 페이지 크롤링 프로그램")
    print("=" * 60)
    
    # 크롤러 생성
    crawler = DynamicWebCrawler(headless=False)  # headless=True로 백그라운드 실행
    
    try:
        # 드라이버 시작
        crawler.start()
        
        # 예제 1: 소셜 미디어 게시물 수집
        crawler.extract_social_media_posts()
        
        # 결과 요약
        crawler.print_summary()
        
        # JSON 저장
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'dynamic_crawling_{timestamp}.json'
        crawler.save_to_json(filename)
        
        # 스크린샷
        crawler.take_screenshot()
        
    except Exception as e:
        print(f"\n❌ 에러 발생: {e}")
        
    finally:
        # 브라우저 종료
        crawler.stop()
    
    print("\n" + "=" * 60)
    print("  프로그램 종료")
    print("=" * 60)


if __name__ == "__main__":
    main()


"""
실제 사용 예시:

1. 인스타그램 해시태그 수집:
   - 로그인 필요
   - 무한 스크롤 처리
   - 게시물 정보 수집
   
2. YouTube 동영상 정보:
   - 검색 결과 수집
   - 스크롤로 더 많은 결과 로드
   - 제목, 조회수, 업로드 날짜 등

3. LinkedIn 채용 공고:
   - 로그인 후 접근
   - 필터 설정
   - 공고 정보 수집

주의사항:
- 각 사이트의 이용약관 확인 필수
- 로그인 정보 보안 (환경변수 사용)
- robots.txt 확인
- 과도한 요청 금지
- API 제공 여부 확인 (API 사용 권장)

보안:
- 비밀번호 하드코딩 금지
- 환경변수나 설정 파일 사용
- .gitignore에 설정 파일 추가

커스터마이징:
1. 실제 웹사이트에 맞게 선택자 수정
2. 로그인 로직 구현
3. 데이터 정제 로직 추가
4. 에러 처리 강화
5. 재시도 로직 추가
6. 프록시 사용 (필요 시)
"""

