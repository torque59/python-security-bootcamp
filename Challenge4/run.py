from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/secret")
def secret():
    return "s0lvingpyth0n1sfun"

@app.route("/")
def check():
    sol = "s0lvingpyth0n1sfun"
    flag = request.args.get('flag')
    if flag:
        length = len(flag)
        if flag[:length] == sol[:length]:
            return "true"
        elif flag == "s0lvingpyth0n1sfun":
            return "Your flag is s0lvingpyth0n1sfun"
        else:
			return "false"
    else:
		return "false"

if __name__ == "__main__":
    app.run()
