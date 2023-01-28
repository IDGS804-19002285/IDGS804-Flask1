from flask import Flask
from flask import request

app = Flask (__name__)

@app.route("/suma", methods=["GET","POST"])
def suma():
    if request.method=='POST':

        num1= int(request.form.get("num1"))
        num2= int(request.form.get("num2"))
        res = 0

        if(request.form.get('suma') == 'Sum'):
            res = num1 + num2
        if(request.form.get('suma')== 'Res'):
            res = num1 - num2
        if(request.form.get('suma') == 'Mul'):
            res = num1 * num2
        if(request.form.get('suma') == 'Div'):
            res = num1 / num2
        return "<h1>El resultado es : {} </h1>".format(str(int(res)))
    else:
        return'''

            <form action="/suma" method="POST">
            <input type="radio" name="suma" value="Sum"/>Suma</br></br>
            <input type="radio" name="suma" value="Res"/>Resta</br></br>
            <input type="radio" name="suma" value="Mul"/>Multiplicacion</br></br>
            <input type="radio" name="suma" value="Div"/>Division</br></br>
            <label>N1: </label>
            <input type="text" name="num1"/></br></br>
            <label>N2: </label>
            <input type="text" name="num2"/></br></br>
            <input type="submit" value="Calcular"/></br></br>
            </form>

        '''

if __name__=='__main__':
    app.run(debug=True,port=3000)