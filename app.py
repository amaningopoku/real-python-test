from flask import Flask

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route("/")
@app.route("/hello")

def hello_world():
	return "Hello, World! I am Prince Opoku Amaning "

@app.route("/test")
def search():
	return "hello"

@app.route("/integer/<int:value>")
def int_type(value):
	print(value + 1)
	return "Correct"

@app.route("/float/<float:value>")
def float_type(value):
	print(value + 1)
	return "Correct"

@app.route("/path/<path:value>")
def path_type(value):
	print(value)
	return "Correct"

@app.route("/name/<name>")
def index(name):
	if name.lower() == "michael":
		return "Hello, {}".format(name), 200
	else:
		return "Not Found", 404

if __name__ == "__main__":
	app.run()