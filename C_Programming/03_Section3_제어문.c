/*
 * Section 3: 제어문
 * - if 문
 * - switch 문
 * - for 문
 * - while 문
 * - do-while 문
 * - break와 continue
 * - 중첩 반복문
 */

#include <stdio.h>

// ============================================
// 1. if 문
// ============================================
void if_statement() {
    printf("\n=== if 문 ===\n");
    
    int score = 85;
    
    // 단순 if
    if (score >= 90) {
        printf("A 학점입니다.\n");
    }
    
    // if-else
    if (score >= 60) {
        printf("합격입니다!\n");
    } else {
        printf("불합격입니다.\n");
    }
    
    // if-else if-else
    if (score >= 90) {
        printf("학점: A\n");
    } else if (score >= 80) {
        printf("학점: B\n");
    } else if (score >= 70) {
        printf("학점: C\n");
    } else if (score >= 60) {
        printf("학점: D\n");
    } else {
        printf("학점: F\n");
    }
    
    // 중첩 if
    int age = 25;
    int hasLicense = 1;
    
    if (age >= 18) {
        if (hasLicense) {
            printf("운전 가능합니다.\n");
        } else {
            printf("면허증이 필요합니다.\n");
        }
    } else {
        printf("나이가 부족합니다.\n");
    }
}

// ============================================
// 2. switch 문
// ============================================
void switch_statement() {
    printf("\n=== switch 문 ===\n");
    
    int day = 3;
    
    printf("요일 번호 %d: ", day);
    switch(day) {
        case 1:
            printf("월요일\n");
            break;
        case 2:
            printf("화요일\n");
            break;
        case 3:
            printf("수요일\n");
            break;
        case 4:
            printf("목요일\n");
            break;
        case 5:
            printf("금요일\n");
            break;
        case 6:
            printf("토요일\n");
            break;
        case 7:
            printf("일요일\n");
            break;
        default:
            printf("잘못된 요일 번호\n");
    }
    
    // break가 없는 경우 (fall-through)
    char grade = 'B';
    printf("\n학점 %c: ", grade);
    
    switch(grade) {
        case 'A':
        case 'a':
            printf("최우수\n");
            break;
        case 'B':
        case 'b':
            printf("우수\n");
            break;
        case 'C':
        case 'c':
            printf("보통\n");
            break;
        default:
            printf("노력 필요\n");
    }
}

// ============================================
// 3. for 문
// ============================================
void for_loop() {
    printf("\n=== for 문 ===\n");
    
    // 기본 for 문
    printf("1부터 5까지: ");
    for (int i = 1; i <= 5; i++) {
        printf("%d ", i);
    }
    printf("\n");
    
    // 역순 출력
    printf("5부터 1까지: ");
    for (int i = 5; i >= 1; i--) {
        printf("%d ", i);
    }
    printf("\n");
    
    // 2씩 증가
    printf("짝수 (2부터 10까지): ");
    for (int i = 2; i <= 10; i += 2) {
        printf("%d ", i);
    }
    printf("\n");
    
    // 구구단 (3단)
    printf("\n3단:\n");
    for (int i = 1; i <= 9; i++) {
        printf("3 x %d = %d\n", i, 3 * i);
    }
}

// ============================================
// 4. while 문
// ============================================
void while_loop() {
    printf("\n=== while 문 ===\n");
    
    // 기본 while 문
    int count = 1;
    printf("1부터 5까지 출력:\n");
    while (count <= 5) {
        printf("%d ", count);
        count++;
    }
    printf("\n");
    
    // 합계 계산
    int sum = 0;
    int num = 1;
    while (num <= 10) {
        sum += num;
        num++;
    }
    printf("1부터 10까지의 합: %d\n", sum);
    
    // 무한 루프 예제 (주의: 실제 실행하지 않음)
    /*
    while (1) {
        printf("무한 루프\n");
        // break를 사용하여 탈출 가능
    }
    */
}

// ============================================
// 5. do-while 문
// ============================================
void do_while_loop() {
    printf("\n=== do-while 문 ===\n");
    
    // while과 do-while의 차이
    int i = 10;
    
    printf("while 문 (조건 먼저 확인):\n");
    while (i < 5) {
        printf("실행됨\n");  // 실행되지 않음
    }
    printf("실행 안됨\n");
    
    printf("\ndo-while 문 (최소 1번 실행):\n");
    do {
        printf("최소 1번 실행됨\n");  // 반드시 1번 실행
    } while (i < 5);
    
    // 메뉴 선택 예제
    printf("\n메뉴 선택 예제:\n");
    int choice;
    do {
        printf("\n--- 메뉴 ---\n");
        printf("1. 시작\n");
        printf("2. 설정\n");
        printf("3. 종료\n");
        printf("선택 (1-3): ");
        
        // 실제 입력 대신 시뮬레이션
        choice = 3;  // 종료 선택
        printf("%d\n", choice);
        
        switch(choice) {
            case 1:
                printf("게임 시작!\n");
                break;
            case 2:
                printf("설정 화면\n");
                break;
            case 3:
                printf("프로그램 종료\n");
                break;
            default:
                printf("잘못된 선택\n");
        }
    } while (choice != 3);
}

