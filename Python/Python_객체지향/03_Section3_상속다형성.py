# Section 3: 상속과 다형성
# 상속 기본, 메서드 오버라이딩, 다중 상속

print("=" * 50)
print("Section 3: 상속과 다형성")
print("=" * 50)

# =============================================================================
# 1. 상속 기본
# =============================================================================
print("\n1. 상속 기본")
print("-" * 30)

class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))

class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        # 명시적으로 부모의 생성자 메소드 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1}, subject; {2}, stdent ID: {3})".format(
            self.name, self.phoneNumber, self.subject, self.studentID))

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
p.printInfo()
s.printInfo()
print("Student 인스턴스 속성:", s.__dict__)

# =============================================================================
# 2. 부모 클래스 생성자 호출
# =============================================================================
print("\n2. 부모 클래스 생성자 호출")
print("-" * 30)

class Person:
    def __init__(self, name, phoneNumber):
        self.Name = name
        self.PhoneNumber = phoneNumber
    
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.Name, self.PhoneNumber))

class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        Person.__init__(self, name, phoneNumber) 
        self.Subject = subject
        self.StudentId = studentID

# 인스턴스 생성
student = Student("홍길동", "010-1234-5678", "컴퓨터공학", "2021001")
student.printInfo()

# =============================================================================
# 3. 메서드 재정의 (오버라이딩)
# =============================================================================
print("\n3. 메서드 재정의 (오버라이딩)")
print("-" * 30)

class Person:
    " Super Class "
    def __init__(self, name, phoneNumber):
        self.Name = name 
        self.PhoneNumber = phoneNumber
    
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.Name, 
                        self.PhoneNumber))
   
class Student(Person):
    " Sub Class "
    def __init__(self, name, phoneNumber, subject, studentID):
        #명시적으로 Person 생성자를 호출
        Person.__init__(self, name, phoneNumber)
        self.Subject = subject
        self.StudentID = studentID
    
    def printInfo(self): #Person의 PrintInfo()메서드를 재정의
        print("Info(Name:{0}, Phone Number:{1})".format(self.Name, self.PhoneNumber))
        print("Info(Subject:{0}, Student ID:{1})".format(self.Subject, self.StudentID))
        
p = Person("전우치", "010-222-3333")
s = Student("이순신", "010-333-4444", "컴공", "990000")
p.printInfo()
s.printInfo()

# =============================================================================
# 4. 다중 상속 기본
# =============================================================================
print("\n4. 다중 상속 기본")
print("-" * 30)

class Tiger:
    def jump(self):
        print("호랑이 점프")

class Lion:
    def bite(self):
        print("사자 물어뜯기")

class Liger(Tiger, Lion):
    def play(self):
        print("라이거와 놀기")

l = Liger()
l.play()
l.jump()
l.bite()

# =============================================================================
# 5. MRO (Method Resolution Order)
# =============================================================================
print("\n5. MRO (Method Resolution Order)")
print("-" * 30)

class Tiger:
    def cry(self):
        print("호랑이 어흥~~")

class Lion:
    def cry(self):
        print("사자 으르릉~~")

class Liger(Tiger, Lion):  
    def play(self):
        print("라이거와 놀기")

l = Liger()
l.cry()  # Tiger의 cry가 호출됨 (MRO 순서)
print("Liger클래스의 MRO:", Liger.__mro__)

# =============================================================================
# 6. isinstance 함수로 상속 관계 확인
# =============================================================================
print("\n6. isinstance 함수로 상속 관계 확인")
print("-" * 30)

class Person:
    pass

class Bird:
    pass

class Student(Person):
    pass

p, s = Person(), Student()
print("p is instance of Person: ", isinstance(p, Person))
print("s is instance of Person: ", isinstance(s, Person))
print("p is instance of Object: ", isinstance(p, object))
print("p is instance of Bird: ", isinstance(p, Bird))
print("int is instance of Object: ", isinstance(int, object))

# =============================================================================
# 7. 개발자 클래스 상속 예제
# =============================================================================
print("\n7. 개발자 클래스 상속 예제")
print("-" * 30)

#상속 연습
class Developer:
    def __init__(self, name):
        self.name = name 
    
    def getSalary(self, day):
        result = day * 50000
        print("개발자 월급:", result)

class WebDeveloper(Developer):
    def __init__(self, name, skill):
        Developer.__init__(self, name)
        self.skill = skill
    
    def getSalary(self, day):
        result = day * 150000
        print("웹 개발자 월급:", result)
    
class MobileDeveloper(Developer):
    def __init__(self, name, skill):
        Developer.__init__(self, name)
        self.skill = skill 
    
    def getSalary(self, day):
        result = day * 250000
        print("모바일 개발자 월급:", result)

#인스턴스 생성
dev = Developer("전우치")
webDev = WebDeveloper("이순신", "ASP.NET")
mobileDev = MobileDeveloper("박문수", "iOS")

dev.getSalary(20)
webDev.getSalary(20)
mobileDev.getSalary(20)

print("\n" + "=" * 50)
print("Section 3 완료!")
print("=" * 50)
