/*
 * 예제: 간단한 계산기 프로그램
 * 
 * 기능:
 * - 사칙연산 (+, -, *, /)
 * - 메뉴 기반 인터페이스
 * - 반복 실행
 */

#include <stdio.h>
#include <stdlib.h>

// 함수 프로토타입
void display_menu(void);
double add(double a, double b);
double subtract(double a, double b);
double multiply(double a, double b);
double divide(double a, double b);

int main() {
    int choice;
    double num1, num2, result;
    
    printf("====================================\n");
    printf("     간단한 계산기 프로그램\n");
    printf("====================================\n\n");
    
    while (1) {
        display_menu();
        printf("선택: ");
        scanf("%d", &choice);
        
        // 종료 조건
        if (choice == 5) {
            printf("\n프로그램을 종료합니다.\n");
            break;
        }
        
        // 잘못된 선택
        if (choice < 1 || choice > 5) {
            printf("\n잘못된 선택입니다. 다시 선택해주세요.\n\n");
            continue;
        }
        
        // 숫자 입력
        printf("첫 번째 숫자: ");
        scanf("%lf", &num1);
        printf("두 번째 숫자: ");
        scanf("%lf", &num2);
        
        // 연산 수행
        switch (choice) {
            case 1:
                result = add(num1, num2);
                printf("\n%.2f + %.2f = %.2f\n\n", num1, num2, result);
                break;
            case 2:
                result = subtract(num1, num2);
                printf("\n%.2f - %.2f = %.2f\n\n", num1, num2, result);
                break;
            case 3:
                result = multiply(num1, num2);
                printf("\n%.2f * %.2f = %.2f\n\n", num1, num2, result);
                break;
            case 4:
                if (num2 == 0) {
                    printf("\n오류: 0으로 나눌 수 없습니다!\n\n");
                } else {
                    result = divide(num1, num2);
                    printf("\n%.2f / %.2f = %.2f\n\n", num1, num2, result);
                }
                break;
        }
    }
    
    return 0;
}

// 메뉴 출력 함수
void display_menu() {
    printf("========== 메뉴 ==========\n");
    printf("1. 덧셈 (+)\n");
    printf("2. 뺄셈 (-)\n");
    printf("3. 곱셈 (*)\n");
    printf("4. 나눗셈 (/)\n");
    printf("5. 종료\n");
    printf("==========================\n");
}

// 덧셈 함수
double add(double a, double b) {
    return a + b;
}

// 뺄셈 함수
double subtract(double a, double b) {
    return a - b;
}

// 곱셈 함수
double multiply(double a, double b) {
    return a * b;
}

// 나눗셈 함수
double divide(double a, double b) {
    return a / b;
}

/*
 * 실행 예시:
 * 
 * ====================================
 *      간단한 계산기 프로그램
 * ====================================
 * 
 * ========== 메뉴 ==========
 * 1. 덧셈 (+)
 * 2. 뺄셈 (-)
 * 3. 곱셈 (*)
 * 4. 나눗셈 (/)
 * 5. 종료
 * ==========================
 * 선택: 1
 * 첫 번째 숫자: 10
 * 두 번째 숫자: 5
 * 
 * 10.00 + 5.00 = 15.00
 */

