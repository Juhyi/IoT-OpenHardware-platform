from flask import Flask

app = Flask(__name__)		# name 이름을 통한 falsk 객체 생성

@app.route("/")		# 라우팅을 위한 뷰함수 등록
def hello():
	return "집에 가고싶엉!!"

if __name__ == "__main__":		#터미널에서 직접 시행시키면 실행파일이 main으로 바뀐다.
	app.run(host="0.0.0.0", port="10111", debug=True)		# 실행을 위한 명령문으로 생각하면 됨
	
