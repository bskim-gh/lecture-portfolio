# Section 6: 웹 개발 기초

## 📚 학습 목표
- Flask와 Django 웹 프레임워크 이해
- 웹 애플리케이션 구축과 데이터 표시 방법 학습
- 사용자 입력 처리와 데이터 저장 구현

---

## 6-1. Flask 또는 Django 소개

Flask와 Django는 파이썬 웹 프레임워크로, 웹 애플리케이션을 구축하기 위한 도구입니다.

### Flask 소개

Flask는 간결하고 가벼운 마이크로 웹 프레임워크로, 웹 애플리케이션의 기본 기능을 제공하면서도 사용자에게 유연성과 확장성을 제공합니다. 작은 규모의 프로젝트나 간단한 API를 개발할 때 적합한 선택입니다.

**Flask 예제: 간단한 웹 애플리케이션**

```python
# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/user/<username>')
def user_profile(username):
    return render_template('user_profile.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
```

위 예제는 Flask를 사용하여 간단한 웹 애플리케이션을 만드는 방법을 보여줍니다. `/` 경로로 접속하면 "Hello, World!"를 반환하고, `/user/<username>` 경로로 접속하면 해당 유저의 프로필 페이지를 템플릿을 이용하여 보여줍니다.

### Django 소개

Django는 강력한 웹 프레임워크로, 웹 애플리케이션의 전체 개발에 필요한 기능을 제공합니다. 모듈화된 구조와 자동화된 기능으로 복잡한 프로젝트를 구축하기에 적합하며, 기본적인 기능들이 이미 구현되어 있어 빠르게 개발할 수 있습니다.

**Django의 주요 특징:**
- **MVT(Model-View-Template) 패턴**: 모델, 뷰, 템플릿을 분리하여 구조화된 개발
- **ORM(Object-Relational Mapping)**: 데이터베이스를 Python 객체로 다룸
- **Admin 인터페이스**: 자동으로 생성되는 관리자 페이지
- **보안**: CSRF, XSS, SQL Injection 등에 대한 보호 기능 내장

---

## 6-2. 웹 애플리케이션 구축과 데이터 표시

Flask를 사용하여 웹 애플리케이션을 구축하고, 데이터를 표시하는 방법을 보여드리겠습니다.

### 예제: 간단한 데이터 표시 웹 애플리케이션

**1. Flask 설치**

```bash
pip install Flask
```

**2. 프로젝트 구조**

```
my_app/
├── app.py
├── templates/
│   ├── index.html
│   └── data.html
└── data.csv
```

**3. app.py 코드**

```python
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def show_data():
    # CSV 파일 읽기
    df = pd.read_csv('data.csv')
    # DataFrame을 HTML 테이블로 변환
    table_html = df.to_html(classes='table table-striped', index=False)
    return render_template('data.html', table=table_html)

if __name__ == '__main__':
    app.run(debug=True)
```

**4. templates/index.html**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome to Data Display App</h1>
    <a href="/data">View Data</a>
</body>
</html>
```

**5. templates/data.html**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Data</title>
</head>
<body>
    <h1>Data Table</h1>
    {{ table|safe }}
    <br>
    <a href="/">Back to Home</a>
</body>
</html>
```

---

## 6-3. 사용자 입력 처리와 데이터 저장

사용자 입력 처리와 데이터 저장을 Flask를 사용하여 구현하는 방법을 보여드리겠습니다.

### 예제: 사용자 입력 처리와 데이터 저장

**1. Flask 설치**

```bash
pip install Flask
```

**2. 프로젝트 구조**

```
my_app/
├── app.py
├── templates/
│   ├── index.html
│   └── success.html
└── data.txt
```

**3. app.py 코드**

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # 폼에서 데이터 가져오기
    name = request.form['name']
    email = request.form['email']
    
    # 데이터를 파일에 저장
    with open('data.txt', 'a') as file:
        file.write(f"Name: {name}, Email: {email}\n")
    
    return render_template('success.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
```

**4. templates/index.html**

```html
<!DOCTYPE html>
<html>
<head>
    <title>User Input</title>
</head>
<body>
    <h1>Enter Your Information</h1>
    <form action="/submit" method="post">
        <label>Name:</label>
        <input type="text" name="name" required><br><br>
        
        <label>Email:</label>
        <input type="email" name="email" required><br><br>
        
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

**5. templates/success.html**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Success</title>
</head>
<body>
    <h1>Thank you, {{ name }}!</h1>
    <p>Your information has been saved.</p>
    <a href="/">Go Back</a>
</body>
</html>
```

---

## 📝 정리

Section 6에서는 다음 내용을 다루었습니다:
- Flask 마이크로 웹 프레임워크의 기본 개념
- Django 풀스택 웹 프레임워크의 주요 특징
- Flask를 사용한 웹 애플리케이션 구축
- CSV 데이터를 읽어 웹 페이지에 표시하는 방법
- 사용자 입력을 받아 파일에 저장하는 방법
- Flask의 라우팅, 템플릿, 폼 처리

Flask와 Django를 활용하면 간단한 웹 사이트부터 복잡한 웹 애플리케이션까지 다양한 프로젝트를 구현할 수 있습니다.

