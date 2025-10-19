/*
 * Section 2: 연산자
 * - 산술 연산자
 * - 대입 연산자
 * - 비교 연산자
 * - 논리 연산자
 * - 증감 연산자
 * - 비트 연산자
 */

#include <stdio.h>

// ============================================
// 1. 산술 연산자
// ============================================
void arithmetic_operators() {
    int a = 10, b = 3;
    
    printf("\n=== 산술 연산자 ===\n");
    printf("a = %d, b = %d\n", a, b);
    printf("덧셈 (a + b): %d\n", a + b);
    printf("뺄셈 (a - b): %d\n", a - b);
    printf("곱셈 (a * b): %d\n", a * b);
    printf("나눗셈 (a / b): %d\n", a / b);  // 정수 나눗셈
    printf("나머지 (a %% b): %d\n", a % b);
    
    // 실수 나눗셈
    float result = (float)a / b;
    printf("실수 나눗셈 (a / b): %.2f\n", result);
}

// ============================================
// 2. 대입 연산자
// ============================================
void assignment_operators() {
    int x = 10;
    
    printf("\n=== 대입 연산자 ===\n");
    printf("초기값 x = %d\n", x);
    
    x += 5;  // x = x + 5
    printf("x += 5 -> x = %d\n", x);
    
    x -= 3;  // x = x - 3
    printf("x -= 3 -> x = %d\n", x);
    
    x *= 2;  // x = x * 2
    printf("x *= 2 -> x = %d\n", x);
    
    x /= 4;  // x = x / 4
    printf("x /= 4 -> x = %d\n", x);
    
    x %= 3;  // x = x % 3
    printf("x %%= 3 -> x = %d\n", x);
}

// ============================================
// 3. 비교 연산자
// ============================================
void comparison_operators() {
    int a = 10, b = 20;
    
    printf("\n=== 비교 연산자 ===\n");
    printf("a = %d, b = %d\n", a, b);
    printf("a == b: %d\n", a == b);  // 같은지
    printf("a != b: %d\n", a != b);  // 다른지
    printf("a > b: %d\n", a > b);    // 크기
    printf("a < b: %d\n", a < b);    // 작기
    printf("a >= b: %d\n", a >= b);  // 크거나 같기
    printf("a <= b: %d\n", a <= b);  // 작거나 같기
    
    // 0은 거짓(false), 1은 참(true)
}

// ============================================
// 4. 논리 연산자
// ============================================
void logical_operators() {
    int x = 5, y = 10, z = 15;
    
    printf("\n=== 논리 연산자 ===\n");
    printf("x = %d, y = %d, z = %d\n", x, y, z);
    
    // AND 연산 (&&)
    printf("(x < y) && (y < z): %d\n", (x < y) && (y < z));
    printf("(x > y) && (y < z): %d\n", (x > y) && (y < z));
    
    // OR 연산 (||)
    printf("(x > y) || (y < z): %d\n", (x > y) || (y < z));
    printf("(x > y) || (y > z): %d\n", (x > y) || (y > z));
    
    // NOT 연산 (!)
    printf("!(x < y): %d\n", !(x < y));
    printf("!(x > y): %d\n", !(x > y));
}

// ============================================
// 5. 증감 연산자
// ============================================
void increment_decrement() {
    int a = 5, b = 5;
    
    printf("\n=== 증감 연산자 ===\n");
    printf("초기값: a = %d, b = %d\n", a, b);
    
    // 전위 증감 (++a, --a)
    printf("\n전위 증감:\n");
    printf("++a = %d (a는 이제 %d)\n", ++a, a);
    printf("--b = %d (b는 이제 %d)\n", --b, b);
    
    // 후위 증감 (a++, a--)
    a = 5; b = 5;
    printf("\n후위 증감:\n");
    printf("a++ = %d (a는 이제 %d)\n", a++, a);
    printf("b-- = %d (b는 이제 %d)\n", b--, b);
    
    // 차이점 예제
    int x = 10, y = 10;
    printf("\n전위 vs 후위:\n");
    printf("y = ++x: x=%d, y=%d\n", x, ++x);  // x를 먼저 증가
    
    x = 10;
    printf("y = x++: x=%d, y=%d\n", x++, x);  // x를 나중에 증가
}

