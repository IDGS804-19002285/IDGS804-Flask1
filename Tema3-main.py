from flask import Flask

app = Flask (__name__)

@app.route("/")
def index():
    return "Hola Mundo"

@app.route("/user/<string:user>")
def user(user):
    return "Hola "+ user

@app.route("/numero/<int:n>")
def numero(n):
    return "numero: {}".format(n)

@app.route("/username/<int:id>/<string:username>")
def usern(id,username):
    return "ID: {} nombre: {}".format(id,username)


if __name__=='__main__':
    app.run(debug=True,port=3000)