// ============================================
// 6. break와 continue
// ============================================
void break_continue() {
    printf("\n=== break와 continue ===\n");
    
    // break 예제
    printf("break 예제 (5에서 멈춤):\n");
    for (int i = 1; i <= 10; i++) {
        if (i == 5) {
            break;  // 반복문 종료
        }
        printf("%d ", i);
    }
    printf("\n");
    
    // continue 예제
    printf("\ncontinue 예제 (3의 배수 제외):\n");
    for (int i = 1; i <= 10; i++) {
        if (i % 3 == 0) {
            continue;  // 다음 반복으로
        }
        printf("%d ", i);
    }
    printf("\n");
    
    // 소수 찾기 (break 활용)
    printf("\n2부터 20까지의 소수:\n");
    for (int num = 2; num <= 20; num++) {
        int is_prime = 1;  // 소수라고 가정
        
        for (int i = 2; i < num; i++) {
            if (num % i == 0) {
                is_prime = 0;
                break;  // 약수를 찾았으므로 더 확인할 필요 없음
            }
        }
        
        if (is_prime) {
            printf("%d ", num);
        }
    }
    printf("\n");
}

// ============================================
// 7. 중첩 반복문
// ============================================
void nested_loops() {
    printf("\n=== 중첩 반복문 ===\n");
    
    // 구구단 전체
    printf("구구단:\n");
    for (int dan = 2; dan <= 9; dan++) {
        printf("\n[%d단]\n", dan);
        for (int num = 1; num <= 9; num++) {
            printf("%d x %d = %2d\n", dan, num, dan * num);
        }
    }
    
    // 별 찍기 패턴
    printf("\n\n별 패턴 1 (직각삼각형):\n");
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= i; j++) {
            printf("*");
        }
        printf("\n");
    }
    
    printf("\n별 패턴 2 (역삼각형):\n");
    for (int i = 5; i >= 1; i--) {
        for (int j = 1; j <= i; j++) {
            printf("*");
        }
        printf("\n");
    }
    
    printf("\n별 패턴 3 (정삼각형):\n");
    for (int i = 1; i <= 5; i++) {
        // 공백 출력
        for (int j = 1; j <= 5 - i; j++) {
            printf(" ");
        }
        // 별 출력
        for (int j = 1; j <= 2 * i - 1; j++) {
            printf("*");
        }
        printf("\n");
    }
}

// ============================================
// 8. goto 문 (권장하지 않음)
// ============================================
void goto_statement() {
    printf("\n=== goto 문 (사용 자제) ===\n");
    
    int count = 0;
    
    start:  // 레이블
    printf("count: %d\n", count);
    count++;
    
    if (count < 3) {
        goto start;  // start 레이블로 이동
    }
    
    printf("goto 문은 코드의 흐름을 복잡하게 만들어 권장하지 않습니다.\n");
}

// ============================================
// Main 함수
// ============================================
int main() {
    printf("====================================\n");
    printf("  C 언어 Section 3: 제어문\n");
    printf("====================================\n");
    
    if_statement();
    switch_statement();
    for_loop();
    while_loop();
    do_while_loop();
    break_continue();
    nested_loops();
    goto_statement();
    
    printf("\n====================================\n");
    printf("  Section 3 완료!\n");
    printf("====================================\n");
    
    return 0;
}

/*
 * 실습 문제:
 * 
 * 1. 1부터 100까지의 수 중에서 3의 배수의 합을 구하는 프로그램을 작성하세요.
 * 2. 사용자로부터 숫자를 입력받아 팩토리얼을 계산하는 프로그램을 작성하세요.
 *    (예: 5! = 5 × 4 × 3 × 2 × 1 = 120)
 * 3. 다이아몬드 모양의 별 패턴을 출력하는 프로그램을 작성하세요.
 * 4. 계산기 프로그램을 작성하세요. (+, -, *, / 연산을 선택하고
 *    두 숫자를 입력받아 결과를 출력. 0을 입력하면 종료)
 */