// ============================================
// 6. 비트 연산자
// ============================================
void bitwise_operators() {
    unsigned int a = 60;  // 0011 1100
    unsigned int b = 13;  // 0000 1101
    
    printf("\n=== 비트 연산자 ===\n");
    printf("a = %u (이진수: 0011 1100)\n", a);
    printf("b = %u (이진수: 0000 1101)\n", b);
    
    printf("\nAND (a & b): %u\n", a & b);   // 0000 1100 = 12
    printf("OR (a | b): %u\n", a | b);      // 0011 1101 = 61
    printf("XOR (a ^ b): %u\n", a ^ b);     // 0011 0001 = 49
    printf("NOT (~a): %u\n", ~a);           // 1100 0011
    printf("LEFT SHIFT (a << 2): %u\n", a << 2);   // 1111 0000 = 240
    printf("RIGHT SHIFT (a >> 2): %u\n", a >> 2);  // 0000 1111 = 15
}

// ============================================
// 7. 조건 연산자 (삼항 연산자)
// ============================================
void ternary_operator() {
    int a = 10, b = 20;
    
    printf("\n=== 조건 연산자 (삼항 연산자) ===\n");
    
    // 조건 ? 참일때값 : 거짓일때값
    int max = (a > b) ? a : b;
    printf("a = %d, b = %d\n", a, b);
    printf("최대값: %d\n", max);
    
    // 짝수/홀수 판별
    int num = 7;
    printf("\n%d는 %s입니다.\n", num, (num % 2 == 0) ? "짝수" : "홀수");
}

// ============================================
// 8. 연산자 우선순위
// ============================================
void operator_precedence() {
    printf("\n=== 연산자 우선순위 ===\n");
    
    int result;
    
    // 산술 연산자 우선순위
    result = 2 + 3 * 4;
    printf("2 + 3 * 4 = %d (곱셈이 먼저)\n", result);
    
    result = (2 + 3) * 4;
    printf("(2 + 3) * 4 = %d (괄호가 최우선)\n", result);
    
    // 비교와 논리 연산자
    result = 10 > 5 && 20 < 30;
    printf("10 > 5 && 20 < 30 = %d\n", result);
    
    /*
     * 연산자 우선순위 (높은 것부터):
     * 1. () [] -> .
     * 2. ++ -- ! ~ (단항)
     * 3. * / %
     * 4. + -
     * 5. << >>
     * 6. < <= > >=
     * 7. == !=
     * 8. &
     * 9. ^
     * 10. |
     * 11. &&
     * 12. ||
     * 13. ?:
     * 14. = += -= *= /= %= 등
     */
}

// ============================================
// Main 함수
// ============================================
int main() {
    printf("====================================\n");
    printf("  C 언어 Section 2: 연산자\n");
    printf("====================================\n");
    
    arithmetic_operators();
    assignment_operators();
    comparison_operators();
    logical_operators();
    increment_decrement();
    bitwise_operators();
    ternary_operator();
    operator_precedence();
    
    printf("\n====================================\n");
    printf("  Section 2 완료!\n");
    printf("====================================\n");
    
    return 0;
}

/*
 * 실습 문제:
 * 
 * 1. 두 정수를 입력받아 사칙연산 결과를 모두 출력하는 프로그램을 작성하세요.
 * 2. 점수를 입력받아 90점 이상이면 "A", 80점 이상이면 "B", 
 *    70점 이상이면 "C", 그 외는 "F"를 출력하세요 (삼항 연산자 사용).
 * 3. 년도를 입력받아 윤년인지 판별하는 프로그램을 작성하세요.
 *    (윤년 조건: 4의 배수이면서 100의 배수가 아니거나, 400의 배수)
 */

