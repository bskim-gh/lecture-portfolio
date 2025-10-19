/*
 * 예제: 학생 성적 관리 프로그램
 * 
 * 기능:
 * - 학생 정보 입력
 * - 성적 통계 (평균, 최고점, 최저점)
 * - 학점 계산
 * - 파일 저장 및 불러오기
 */

#include <stdio.h>
#include <string.h>

#define MAX_STUDENTS 50

// 학생 구조체
typedef struct {
    int id;
    char name[50];
    int korean;
    int english;
    int math;
    float average;
    char grade;
} Student;

// 함수 프로토타입
void input_student(Student *s, int id);
void calculate_stats(Student *s);
char calculate_grade(float avg);
void display_student(Student s);
void display_all_students(Student students[], int count);
void display_statistics(Student students[], int count);
void save_to_file(Student students[], int count);
int load_from_file(Student students[]);

int main() {
    Student students[MAX_STUDENTS];
    int student_count = 0;
    int choice;
    
    printf("====================================\n");
    printf("    학생 성적 관리 프로그램\n");
    printf("====================================\n\n");
    
    while (1) {
        printf("\n========== 메뉴 ==========\n");
        printf("1. 학생 추가\n");
        printf("2. 전체 학생 조회\n");
        printf("3. 통계 보기\n");
        printf("4. 파일로 저장\n");
        printf("5. 파일에서 불러오기\n");
        printf("6. 종료\n");
        printf("==========================\n");
        printf("선택: ");
        scanf("%d", &choice);
        
        switch (choice) {
            case 1:
                if (student_count < MAX_STUDENTS) {
                    input_student(&students[student_count], student_count + 1);
                    calculate_stats(&students[student_count]);
                    student_count++;
                    printf("\n학생 정보가 추가되었습니다.\n");
                } else {
                    printf("\n더 이상 학생을 추가할 수 없습니다.\n");
                }
                break;
                
            case 2:
                if (student_count == 0) {
                    printf("\n등록된 학생이 없습니다.\n");
                } else {
                    display_all_students(students, student_count);
                }
                break;
                
            case 3:
                if (student_count == 0) {
                    printf("\n등록된 학생이 없습니다.\n");
                } else {
                    display_statistics(students, student_count);
                }
                break;
                
            case 4:
                if (student_count == 0) {
                    printf("\n저장할 학생 정보가 없습니다.\n");
                } else {
                    save_to_file(students, student_count);
                    printf("\n파일에 저장되었습니다.\n");
                }
                break;
                
            case 5:
                student_count = load_from_file(students);
                if (student_count > 0) {
                    printf("\n%d명의 학생 정보를 불러왔습니다.\n", student_count);
                }
                break;
                
            case 6:
                printf("\n프로그램을 종료합니다.\n");
                return 0;
                
            default:
                printf("\n잘못된 선택입니다.\n");
        }
    }
    
    return 0;
}

// 학생 정보 입력
void input_student(Student *s, int id) {
    s->id = id;
    
    printf("\n학생 이름: ");
    scanf("%s", s->name);
    
    printf("국어 점수: ");
    scanf("%d", &s->korean);
    
    printf("영어 점수: ");
    scanf("%d", &s->english);
    
    printf("수학 점수: ");
    scanf("%d", &s->math);
}

// 평균과 학점 계산
void calculate_stats(Student *s) {
    s->average = (s->korean + s->english + s->math) / 3.0f;
    s->grade = calculate_grade(s->average);
}

// 학점 계산
char calculate_grade(float avg) {
    if (avg >= 90) return 'A';
    else if (avg >= 80) return 'B';
    else if (avg >= 70) return 'C';
    else if (avg >= 60) return 'D';
    else return 'F';
}

// 학생 정보 출력
void display_student(Student s) {
    printf("%3d %-10s %4d %4d %4d %6.2f %4c\n",
           s.id, s.name, s.korean, s.english, s.math, s.average, s.grade);
}

// 전체 학생 출력
void display_all_students(Student students[], int count) {
    printf("\n========================================\n");
    printf("학번 이름       국어 영어 수학 평균   학점\n");
    printf("========================================\n");
    
    for (int i = 0; i < count; i++) {
        display_student(students[i]);
    }
    
    printf("========================================\n");
}

// 통계 정보 출력
void display_statistics(Student students[], int count) {
    float total_avg = 0;
    float max_avg = students[0].average;
    float min_avg = students[0].average;
    int max_idx = 0, min_idx = 0;
    
    for (int i = 0; i < count; i++) {
        total_avg += students[i].average;
        
        if (students[i].average > max_avg) {
            max_avg = students[i].average;
            max_idx = i;
        }
        
        if (students[i].average < min_avg) {
            min_avg = students[i].average;
            min_idx = i;
        }
    }
    
    total_avg /= count;
    
    printf("\n========== 통계 정보 ==========\n");
    printf("총 학생 수: %d명\n", count);
    printf("전체 평균: %.2f\n", total_avg);
    printf("\n최고 성적:\n");
    printf("  이름: %s\n", students[max_idx].name);
    printf("  평균: %.2f (학점: %c)\n", max_avg, students[max_idx].grade);
    printf("\n최저 성적:\n");
    printf("  이름: %s\n", students[min_idx].name);
    printf("  평균: %.2f (학점: %c)\n", min_avg, students[min_idx].grade);
    printf("==============================\n");
}

// 파일로 저장
void save_to_file(Student students[], int count) {
    FILE *fp = fopen("students.dat", "wb");
    
    if (fp == NULL) {
        printf("파일을 열 수 없습니다.\n");
        return;
    }
    
    fwrite(&count, sizeof(int), 1, fp);
    fwrite(students, sizeof(Student), count, fp);
    
    fclose(fp);
}

// 파일에서 불러오기
int load_from_file(Student students[]) {
    FILE *fp = fopen("students.dat", "rb");
    
    if (fp == NULL) {
        printf("\n파일을 열 수 없습니다.\n");
        return 0;
    }
    
    int count;
    fread(&count, sizeof(int), 1, fp);
    fread(students, sizeof(Student), count, fp);
    
    fclose(fp);
    return count;
}

/*
 * 실행 예시:
 * 
 * ====================================
 *     학생 성적 관리 프로그램
 * ====================================
 * 
 * ========== 메뉴 ==========
 * 1. 학생 추가
 * 2. 전체 학생 조회
 * 3. 통계 보기
 * 4. 파일로 저장
 * 5. 파일에서 불러오기
 * 6. 종료
 * ==========================
 * 선택: 1
 * 
 * 학생 이름: 홍길동
 * 국어 점수: 85
 * 영어 점수: 90
 * 수학 점수: 88
 * 
 * 학생 정보가 추가되었습니다.
 */

