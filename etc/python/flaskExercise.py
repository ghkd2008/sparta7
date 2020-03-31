from flask import Flask, render_template

app = Flask(__name__)
#일반적인 형식 (__name__)


@app.route('/')   #<----의미중요! root경로로 오면 이 함수를 실행할거야.
def home():
   return render_template("homework1.html")  #render_template() alt+ent로 import하면 됨. flask에 내장된 함수.

@app.route('/music')   #<----의미중요! /music경로로 오면 이 함수를 실행할거야.
def music():
   return 'This is Music!'

@app.route('/music/top100')   #<----의미중요! root경로로 오면 이 함수를 실행할거야.
def music100():
   return 'This is Top 100!'

#결국 return하는게 html이니까 html 써넣어도됨. 근데 html은 코드가 기니까 html파일을 저장하고 그 경로랑 연결 해줌.
#즉, 이 서버 파이썬 파일과 같은 레벨에 templates 폴더 만들기!! 이름은 무조건 templates로 고정! 그 안에 html 파일 저장.



#재생버튼 누르면 자동으로 되는거
#즉, 너 재생버튼 눌렀니?
#if문 생략가능
if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True) #주소는 이 컴퓨터, 5000포트 기본사용, debug=True를 사용함으로써 알아서 재기동을 함. 즉, 껐다켜졌다 알아서 함.
   #프로그램이 계속 돌아감. 중지시키지 않으면 아래줄로 안내려감
   #즉, 이 명령이 제일 마지막에 와야겠지.




