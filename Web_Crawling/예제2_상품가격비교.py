"""
실전 예제 2: 상품 가격 비교 프로그램
- 여러 쇼핑몰의 상품 가격 수집
- 가격 비교 및 분석
- 최저가 추천
"""

import requests
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime

class ProductPriceComparison:
    """
    상품 가격 비교 클래스
    """
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        })
        self.products = []
    
    def clean_price(self, price_str):
        """
        가격 문자열 정제
        "10,000원" -> 10000
        """
        numbers = re.sub(r'[^\d]', '', price_str)
        return int(numbers) if numbers else 0
    
    def fetch_page(self, url):
        """
        페이지 가져오기
        """
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"❌ 에러: {e}")
            return None
    
    def crawl_site_a(self, product_name):
        """
        사이트 A 크롤링 (예제)
        """
        print(f"\n🛒 사이트 A 검색 중...")
        
        # 실제로는 검색 URL 사용
        url = f"https://sitea.com/search?q={product_name}"
        
        # 데모 데이터
        products = [
            {
                'site': 'SiteA',
                'name': f'{product_name} - 상품1',
                'price': 25000,
                'url': 'https://sitea.com/product/1',
                'shipping': 2500
            },
            {
                'site': 'SiteA',
                'name': f'{product_name} - 상품2',
                'price': 23000,
                'url': 'https://sitea.com/product/2',
                'shipping': 0
            }
        ]
        
        print(f"   ✅ {len(products)}개 상품 발견")
        return products
    
    def crawl_site_b(self, product_name):
        """
        사이트 B 크롤링 (예제)
        """
        print(f"\n🛒 사이트 B 검색 중...")
        
        # 데모 데이터
        products = [
            {
                'site': 'SiteB',
                'name': f'{product_name} - 특가',
                'price': 22000,
                'url': 'https://siteb.com/product/100',
                'shipping': 3000
            },
            {
                'site': 'SiteB',
                'name': f'{product_name} - 정품',
                'price': 26000,
                'url': 'https://siteb.com/product/200',
                'shipping': 0
            }
        ]
        
        print(f"   ✅ {len(products)}개 상품 발견")
        return products
    
    def crawl_site_c(self, product_name):
        """
        사이트 C 크롤링 (예제)
        """
        print(f"\n🛒 사이트 C 검색 중...")
        
        # 데모 데이터
        products = [
            {
                'site': 'SiteC',
                'name': f'{product_name} - 공식판매',
                'price': 24500,
                'url': 'https://sitec.com/p/500',
                'shipping': 2000
            }
        ]
        
        print(f"   ✅ {len(products)}개 상품 발견")
        return products
    
    def search_all_sites(self, product_name):
        """
        모든 사이트 검색
        """
        print("=" * 60)
        print(f"  상품 검색: {product_name}")
        print("=" * 60)
        
        # 각 사이트에서 검색
        self.products.extend(self.crawl_site_a(product_name))
        self.products.extend(self.crawl_site_b(product_name))
        self.products.extend(self.crawl_site_c(product_name))
        
        print(f"\n📊 총 {len(self.products)}개 상품 발견")
    
    def calculate_total_price(self, product):
        """
        총 가격 계산 (상품가격 + 배송비)
        """
        return product['price'] + product['shipping']
    
    def analyze_prices(self):
        """
        가격 분석
        """
        if not self.products:
            print("❌ 분석할 데이터가 없습니다.")
            return
        
        print("\n" + "=" * 60)
        print("  가격 분석")
        print("=" * 60)
        
        # 총 가격 추가
        for product in self.products:
            product['total_price'] = self.calculate_total_price(product)
        
        # 가격순 정렬
        sorted_products = sorted(self.products, key=lambda x: x['total_price'])
        
        # 최저가
        cheapest = sorted_products[0]
        print(f"\n🏆 최저가 상품:")
        print(f"   사이트: {cheapest['site']}")
        print(f"   상품명: {cheapest['name']}")
        print(f"   상품가: {cheapest['price']:,}원")
        print(f"   배송비: {cheapest['shipping']:,}원")
        print(f"   총 가격: {cheapest['total_price']:,}원")
        print(f"   링크: {cheapest['url']}")
        
        # 평균 가격
        avg_price = sum(p['total_price'] for p in self.products) / len(self.products)
        print(f"\n📊 평균 가격: {avg_price:,.0f}원")
        
        # 가격 범위
        max_price = max(p['total_price'] for p in self.products)
        min_price = min(p['total_price'] for p in self.products)
        print(f"   최저가: {min_price:,}원")
        print(f"   최고가: {max_price:,}원")
        print(f"   가격 차이: {max_price - min_price:,}원")
        
        return sorted_products
    
    def print_all_products(self):
        """
        모든 상품 출력
        """
        if not self.products:
            return
        
        print("\n" + "=" * 60)
        print("  전체 상품 목록")
        print("=" * 60)
        
        # 가격순 정렬
        sorted_products = sorted(self.products, 
                                key=lambda x: self.calculate_total_price(x))
        
        for i, product in enumerate(sorted_products, 1):
            total = self.calculate_total_price(product)
            print(f"\n{i}. [{product['site']}] {product['name']}")
            print(f"   상품가: {product['price']:,}원")
            print(f"   배송비: {product['shipping']:,}원")
            print(f"   총 가격: {total:,}원")
            print(f"   URL: {product['url']}")
    
    def save_to_json(self, filename):
        """
        JSON 파일로 저장
        """
        if not self.products:
            print("❌ 저장할 데이터가 없습니다.")
            return
        
        # 총 가격 추가
        for product in self.products:
            product['total_price'] = self.calculate_total_price(product)
        
        data = {
            'crawled_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'total_count': len(self.products),
            'products': sorted(self.products, key=lambda x: x['total_price'])
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ JSON 저장 완료: {filename}")
    
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
    print("  상품 가격 비교 프로그램")
    print("=" * 60)
    
    comparator = ProductPriceComparison()
    
    try:
        # 검색할 상품명
        product_name = "무선 이어폰"
        
        # 모든 사이트 검색
        comparator.search_all_sites(product_name)
        
        # 가격 분석
        comparator.analyze_prices()
        
        # 전체 상품 출력
        comparator.print_all_products()
        
        # JSON 저장
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'price_comparison_{timestamp}.json'
        comparator.save_to_json(filename)
        
    finally:
        comparator.close()
    
    print("\n" + "=" * 60)
    print("  프로그램 종료")
    print("=" * 60)


if __name__ == "__main__":
    main()


"""
실제 사용 예시:

1. 네이버 쇼핑:
   URL: https://search.shopping.naver.com/search/all?query=상품명
   선택자: 상품 리스트, 가격, 배송비 등

2. 쿠팡:
   URL: https://www.coupang.com/np/search?q=상품명
   선택자: 상품 정보

3. 11번가:
   URL: https://search.11st.co.kr/Search.tmall?kwd=상품명
   선택자: 가격 정보

주의사항:
- 각 사이트의 robots.txt 확인
- 이용약관 준수
- API가 제공되는 경우 API 사용 권장
- 과도한 요청 금지
- 개인 정보 수집 금지

커스터마이징:
1. 실제 쇼핑몰 사이트 추가
2. 상품 상세 정보 수집 (리뷰, 평점 등)
3. 가격 변동 추적 기능
4. 알림 기능 추가 (최저가 알림)
5. 데이터베이스 연동
"""

