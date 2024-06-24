from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def get():
	value1 = request.args.get("이름", "user")
	value2 = request.args.get("주소", "부산")
	return "<h3>이름 :</h3>" + value1  +"<h1>주소 :</h1>" + value2

if __name__ == "__main__":
	app.run(host="0.0.0.0", port="10011", debug=True)
