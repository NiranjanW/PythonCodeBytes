from flask import Flask , render_template , request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/greet')
def greet():
    # if "name" in request.args:
    #     name = request.args["name"]
    # else:
    #     name = "world"
    name = request.args.get("name", 'world')
    return render_template("index.html" , name=name)
