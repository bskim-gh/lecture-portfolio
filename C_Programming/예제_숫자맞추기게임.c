/*
 * 예제: 숫자 맞추기 게임
 * 
 * 기능:
 * - 랜덤 숫자 생성
 * - 사용자 입력
 * - 힌트 제공 (Up/Down)
 * - 시도 횟수 카운트
 * - 난이도 선택
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// 함수 프로토타입
void display_intro(void);
int select_difficulty(void);
int generate_random(int max);
void play_game(int max_number, int max_attempts);
void display_result(int attempts, int max_attempts, int found);

int main() {
    int difficulty;
    int max_number, max_attempts;
    char play_again;
    
    // 난수 생성기 초기화
    srand(time(NULL));
    
    display_intro();
    
    do {
        // 난이도 선택
        difficulty = select_difficulty();
        
        // 난이도에 따른 설정
        switch (difficulty) {
            case 1:  // 쉬움
                max_number = 50;
                max_attempts = 10;
                break;
            case 2:  // 보통
                max_number = 100;
                max_attempts = 8;
                break;
            case 3:  // 어려움
                max_number = 200;
                max_attempts = 6;
                break;
            default:
                max_number = 100;
                max_attempts = 8;
        }
        
        // 게임 시작
        play_game(max_number, max_attempts);
        
        // 재시작 여부
        printf("\n다시 플레이하시겠습니까? (y/n): ");
        scanf(" %c", &play_again);
        printf("\n");
        
    } while (play_again == 'y' || play_again == 'Y');
    
    printf("게임을 종료합니다. 감사합니다!\n");
    
    return 0;
}

// 게임 소개
void display_intro() {
    printf("====================================\n");
    printf("      숫자 맞추기 게임\n");
    printf("====================================\n");
    printf("컴퓨터가 생각한 숫자를 맞춰보세요!\n");
    printf("힌트를 보고 범위를 좁혀가세요.\n");
    printf("====================================\n\n");
}

// 난이도 선택
int select_difficulty() {
    int choice;
    
    printf("========== 난이도 선택 ==========\n");
    printf("1. 쉬움   (1-50,  10번 시도)\n");
    printf("2. 보통   (1-100, 8번 시도)\n");
    printf("3. 어려움 (1-200, 6번 시도)\n");
    printf("================================\n");
    printf("선택 (1-3): ");
    scanf("%d", &choice);
    printf("\n");
    
    if (choice < 1 || choice > 3) {
        printf("잘못된 선택입니다. 보통 난이도로 시작합니다.\n\n");
        return 2;
    }
    
    return choice;
}

// 랜덤 숫자 생성
int generate_random(int max) {
    return (rand() % max) + 1;
}

// 게임 진행
void play_game(int max_number, int max_attempts) {
    int target = generate_random(max_number);
    int guess;
    int attempts = 0;
    int found = 0;
    
    printf("게임 시작!\n");
    printf("1부터 %d 사이의 숫자를 맞춰보세요.\n", max_number);
    printf("기회는 총 %d번입니다.\n\n", max_attempts);
    
    while (attempts < max_attempts) {
        printf("시도 %d/%d - 숫자를 입력하세요: ", attempts + 1, max_attempts);
        scanf("%d", &guess);
        attempts++;
        
        // 범위 체크
        if (guess < 1 || guess > max_number) {
            printf("❌ 범위를 벗어났습니다! (1-%d)\n\n", max_number);
            attempts--;  // 잘못된 입력은 카운트하지 않음
            continue;
        }
        
        // 정답 확인
        if (guess == target) {
            found = 1;
            printf("🎉 정답입니다!\n");
            break;
        } else if (guess < target) {
            printf("⬆️  Up! 더 큰 숫자입니다.\n");
        } else {
            printf("⬇️  Down! 더 작은 숫자입니다.\n");
        }
        
        // 힌트 제공 (가까운 경우)
        int diff = abs(guess - target);
        if (diff <= 5) {
            printf("💡 힌트: 아주 가깝습니다!\n");
        } else if (diff <= 10) {
            printf("💡 힌트: 가깝습니다!\n");
        }
        
        printf("\n");
    }
    
    // 결과 출력
    display_result(attempts, max_attempts, found);
    
    if (!found) {
        printf("정답은 %d 였습니다.\n", target);
    }
}

// 결과 출력
void display_result(int attempts, int max_attempts, int found) {
    printf("\n====================================\n");
    printf("          게임 종료\n");
    printf("====================================\n");
    
    if (found) {
        printf("축하합니다! %d번 만에 맞추셨습니다!\n", attempts);
        
        // 평가
        if (attempts <= max_attempts / 3) {
            printf("평가: ⭐⭐⭐ 천재!\n");
        } else if (attempts <= max_attempts * 2 / 3) {
            printf("평가: ⭐⭐ 훌륭해요!\n");
        } else {
            printf("평가: ⭐ 성공!\n");
        }
    } else {
        printf("아쉽네요! 기회를 모두 사용했습니다.\n");
        printf("다시 도전해보세요!\n");
    }
    
    printf("====================================\n");
}

/*
 * 실행 예시:
 * 
 * ====================================
 *       숫자 맞추기 게임
 * ====================================
 * 컴퓨터가 생각한 숫자를 맞춰보세요!
 * 힌트를 보고 범위를 좁혀가세요.
 * ====================================
 * 
 * ========== 난이도 선택 ==========
 * 1. 쉬움   (1-50,  10번 시도)
 * 2. 보통   (1-100, 8번 시도)
 * 3. 어려움 (1-200, 6번 시도)
 * ================================
 * 선택 (1-3): 2
 * 
 * 게임 시작!
 * 1부터 100 사이의 숫자를 맞춰보세요.
 * 기회는 총 8번입니다.
 * 
 * 시도 1/8 - 숫자를 입력하세요: 50
 * ⬆️  Up! 더 큰 숫자입니다.
 * 
 * 시도 2/8 - 숫자를 입력하세요: 75
 * ⬇️  Down! 더 작은 숫자입니다.
 * 
 * 시도 3/8 - 숫자를 입력하세요: 62
 * ⬆️  Up! 더 큰 숫자입니다.
 * 💡 힌트: 가깝습니다!
 * 
 * 시도 4/8 - 숫자를 입력하세요: 68
 * 🎉 정답입니다!
 * 
 * ====================================
 *           게임 종료
 * ====================================
 * 축하합니다! 4번 만에 맞추셨습니다!
 * 평가: ⭐⭐ 훌륭해요!
 * ====================================
 */

